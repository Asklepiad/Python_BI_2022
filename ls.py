#!/usr/bin/env python3
import sys
import os
import argparse
import shutil

parser = argparse.ArgumentParser()
parser.add_argument("path", type=str, nargs="*", default=str(os.getcwd()))
parser.add_argument("-a", action = "store_true")

arguments = parser.parse_args()


def ls_time(pathto):
    if arguments.a != True:
        for line in os.listdir(pathto):
            if not line.startswith("."):
                sys.stdout.write(line)
                sys.stdout.write("\n")
        sys.stdout.write("\n")
    else:
        sys.stdout.write(".")
        sys.stdout.write("\n")
        sys.stdout.write("..")
        sys.stdout.write("\n")
        for line in os.listdir(pathto):
            sys.stdout.write(line)
            sys.stdout.write("\n")
        sys.stdout.write("\n")

if arguments.path == os.getcwd():
    pathto = os.path.abspath(arguments.path)
    ls_time(pathto)
else:
    for pathto in arguments.path:
        pathto = os.path.abspath(pathto)
        ls_time(pathto)
