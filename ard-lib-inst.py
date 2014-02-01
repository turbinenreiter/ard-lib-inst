# ard-lib-inst
# Arduino Library Installer by Sebastian Plamauer

import requests
import zipfile
import StringIO
import os
import csv

# reads the list of repos
def getliblist():
    try:
        repo = '/home/plam/projects/ard-lib-inst/repo.csv'
        libs = []
        with open(repo, 'rb') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                libs.append(row)
        print '\tGot repo.\n'
        return libs
    except:
        print '\tCouldn\'t get repo.\n'
        return False

# downloads libs and unpacks them to the lib-folder
def getlib(name, url):
    try:
        if os.path.isdir('/home/plam/sketchbook/libraries/'+name) == False:
            req = requests.get(url)
            zipobj = zipfile.ZipFile(StringIO.StringIO(req.content))
            zipobj.extractall('/home/plam/sketchbook/libraries')
            dirname = zipobj.namelist()[0][:-1]
            os.rename('/home/plam/sketchbook/libraries/'+dirname,'/home/plam/sketchbook/libraries/'+name)
            print '\tInstalled '+name
        else:
            print '\t'+name+' is already installed.'
        return True
    except:
        print '\tThere was an error.'
        return False 

def init():

    print '\n\t\tarduino-library-installer\n'
    print '\t\'all\' to install libs in the repo'
    print '\t\'list\' for a list of libs'
    print '\t\'name\' to install the lib \'name\''
    print '\t\'exit\' to exit\n'
    global liblist
    liblist = getliblist()

def UI():

    global liblist

    if liblist == False:
        command = 'exit'
    else:

        command = raw_input('\tcommand: ')

        if command == 'all':
            for lib in liblist:
                getlib(lib[0], lib[1])
        elif command == 'list':
            for lib in liblist:
                print '\t'+lib[0]
        elif command == 'exit':
                print '\n\tExiting ard-lib-inst\n'
        else:
            name = command
            found = False
            for lib in liblist:
                if lib[0] == name:
                    getlib(lib[0], lib[1])
                    found = True
            if found == False:
                print '\tThe lib '+name+' is not in the repo.'

    return command

def main():
    init()
    command = ''
    while command != 'exit':
        command = UI()

if __name__ == '__main__':
    main()
