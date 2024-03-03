import os
import platform
import subprocess

def instalar_pip3():
    sistema_operativo = platform.system()
    if sistema_operativo == "Linux":
        distribucion = platform.linux_distribution()[0].lower()
        if distribucion in ["debian", "ubuntu"]:
            subprocess.call(["sudo", "apt-get", "install", "-y", "python3-pip"])
        elif distribucion == "fedora":
            subprocess.call(["sudo", "dnf", "install", "-y", "python3-pip"])
        elif distribucion == "arch":
            subprocess.call(["sudo", "pacman", "-S", "--noconfirm", "python-pip"])

def instalar_librerias(lista_librerias):
    sistema_operativo = platform.system()

    if sistema_operativo == "Windows":
        subprocess.call(['pip', 'install'] + lista_librerias)
    elif sistema_operativo == "Linux":
        pip3_path = subprocess.check_output("which pip3", shell=True).decode().strip()
        if not pip3_path:
            instalar_pip3()
            pip3_path = subprocess.check_output("which pip3", shell=True).decode().strip()
        if pip3_path:
            subprocess.call(["pip3", 'install'] + lista_librerias)
        else:
            print("Error: pip3 can't be installed, try manual mode.")
    else:
        print("Error: S.O. not supported.")

print("You want to install PyTerminal? (Y/n)")

yn = input(">> ")

if yn.upper() == "N":
    exit

print("You want to manually specify the path? (y/N)")

if yn.upper() == "Y":
    print("You must put an absolute path.")
    TerminalPath = input(">> ")
else:
    TerminalPath = f'{os.path.expanduser("~")}{os.sep}PyTerm'

print("Now we're going to install some Python libraries.")

instalar_librerias(["python-cfonts"])

filedict = {
    'app.py':"""
    
app
    
    """,
    'Module_A.py':"""

a
    
    """,
    'Module_B.py':"""

b
    
    """,
    'Module_C.py':"""

c
    
    """,
    'Module_D.py':"""

d
    
    """,
    
}

if not os.path.exists(TerminalPath):
    os.makedirs(TerminalPath)

for nombre_archivo, contenido in filedict.items():
    ruta_archivo = os.path.join(TerminalPath, nombre_archivo)
    with open(ruta_archivo, 'w') as archivo:
        archivo.write(contenido)
