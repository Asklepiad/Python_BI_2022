#!/usr/bin/env python
# coding: utf-8

import re
import matplotlib.pyplot as plt
import seaborn as sns


# Parsing of ftp

with open ("/home/asklepiad/Downloads/references.txt", "r") as references, open("/home/asklepiad/Downloads/ftps", "w") as ftps:
    refere = re.compile(r"\bftp.+?[\n\t;]")
    for line in references:
        ref = refere.findall(line)
        for strings in ref:
            ftps.write(strings.strip("\n\t;"))
            ftps.write("\n")


# Number from story

with open ("/home/asklepiad/Downloads/2430AD.txt", "r") as story:
    refere = re.compile(r"\D\d+?\.?\d+?\D")
    for line in story:
        ref = refere.findall(line)
        for number in ref:
            print(number.strip(","))


# A from story

with open ("/home/asklepiad/Downloads/2430AD.txt", "r") as story:
    refere = re.compile(r"\b[\w]*?[Aa].*?\b")
    for line in story:
        ref = refere.findall(line)
        for number in ref:
            print(number)
            counter += 1


# Not well worked !-finder

with open ("/home/asklepiad/Downloads/2430AD.txt", "r") as story:
    refere = re.compile(r"(\b[A-Z0-9].*?\!)[\s\'\"]")
    for line in story:
        ref = refere.findall(line)
        for number in ref:
            print(number)


# Переводчик с русского на кирпичный

def kirpich(string):
    pattern = re.compile(r"([аоуэиыеёяю])")
    substitution = r"\1к\1"
    return(pattern.sub(substitution, string))


# Barplot of word lengthes

with open ("/home/asklepiad/Downloads/2430AD.txt", "r") as story:
    pattern = re.compile(r"\b[\w]+?\b")
    length_dictionary = {}
    for line in story:
        ref = pattern.findall(line)
        for word in ref:
            if word not in length_dictionary:
                length_dictionary[word.lower()] = len(word)
    barplot_dictionary = {}
    percent = round(100 / len(length_dictionary), 5)
    for i in range(1, max(length_dictionary.values())+1):
        for value in length_dictionary.values():
            if value == i:
                if value in barplot_dictionary:
                    barplot_dictionary[i] += percent
                else:
                    barplot_dictionary[i] = percent
    plt.bar(barplot_dictionary.keys(), barplot_dictionary.values())
    plt.xlabel("Length of words")
    plt.ylabel("Frequency")


# Function for extracting sentence with exact lehgth

def sentence_length(text, number):
    string = r"\b[A-ZА-Я][\w]*?\b[\s]"
    str_repeat = r"\b[\w]+?\b[\s]"
    str_end = r"\b[\w]+?[\.\!\?]"
    for i in range(number-2):
        string += str_repeat
    string += str_end
    pattern = re.compile(string)
    output = []
    for word in pattern.findall(text):
        output.append(tuple(word.split()))
    print(output)

