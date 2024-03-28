import os, platform
import Module_A as a
from cfonts import render

class terminalClass():
    def __init__(self) -> None:
        self.IDLS()
        self.update()
    
    # Init Detect and Load System
    def IDLS(self):
        if a.isFirstTime:
            print(render('Welcome to PyTerminal', colors=['red', 'yellow'], align='center', line_height=3, font='chrome'))
        else:
            print(render('PyTerminal', colors=['red', 'yellow'], align='center', line_height=3, font='chrome'))
        self.ActiveDirectory = a.startDirectory()
        self.commands = a.dictCommands()
            
    # Terminal command execute|
    def execute(self, prompt_):
        Nl = prompt_.count("|") ; result_L = [] 
        if Nl < 1:
            promptU = [prompt_]
            Nl = 1
        else:
            promptU = prompt_.split("|")
        for i in range(0,Nl):
            prompt_l = promptU[i].split(" ")
            command = prompt_l[0].lower()
            if command == "clear":
                if os.name == 'nt':  # Windows
                    os.system('cls')
                else:  # Unix/Linux/Mac
                    os.system('clear')
                return
            if command in self.commands:
                try:
                    if prompt_l.count("[arg]") > 1:
                        result = self.commands[command](a.replace_items(prompt_l, result_L[i].split(" ")), self.ActiveDirectory)
                    else:
                        result = self.commands[command](prompt_l.replace("[arg]", result_L[i]), self.ActiveDirectory)
                except:
                    result = self.commands[command](prompt_l, self.ActiveDirectory)
                result_L.append(result)
            else:
                if command == "":
                    print(a.paintText(f"{self.ActiveDirectory} ➽  ", color='yellow'))
                    result_L.append("")
                    return
                else:
                    print(a.paintText(f'Command "{command}" not found, type "help" for help', color='yellow'))
                    result_L.append("")
                    return
            if result is not None:
                if 'error' in result:
                    print(a.paintText(f"Error : {result.get('error')}", color='red'))
                    return
                if 'ActiveDirectory' in result:
                    self.ActiveDirectory = result.get('ActiveDirectory')
    
    # Terminal process update
    def update(self):
        while(True):
            command = input(a.paintText(f"{self.ActiveDirectory} ➢")+"  ")
            self.execute(command)
            
            
if __name__ == '__main__':
    terminalClass()