#!/usr/bin/env python3
# function to rename files.
import os, sys
import hashlib


def hashfile(path, blocksize = 65536):
    '''read file and return its hasher 
       paramters:
           path -  this is actual name of the file
           blocksize = 65536 this is the long bate readed
    '''
    afile = open(path, 'rb')
    hasher = hashlib.md5()
    buf = afile.read(blocksize)
    while len(buf) > 0:
        hasher.update(buf)
        buf = afile.read(blocksize)
    afile.close()
    return hasher.hexdigest()

def renamefile(f):
    ext = ('.exe', '.dll', '.cmd','.lnk', '.json', '.EXE', '.DLL')
    pathtodir = os.path.dirname(f)
    if not f.endswith(ext):
        f_name, f_ext = os.path.splitext(f)
        print(f"f_name: {f_name} , f_ext {f_ext}")
        hash_name = hashfile(f)
        f_name_dst = os.path.join(pathtodir, hash_name + f_ext)
        print(f"f_name_dst: {f_name_dst}")
        if f != f_name_dst:
            try:
                print(f"rename: {f}")
                os.rename(f, f_name_dst)
            except Exception as e:
                print(f"Exception rename {f} to {f_name_dst}\n" + str(e.args))

def explorer(dirname):
    ext = ('.exe', '.dll', '.cmd','.lnk', '.json', '.EXE', '.DLL')
    if os.path.isdir(dirname): #si es un directorio
        # os.chdir(dir) # establecemos el directorio actual como corriente.
        listdir = os.listdir(dirname)
        print(listdir)
        for f in listdir: #recorrremos la lista
            f = os.path.join(dirname, f)
            if os.path.isdir(f): continue
            if os.path.islink(f): continue
            if os.path.isfile(f):
                if not f.endswith(ext):
                    f_name, f_ext = os.path.splitext(f)
                    print(f"f_name: {f_name} , f_ext {f_ext}")
                    hash_name = hashfile(f)
                    f_name_dst =os.path.join(dirname, hash_name + f_ext)
                    print(f"f_name_dst: {f_name_dst}")
                    if f != f_name_dst:
                        try:
                            print(f"rename: {f}")
                            os.rename(f, f_name_dst)
                        except Exception as e:
                            print(f"Exception rename {f} to {f_name_dst}\n" + str(e.args))
                    print('\n')


if __name__=='__main__':
    # currentdir = os.getcwd()
    if len(sys.argv)< 2:
        print('add path to directory')
        sys.exit(1)
    dirname = os.path.abspath(sys.argv[1])
    if os.path.isdir(dirname):
        print('dir:', dirname)
        res = input(f"quieres renombrar los archivos del directorio{dir} Yes/No: ")
        if res.upper() == 'Y':
            explorer(dirname)
    elif os.path.isfile(dirname):
        print('file:', dirname)
        res = input(f"quieres renombrar {dirname} Yes/No: ")
        if res.upper() == 'Y':
            # os.chdir(os.path.dirname(dir))
            renamefile(dirname)
            # os.chdir(currentdir)
    print(f"Current working directory: {os.getcwd()}")
