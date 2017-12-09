# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 23:09:07 2017

@author: Shakur
"""

import os

def remove_files(folder):
    files = os.listdir(os.chdir(folder))
    for filename in files:
        os.remove(filename)

folder = 'path//to//folder'
remove_files(folder)