import os, platform, json

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
    def custome_print(lista):
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
                custome_print(os.listdir(ActiveDirectory))
                return
        if os.path.exists(path):
            custome_print(os.listdir(path))
        else:
            return {'error':'path not found'}
    else:
        custome_print(os.listdir(ActiveDirectory))
        return
    
def pwd(prompt_, ActiveDirectory):
    print(ActiveDirectory)
    
def exit_(a,b):
    exit()