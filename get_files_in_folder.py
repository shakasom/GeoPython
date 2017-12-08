# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 22:17:05 2017

@author: Shakur
"""




import os 

os.chdir('PATH')
folder = os.listdir()



def get_file_names(folder):
    """ This function prints the name of the files in a give folder and 
    the count of these files
    >>> get_file_names(folder)
        Files : [a.txt, b.csv]
        Counts: 2
    """
    count = 0
    file_names = []
    
    for files in folder:
        count += 1
        file_names.append(files)
        
    return file_names 

print("Files: %s " % (file_names))
print("Counts : %d " % (count))


def get_extensions(folder):
    """ The functions prints extensions of the files in a folder
    >>> get_extensions(folder)
        Extensions: [csv, txt]
    """
    files = get_file_names(folder)
    extensions = []
    for i in files:
        extensions.append(i.split(".")[1:])

    print("Extensions: %s " % extensions)
    
get_file_names(folder)
get_extensions(folder)     
    
    
    




