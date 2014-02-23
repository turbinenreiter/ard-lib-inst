# Author: Schaden Philipp
#
# Description:
# A class used to manage the repo.csv Librarie and its entries
# Functions:
#   *add library
#   *delete library
#   *check for multiple entries
#   *get all entries

#import library
import os
import csv

class Libmng:
    
    def __init__(self,libname):
        self.libs =[]
        if libname != "":
            self.file = libname+'.csv'
        #    with open(libname+'.csv',"a") as repo
        else:
            self.file = 'repo.cvs'
        #    with open("repo.csv","a") as repo
        

    # addlib adds a library with name to the csv file if it's source 
    # is not already there
    def addlib(self, name, source, info):
        if not self.checklib(name,source):
            with open(self.file,"a") as repo:
                repo.write(name+','+source+','+info+'\n')
            repo.close()
        else:
            print 'Entry already exists'
               
    # delllib deletes the library with name from the csv file
    def dellib(self, name):
        open('new.csv','a').close()
        with open(self.file,'rb') as repo:       
            writer = csv.writer(open('new.csv','w'))
            for row in csv.reader(repo):
                if not row[0] == name:
                    writer.writerow(row)
        repo.close()
        
        os.remove(self.file)
        os.rename('new.csv', self.file)
              
    
    # getlib is used to get the source url from an entry with the name 
    # from the csv file
    def getlib(self, name):
        with open(self.file, 'rb')as repo:
            for row in csv.reader(repo):
                if row[0] == name:
                    return str(row[1])
        
        
    # returns True if the name or the source is found in the repo.csv file
    # and False if not 
    def checklib(self, name, source):
        with open(self.file,'rb') as repo:
            for row in csv.reader(repo):
                if row[0] == name or row[1]==source:
                    return True
            
        return False
        
    # returns an array of the first (part = 1) the second (part = 2) or 
    # both (part = 0) columns from the csv file
    def getall(self,part):
        with open(self.file,'rb') as repo:
            for row in csv.reader(repo):
                if part == 0:
                    self.libs.append(row)
                else:
                    self.libs.append(row[part-1])
                
        return self.libs
        
    
