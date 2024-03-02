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
            
    # Terminal command execute
    def execute(self, prompt_):
        prompt_l = prompt_.split(" ")
        command = prompt_l[0]
        if command == "clear":
            os.system("printf '\033c'")
            return
        if command in self.commands:
            result = self.commands[command](prompt_l, self.ActiveDirectory)
        else:
            if command == "":
                print(a.paintText(f"{self.ActiveDirectory} ➽  ", color='yellow'))
                return
            else:
                print(a.paintText(f'Command "{command}" not found, type "help" for help', color='yellow'))
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
            command = input(a.paintText(f"{self.ActiveDirectory} ➢  "))
            self.execute(command)
            
            
if __name__ == '__main__':
    terminalClass()