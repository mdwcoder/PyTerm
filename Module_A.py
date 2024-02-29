import os, platform, json
import Module_B as b
from cfonts import render

userPath = os.path.expanduser("~")
configPath = f'{userPath}{os.sep}PyTerm{os.sep}config.json'

def FirstSave(dicData):
    if not os.path.exists(configPath):
        os.makedirs(configPath)
    with open(configPath, 'w') as archivo:
        json.dump(configPath, archivo)

def startDirectory() -> str:
    try:
        return os.getcwd()
    except FileNotFoundError:
        return os.path.expanduser("~")    
    
def dictCommands() -> dict:
    return {
        'cd':b.cd,
        'pwd':b.pwd,
        'ls':b.ls,
        'exit':b.exit_,
    }

def paintText(value):
    return render(str(value), colors=['white', 'grey'], font='console')

def isFirstTime() -> bool:
    return not os.path.exists(configPath)