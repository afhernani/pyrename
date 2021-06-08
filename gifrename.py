# ! /usr/bin/env python3
# -*- using:UTF-8 -*-

import os, sys
import argparse

__autor__ = 'Hernani Aleman Ferraz'
__email__ = 'afhernani@gmail.com'
__apply__ = 'gifrename.py'
__version__ = 0.0


def changename(name):
    if '_thumbs_' in name:
        wn = name.split('_thumbs_')[0]
        newname = wn + '_nfx_.gif'
        return newname
    else:
        return " "

def renamefile(name):
    ext = ('.gif', '.GIF')
    if os.path.isfile(name):
        file = os.path.abspath(name)
        if file.endswith(ext):
            new_name = changename(file)
            if new_name == " ":
                print(f"don't rename {file}")
            if file != new_name and new_name != " ":
                try:
                    print(f"rename: {file} >> {new_name}")
                    os.rename(file, new_name)
                except Exception as e:
                    print(f"don't rename {file} to {new_name}")  

def renamefiles_dir(dir):
    ext = ('.gif', '.GIF')
    listdir = os.listdir(dirname)
    for f in listdir:
        if f.endswith(ext):
            file = os.path.join(dir, f)
            new_name = changename(file)
            if new_name == " ":
                print(f"don't rename {file}")
                continue
            if file != new_name:
                try:
                    print(f"rename: {file} >> {new_name}")
                    os.rename(file, new_name)
                except Exception as e:
                    print(f"don't rename {file} to {new_name}")  

def findDup(parentFolder):
    ext = ('.gif', '.GIF')
    for dirName, subdirs, fileList in os.walk(parentFolder):
        print('Scanning %s...' % os.path.abspath(dirName))
        if '.Thumbails' in dirName:
            continue
        if 'Thumbails' in dirName:
            poss = os.path.abspath(dirName)
            for filename in fileList:
                # Get the path to the file
                if filename.endswith(ext):
                    file = os.path.join(poss, filename)
                    newfile = changename(file)
                    print(file, newfile)
                    if newfile == ' ':
                        print(f"it not posible change name to {file}")
                        continue
                    try:
                        os.rename(file, newfile)
                    except FileExistsError as e:
                        print(str(e.args))
                # Calculate hash
            basedir = poss.split(os.sep)
            basedir[-1]='.Thumbails'
            # print(basedir)
            baseultimo = f"{os.sep}".join(basedir)
            # print(baseultimo)
            try:
                os.rename(poss, baseultimo)
                print(f"rename directory {poss} to\n {baseultimo}")
            except FileExistsError as e:
                print(f"don't rename {poss}")


if __name__ == '__main__':
    parse = argparse.ArgumentParser(prog='gifrename.py', 
                    description='Scan subdirecties for rename files types _thumbs_.gif to _nfx_.gif'
                    )
    parse.add_argument('-s', '--scan', type=str, help='scan subdirectorios Thumbails, rename files and renane dir to .Thumbails')
    parse.add_argument('-f', '--file', type=str, help='rename file _thumbs_.gif to _nfx_.gif')
    parse.add_argument('-d', '--dir', type=str, help='rename all files type gif on dir, fineshed to _nfx_.gif')
    parse.add_argument('--version', action='version', version='%(prog)s '+ str(__version__))
    args = parse.parse_args()

    if args.scan:
        findDup(args.scan)
    elif args.file:
        renamefile(args.file)
    elif args.dir:
        dirname = os.path.abspath(args.dir)
        if os.path.isdir(dirname):
            print('dir:', dirname)
            renamefiles_dir(dirname)
        else:
            print(f"{dirname} is not a directory")
    else:
        pass

