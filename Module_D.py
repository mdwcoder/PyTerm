import os

def normalDir(actualpath : str, dirpath : str):
    if dirpath == "..":
        return {'value':os.path.split(actualpath)[0]}
    elif dirpath == ".":
        return {'value':actualpath}
    if os.path.exists(dirpath):
        if os.path.isfile(dirpath):
            return {'error':f'{dirpath} is a file.'}
        return {'value':dirpath}
    else: 
        if actualpath[-1] == os.sep:
            actualpathA = actualpath[:-1]
        else:
            actualpathA = actualpath
        if dirpath[0] == os.sep:
            dirpathA = dirpath[1:]
        else:
            dirpathA = dirpath
        testpath = f"{actualpathA}{os.sep}{dirpathA}"
        if os.path.exists(testpath):
            if os.path.isfile(testpath):
                return {'error':f'{dirpath} is a file.'}
            return {'value':testpath}
        else:
            return {'error':f'{dirpath} does not exist.'}
    
def normalFile(actualpath: str, filepath: str):
    # Obtener el directorio normalizado del archivo
    result = normalDir(actualpath, os.path.dirname(filepath))
    if 'value' in result:
        # Si se encuentra el directorio, devolver la ruta completa del archivo
        return {'value': os.path.join(result['value'], os.path.basename(filepath))}
    else:
        # Si hay un error al normalizar el directorio, devolver el mismo error
        return {'error': result['error']}

    
