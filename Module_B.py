import os
import platform
import json
import shutil
import re
import requests
import Module_A as a
import Module_D as d
from bs4 import BeautifulSoup

userPath = os.path.expanduser("~")
configPath = os.path.join(userPath, "PyTerm", "config.json")

# Commands
def cd(prompt_, ActiveDirectory):
    path = ""
    for i in prompt_[1:]:
        if not i.startswith("-"):
            path = i
            break
        else:
            path = ""
    if path == "" or path == "~":
        return {'ActiveDirectory': userPath}
    else:
        if ".." in path:
            if os.sep in path:
                NumDobleDot = len(re.findall(r'\.\.', path))
                UseDirectory = ActiveDirectory
                for i in range(0, NumDobleDot):
                    UseDirectory = os.path.split(UseDirectory)[0]
                return {'ActiveDirectory': UseDirectory}
            else:
                if path == "..":
                    return {'ActiveDirectory': os.path.split(ActiveDirectory)[0]}
        elif path == ".":
            return {'ActiveDirectory': ActiveDirectory}
        else:
            if path.startswith("./") or path.startswith(".\\"):
                path = path[1:]
            result = d.normalDir(ActiveDirectory, path)
            if 'value' in result:
                return {'ActiveDirectory': result['value']}
            else:
                return {'error': result['error']}

def ls(prompt_, ActiveDirectory):
    def custom_print(lista):
        for i in range(0, len(lista), 3):
            fila = lista[i:i+3]
            print("".join(word.ljust(15) for word in fila))

    if len(prompt_) > 1:
        path = ""
        for i in prompt_[1:]:
            if not i.startswith("-"):
                path = i
                break
            else:
                custom_print(os.listdir(ActiveDirectory))
                return
        if os.path.exists(path):
            custom_print(os.listdir(path))
        else:
            return {'error':'path not found'}
    else:
        custom_print(os.listdir(ActiveDirectory))
        return

def cat(prompt_, ActiveDirectory):
    def run(num):
        if os.path.isfile(prompt_[num]):
            try:
                with open(prompt_[num], 'r') as f:
                    print(f.read(), "a")
            except FileNotFoundError:
                return {'error': f'file "{prompt_[num]}" not found'}
        elif os.path.isfile(os.path.join(ActiveDirectory, prompt_[num])):
            try:
                with open(os.path.join(ActiveDirectory, prompt_[num]), 'r') as f:
                    print(f.read(), "a")
            except FileNotFoundError:
                return {'error': f'file "{prompt_[num]}" not found'}
        else:
            return {'error': f'file "{prompt_[num]}" not found'}
    Nl = len(prompt_) - 1
    if Nl == 0:
        run(1)
    else:
        for i in range(1, Nl):
            run(i)

def pwd(prompt_, ActiveDirectory):
    print(ActiveDirectory)

def mkdir(prompt_, ActiveDirectory):
    path = ""
    for i in prompt_[1:]:
        if not i.startswith("-"):
            path = i
            break
        else:
            path = ""
    if os.path.exists(os.path.split(path)[0]):
        os.mkdir(path)
    elif os.path.exists(os.path.split(os.path.join(ActiveDirectory, path))[0]):
        os.mkdir(os.path.join(ActiveDirectory, path))
    else:
        return {'error':'path not found'}

def rm(prompt_, ActiveDirectory):
    path = ""
    for i in prompt_[1:]:
        if not i.startswith("-"):
            path = i
            break
        else:
            path = ""
    try:
        if os.path.isfile(path):  # Verificar si la ruta es un archivo
            os.remove(path)
            return {'mensaje': f"El archivo {path} ha sido eliminado correctamente."}
        elif os.path.isdir(path):  # Verificar si la ruta es un directorio
            shutil.rmtree(path)
            return {'mensaje': f"El directorio {path} y su contenido han sido eliminados correctamente."}
        else:
            return {'error': f"La ruta {path} no corresponde a un archivo ni a un directorio."}
    except OSError as e:
        return {'error': f"Error al eliminar la ruta {path}: {e}"}

def navigate(prompt_, ActiveDirectory): # Errores varios...
    def search(url):
        response = requests.get(url)
        html_content = response.text
        soup = BeautifulSoup(html_content, "html.parser")
        PatronGenerico = r'<(.*?)>' ; PatronAbiertos = r'<(?!.*?/).*?>' ; PatronCerrados = r'</(.*?)>' ; PatronUni = r'<.*?/>'
        elementDict = dict
        open_list = []
        close_list = []
        uni_list = []
        for elemento in re.findall(PatronGenerico, soup):
            if re.match(PatronAbiertos, elemento):
                elementDict[elemento] = "Open"
            elif  re.match(PatronCerrados, elemento):
                elementDict[elemento] = "Close"
            elif re.match(PatronUni, elemento):
                elementDict[elemento] = "Uni"
            else:
                elementDict[elemento] = "Error"


    while(True):
        url = input("Type your url  or 'exit' to go back\n>> ")
        if url == 'exit':
            break
        if "http" not in url:
            url = f"http://{url}"
        search(url)


def grep(prompt_, ActiveDirectory):
    def manyarguments(lista):
        contador = 0
        for elemento in lista:
            if elemento in ["-r", "-f", "-t"]:
                contador += 1
                if contador >= 2:
                    return True
        return False
    
    def listTextFiles(dirpath):
        archivos_texto = []
        for root, dirs, files in os.walk(dirpath):
            for file in files:
                archivo = os.path.join(root, file)
                if os.path.isfile(archivo) and os.access(archivo, os.R_OK):
                    archivos_texto.append(archivo)
        return archivos_texto
    
    Npath = next((i for i, x in enumerate(prompt_[1:], 1) if not x.startswith("-")), None)
    
    if len(prompt_) >= 4:
        filter_ = prompt_[3]
    
    if "-r" not in prompt_ and "-f" not in prompt_ and "-t" not in prompt_:
        return {'error':'grep needs arguments, type "help grep" for help'}
    
    if manyarguments(prompt_):
        return {'error':'Grep can only have 1 main argument, type "help grep" for help'}
    
    if "-r" in prompt_:
        print(prompt_)
        if len(prompt_) < 4:
            return {'error':'syntax error grep -r <directory path> <filter>'}
        else:
            if "-c" in prompt_ and "-l" in prompt_:
                return {'error':'Grep -f can only have 1 secondary argument'}
            try:
                startDirectory = d.normalDir(ActiveDirectory, prompt_[Npath])['value']
            except:
                return {'error':d.normalDir(ActiveDirectory ,prompt_[Npath])['error']}
            textFiles = listTextFiles(startDirectory)
            dictData = {}
            routes = []
            for file_ in textFiles:
                try:
                    with open(file_, 'r') as f:
                        dictData[file_] = f.read()
                except :
                    pass  
            CounterR = 0
            for key in dictData.keys():
                if filter_ in dictData[key]:  # Verificar si el filtro está en el contenido del archivo
                    CounterR += 1  # Incrementar CounterR solo si se encuentra el filtro
                    routes.append(key)
                    if "-l" in prompt_:
                        for line in dictData[key].split("\n"):
                            if filter_ in line:
                                print(line)


            if "-c" in prompt_:
                print(CounterR)
            elif "-l" not in prompt_:
                for i in routes:
                    print(i)
    
    if "-f" in prompt_:
        if "-c" in prompt_ and "-l" in prompt_:
            return {'error':'Grep -f can only have 1 secondary argument'}
        try:
            filePath = d.normalFile(ActiveDirectory, prompt_[Npath])['value']
            print(filePath)
        except:
            return {'error':d.normalDir(ActiveDirectory, prompt_[Npath])['error']}
        print(filePath)
        if "-c" in prompt_:
            with open(filePath, "r") as f:
                CounterF = f.read().count(filter_)
            print(CounterF)
        else:
            with open(filePath, "r") as f:
                pass
    
    if "-t" in prompt_:
        pass



def exit_(a,b):
    exit()
