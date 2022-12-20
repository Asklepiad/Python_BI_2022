#!/usr/bin/env python3

import sys
import os
import argparse
import re

parser = argparse.ArgumentParser()

parser.add_argument("-l", action = "store_true")
parser.add_argument("-w", action = "store_true")
parser.add_argument("-c", action = "store_true")
parser.add_argument("file", type=argparse.FileType("r"), nargs="*", default=sys.stdin)

arguments = parser.parse_args()

if arguments.l == False & arguments.w == False & arguments.c == False:
    arguments.l = True
    arguments.w = True
    arguments.c = True

def counting(text):
    word = re.compile(r"[\^\s][!-~]+?[\s\$]")
    line = re.compile(r"\n")

    if arguments.l == True:
        sys.stdout.write(" ")
        list_l = re.findall(line, text)
        sys.stdout.write(str(len(list_l)))
    if arguments.w == True:
        sys.stdout.write(" ")
        sys.stdout.write(str(len(text.split())))
    if arguments.c == True:
        sys.stdout.write(" ")
        sys.stdout.write(str(len(text)))
    
if arguments.file == sys.stdin:
    text = arguments.file.read()
    counting(text)
    sys.stdout.write("\n")
else:
    for texts in arguments.file:
        text = texts.read()
        counting(text)
        sys.stdout.write("\n")
