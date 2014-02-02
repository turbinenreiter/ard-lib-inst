Arduino Library Installer
=========================

This script helps installing Arduino Libraries on Linux-based operating systems. The repo-file lists libraries and URLs to the .zip-files.  
You have the change the variable 'self.libraries' in the .py-script to the path to your libraries directory.  
A list of more libraries is available under http://playground.arduino.cc/Main/LibraryList. Feel free to commit more libraries to the repo file! There are a lot out there and help is appreciated.

Usage:
------
    python ardlib.py listlibs               #list of available libraries
    python ardlib.py install all            #install all available libraries
    python ardlib.py install <lib>          #install <lib>

