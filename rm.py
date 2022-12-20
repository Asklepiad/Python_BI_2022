#!/usr/bin/env python3

import sys
import os
import argparse
import shutil

parser = argparse.ArgumentParser()
parser.add_argument("path", type=str)
parser.add_argument("-r", action = "store_true")

arguments = parser.parse_args()
pathto = os.path.abspath(arguments.path)

if arguments.r == True:
    if os.path.isdir(pathto) == True:
        shutil.rmtree(pathto)
    else:
        print("It's not a directory.")
else:
    if os.path.isfile(pathto) == True:
        os.remove(pathto)
    else:
        print("It's not a file.")
