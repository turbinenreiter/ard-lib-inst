Arduino Library Installer
=========================

This script helps installing Arduino Libraries on Linux-based operating systems. The repo-file lists libraries and URLs to the .zip-files.  
You have to change the variable 'self.libraries' in the .py-script to the path to your libraries directory.  
A list of more libraries is available under http://playground.arduino.cc/Main/LibraryList. Feel free to commit more libraries to the repo file! There are a lot out there and help is appreciated.

Usage:
------

Type the commands in the terminal. Don't use sudo, it will mess up the ownership of the files.  

    python ardlib.py listlibs               #lists all available libraries
    python ardlib.py install all            #installs all available libraries
    python ardlib.py install <lib>          #installs <lib>
    python ardlib.py delete <lib>           #deletes <lib>

Contributing to the repo-file:
------------------------------

Add links to libraries to the repo file in the following form:

    Name,URL-to-zip-file,URL-to-project-home
