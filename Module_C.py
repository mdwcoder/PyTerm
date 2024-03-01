
def help_(prompt_, ActiveDirectory):
    help_dict = {
        'ls':"""
        
             """,
        'cd':"""
        
             """,
        'mkdir':"""
        
             """ ,  
        'rm':"""
        
             """,
        'pwd':"""
        
             """,
        'exit':"""
        
             """,
    }
    search = prompt_[1]
    if search in help_dict:
        print(help_dict.get(search))