#!/usr/bin/env python3

import sys
import os
import argparse
import re

parser = argparse.ArgumentParser()

parser.add_argument("file", type=argparse.FileType("r"), nargs="*", default=sys.stdin)

arguments = parser.parse_args()

def sorting(text):
    list = []
    for line in text.split("\n"):
        #list.append(r"{}".format(line))
        list.append(repr(line))
    sorted_list = sorted(list)
    for line2 in sorted_list:
        sys.stdout.write(line2)
        sys.stdout.write("\n")

if arguments.file == sys.stdin:
    text = arguments.file.read()
    sorting(text)
else:
    for texts in arguments.file:
        text = texts.read()
        sorting(text)
        
