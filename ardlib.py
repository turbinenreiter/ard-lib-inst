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


class library():

    #init
	def __init__(self):
		self.home = expanduser("~")
		self.repo = os.path.dirname(os.path.realpath(__file__))+'/repo.csv'
		self.libraries = self.home+'/sketchbook/libraries/'
		self.liblist = []

    #getliblist
	def getliblist(self):
		try:
			with open(self.repo, 'rb') as csvfile:
				reader = csv.reader(csvfile)
				for row in reader:
					self.liblist.append(row)
		except: print 'Couldn\'t get repo.'
		return 'getliblist'

    #listlibs
	def listlibs(self):
		try:
			for lib in self.liblist:
				print lib[0]
		except: print 'There is no liblist'
		return 'listlibs'

    #installlib
	def installlib(self, name):
		found = False
		for lib in self.liblist:
			if lib[0] == name:
				url = lib[1]
				found = True
				try:
					if os.path.isdir(self.libraries+name) == False:
						req = requests.get(url)
						zipobj = zipfile.ZipFile(StringIO.StringIO(req.content))
						zipobj.extractall(self.libraries)
						dirname = zipobj.namelist()[0][:-1]
						os.rename(self.libraries+dirname,self.libraries+name)
						print 'Installed '+name
					else: print name+' is already installed.'
				except: print 'There was an error.'
		if found == False: print 'The lib '+name+' is not in the repo.'
		return 'installlib'

    #installall
	def installall(self):
		for lib in self.liblist:
			self.installlib(lib[0])
		return 'installall'

    #deletelib
        def deletelib(self, name):
            found = False
            for lib in self.liblist:
                if lib[0] == name:
                    url = lib[1]
                    found = True
                    try:
                        if os.path.isdir(self.libraries+name) == False:
                            print name+' is not installed.'
                        else:
                            shutil.rmtree(self.libraries+name)
                            print name+' is deleted.'
                    except: print 'There was an error.'
            if found == False: print 'The lib '+name+' is not in the repo.'
            return 'deletelib'


def error():
    print '\n\tValid inputs are:\n\n\t\tardlib.py listlibs\n\t\tardlib.py install all\n\t\tardlib.py install <lib>\n\t\tardlib.py delete <lib>\n'
    sys.exit()


def main(argv):
	
    repo = library()
    repo.getliblist()
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
        repo.listlibs()
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
	
