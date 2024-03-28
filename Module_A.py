
import os, platform, json, subprocess, sys
import Module_B as b
import Module_C as c
from cfonts import render

userPath = os.path.expanduser("~")
configPath = f'{userPath}{os.sep}PyTerm{os.sep}config.json'
    
def admin_gestor(a, b):
    def reiniciar_con_permisos_admin():
        if os.name == 'posix':  # unix
            if os.getuid() == 0: 
                os.execl(sys.executable, sys.executable, *sys.argv)
            else:  
                {'error':'You already are an admin'}
        elif os.name == 'nt':  # Windows
            import ctypes
            shell32 = ctypes.windll.shell32
            if shell32.IsUserAnAdmin() == 0: 
                shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
                sys.exit(0)
            else: 
                {'error':'You already are an admin'}

def user_gestor(prompt_, ActiveDirectory):
    os.execl(sys.executable, sys.executable, *sys.argv)

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
        'rm':b.rm,
        'cat':b.cat,
        'mkdir':b.mkdir,
        'grep':b.grep,
        'help':c.help_,
        'admin': admin_gestor,
        'restart':user_gestor,
        'navigate':b.navigate,
        'exit':b.exit_,
    }

def paintText(value, color='green',align='left'):
    return render(str(value), colors=[color, 'white'], font='console', align=align)[:-2]

def isFirstTime() -> bool:
    if not os.path.exists(configPath):
        FirstSave("")
    return not os.path.exists(configPath)

def replace_items(base_list, replace_list):
    for i in range(len(replace_list)):
        if replace_list[i] != "[arg]":
            base_list[i] = replace_list[i]
    return base_list
