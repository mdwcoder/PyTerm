import os

def normalFile(actualpath : str, filepath : str):
    if os.path.isfile(filepath):
        return {'value':filepath}
    else: 
        if actualpath[-1] == os.sep:
            actualpathA = actualpath[:-1]
        else:
            actualpathA = actualpath
        if filepath[0] == os.sep:
            filepathA = filepath[1:]
        else:
            filepathA = filepath
        testpath = f"{actualpathA}{os.sep}{filepathA}"
        if os.path.isfile(testpath):
            return {'value':testpath}
        else:
            return {'error':f'{filepath} does not exist.'}
    
def normalDir(actualpath : str, dirpath : str):
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
    