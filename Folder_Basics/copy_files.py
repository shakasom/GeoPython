# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 22:30:38 2017

@author: Shakur
"""

import shutil, os


def copy_files(src, dest):
    """
    Copy files from one folder to another
    >>> copy_files(src, dest)
        copying {filename} to {destination}
    """ 
    os.chdir(src)
    files = os.listdir()
    for filename in files:
        shutil.copy(filename, dest)
        print ("Copying {} to {} ".format(filename, dest))
src = 'path//to/source'
dest = 'path//to/destination'
copy_files(src, dest)

