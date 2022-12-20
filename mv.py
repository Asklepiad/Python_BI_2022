#!/usr/bin/env python3

import sys
import os
import argparse
import shutil

parser = argparse.ArgumentParser()

parser.add_argument("path_from", type=str)
parser.add_argument("path_to", type=str)

arguments = parser.parse_args()

pathfrom = os.path.abspath(arguments.path_from)
pathto = os.path.abspath(arguments.path_to)

if os.path.isdir(pathfrom) == True:
    if os.path.isdir(pathto):
        shutil.move(pathfrom, os.path.join(pathto, os.path.basename(pathfrom)))
elif os.path.isfile(pathfrom) == True:
    if os.path.isdir(pathto) == False:
        os.rename(pathfrom, pathto)
    else:
#        print(os.path.join(pathto, os.path.basename(pathfrom)))
        #print(os.path.basename(pathfrom))
        os.rename(pathfrom, os.path.join(pathto, os.path.basename(pathfrom)))
