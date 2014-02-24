#!/usr/bin/python
# ardlib
# Arduino Library Installer by Sebastian Plamauer

import requests
import zipfile
import StringIO
import os
import shutil
import csv
import sys
import getopt
from os.path import expanduser
from libmng import Libmng



class library():

    #init
    def __init__(self):
        self.libmng = Libmng('repo')
        self.home = expanduser("~")
        self.repo = os.path.dirname(os.path.realpath(__file__))+'/repo.csv'
        self.libraries = self.home+'/sketchbook/libraries/'
        if os.path.isdir(self.libraries) == False:
            print self.libraries+' doesn\'t exist.'
            sys.exit()
        self.liblist = []


    #listlibs
    def listlibs(self, part):
        try:
            for name in self.libmng.getall(part): 
                print name
        except: print 'There is no liblist'
        return 'listlibs'
        
    

    #installlib
    def installlib(self, name):
         
        found = self.libmng.checklib(name,'')
        if found == False: 
            print 'The lib '+name+' is not in the repo.'
            return 
        url = self.libmng.getlib(name)
        try:
            if os.path.isdir(self.libraries+name) == False:
                req = requests.get(url)
                zipobj = zipfile.ZipFile(StringIO.StringIO(req.content))
                zipobj.extractall(self.libraries)
                dirname = zipobj.namelist()[0][:-1]
                os.rename(self.libraries+dirname,self.libraries+name)
                print 'Installed '+name
            else: print name+' is already installed.'
        except Exception as detail: 
            print 'There was an error:', detail


    #installall
    def installall(self):
        for name in self.libmng.getall(1):
            self.installlib(name)
        return 'installall'

    #deletelib
    def deletelib(self, name):
        found = self.libmng.checklib(name,'')
        if found == False: 
            print 'The lib '+name+' is not in the repo.'
            return
        url = self.libmng.getlib(name)
        try:
            if os.path.isdir(self.libraries+name) == False:
                print name+' is not installed.'
            else:
                shutil.rmtree(self.libraries+name)
                print name+' is deleted.'
        except Exception as detail: 
            print 'There was an error.', detail
        return 'deletelib'


def error():
    print '\n\tValid inputs are:\n\n\t\tardlib.py listlibs\n\t\tardlib.py install all\n\t\tardlib.py install <lib>\n\t\tardlib.py delete <lib>\n'
    sys.exit()


def main(argv):
	
    repo = library()
    try:
        command = argv[0]
    except:
        error()

    if len(argv) == 1:
        lib = ''
    elif len(argv) == 2:
        lib = argv[1]
    else: error()

    if command == '-h':
        error()
    elif command == 'listlibs':
        repo.listlibs(1)
        sys.exit()
    elif command == 'install' and lib == 'all':
        repo.installall()
        sys.exit()
    elif command == 'install':
        repo.installlib(lib)
        sys.exit()
    elif command == 'delete':
        repo.deletelib(lib)
        sys.exit()
    else:
        error()


if __name__ == '__main__':
	main(sys.argv[1:])
	
