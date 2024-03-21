import os, platform, json, shutil, re
import requests
import Module_A as a
from bs4 import BeautifulSoup

userPath = os.path.expanduser("~")
configPath = f'{userPath}{os.sep}PyTerm{os.sep}config.json'

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
        return {'ActiveDirectory':userPath}
    else:
        if ".." in path:
            if os.sep in path:
                NumDobleDot = len(re.findall(r'\.\.', path))
                UseDirectory = ActiveDirectory
                for i in range(0,NumDobleDot):
                    UseDirectory = os.path.split(UseDirectory)[0]
                return {'ActiveDirectory':UseDirectory}
            else:
                if path == "..":
                    return {'ActiveDirectory':os.path.split(ActiveDirectory)[0]}
        else:
            if path.startswith("./") or path.startswith(".\\"):
                path = path[1:]
            if os.path.exists(path):
                if path[-1:] == os.sep:
                    newPath = f"{ActiveDirectory}{path}"
                else:
                    newPath = f"{ActiveDirectory}{os.sep}{path}"
                if os.path.exists(newPath):
                    return{'ActiveDirectory':newPath}
                else:
                    return{'error':'path not found'}
            else:
                if path[-1:] == os.sep:
                    newPath = f"{ActiveDirectory}{path}"
                else:
                    newPath = f"{ActiveDirectory}{os.sep}{path}"
                if os.path.exists(newPath):
                    return{'ActiveDirectory':newPath}
                else:
                    return{'error':'path not found'}
    
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
            f = open(prompt_[num])
            print(f.read(), "a")
            f.close()
        elif os.path.isfile(f"{ActiveDirectory}{os.sep}{prompt_[num]}"):
            f = open(f"{ActiveDirectory}{os.sep}{prompt_[num]}")
            print(f.read(), "a")
            f.close()
        else:
            return {'error':f'file "{prompt_[num]}" not found'}
    Nl = len(prompt_)-1 ; errorL = []
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
    elif os.path.exists(os.path.split(f"{ActiveDirectory}{path}")[0]):
        os.mkdir(f"{ActiveDirectory}{path}")
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

def navigate(prompt_, ActiveDirectory):
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
    pass
    
def exit_(a,b):
    exit()