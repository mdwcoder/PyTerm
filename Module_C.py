import shutil
import Module_A as a

ancho_terminal = shutil.get_terminal_size().columns
separador = "_" * ancho_terminal


def help_(prompt_, ActiveDirectory):
     help_dict = {
        'ls':f"""
               {separador}
               {a.paintText("LS HELP", 'yellow', 'center')}
               {separador}
               Type "ls" for list your files and directories in you Active Directory.
               If you put a path after "ls" list files and directories there.
               Arguments 
               **Coming soon
             """,
        'cd':f"""
               {separador}
x               {a.paintText("CD HELP", 'yellow', 'center')}
               {separador}
               Type "cd <path/directory>" to go to one directory.
               If you put only "cd" you go to user path.         
               Arguments 
               **Coming soon
             """,
        'mkdir':f"""
               {separador}
               {a.paintText("MKDIR HELP", 'yellow', 'center')}
               {separador}
               Type "mkdir <path/directory>" to make an new/s directory/ies.
               Arguments 
               **Coming soon
             """ ,  
        'rm':f"""
               {separador}
               {a.paintText("RM HELP", 'yellow', 'center')}
               {separador}
               Type "rm <file/directory> to remove that.
               Arguments 
               **Coming soon
             """,
        'pwd':f"""
               {separador}
               {a.paintText("PWD HELP", 'yellow', 'center')}
               {separador}
               PWD return the active directory.
               Arguments 
               **Coming soon
             """,
        'admin':f"""
               {separador}
               ADMIN HELP
               {separador}
               Type "admin" to change the permissions to admin. 
        """,
        'restart':f"""
               {separador}
               RESTAR HELP
               {separador}
               Type "restar" to shutdown and power on pyterminal.
               Is for reset the permissions or when you see some errors.
        """,
        'exit':f"""
               {separador}
               {a.paintText("EXIT HELP", 'yellow', 'center')}
               {separador}
               Type "exit" to close PyTerminal.
             """,
     }
     if len(prompt_) < 2:
         for clave in help_dict:
          print(help_dict[clave])
     else:
          search = prompt_[1]
          if search in help_dict:
               print(help_dict.get(search))