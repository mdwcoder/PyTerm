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
        commands = self.commands
        result_L = []
        
        if "|" not in prompt_:
            promptU = [prompt_]
        else:
            promptU = prompt_.split("|")
        
        for prompt_part in promptU:
            prompt_l = prompt_part.split()
            command = prompt_l[0].lower()
            
            if command == "clear":
                os.system('cls' if os.name == 'nt' else 'clear')
                return

            if command in commands:
                try:
                    arg_index = prompt_l.index("[arg]") if "[arg]" in prompt_l else -1
                    if arg_index > 0:
                        result = commands[command](a.replace_items(prompt_l, result_L[-1].split()), self.ActiveDirectory)
                    else:
                        result = commands[command](' '.join(prompt_l).replace("[arg]", result_L[-1]), self.ActiveDirectory)
                except Exception as e:
                    result = commands[command](prompt_l, self.ActiveDirectory)
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
            if self.ActiveDirectory.count(f"{os.sep}.") > 0:
                self.ActiveDirectory.replace(f"{os.sep}.", "")
            command = input(a.paintText(f"{self.ActiveDirectory} ➢")+"  ")
            self.execute(command)
            
            
if __name__ == '__main__':
    terminalClass()