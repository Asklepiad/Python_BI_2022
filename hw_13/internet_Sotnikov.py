#!/usr/bin/env python
# coding: utf-8

import requests
import re
import os
from dataclasses import dataclass

@dataclass
class GenscanOutput:
    status: str
    cds_list: list
    intron_list: list
    exon_list: list
        
    def __repr__(self):
        nl = f"\n"
        return f"Response status: {self.status}\n\nCds_list: {self.cds_list}\n\nIntron_list (number, start, end): {self.intron_list}\n\nExon_list (number, strans, start, end): {self.exon_list}"

    
def run_genscan(sequence=None, sequence_file=None, organism="Vertebrate", exon_cutoff=1.00, sequence_name=""):
    data = {"-p": "Predicted CDS and peptides", "-o": organism, "-e": exon_cutoff, "-n": sequence_name}
    url = "http://hollywood.mit.edu/cgi-bin/genscanw_py.cgi"
    
    
    if sequence is None and sequence_file is not None:
        
        with open(sequence_file, "r") as dna_seq:
            dna_strings = dna_seq.readlines()    
        number, lim = 0, len(dna_strings)
        while number < lim:
            string = dna_strings[number]
            if string.startswith(">"):
                dna_strings.remove(string)
                lim = len(dna_strings)
            else:
                number += 1
        
        data["-u"] = "".join(dna_strings)
        response = requests.post(url, data=data)
        
    elif sequence is not None and sequence_file is None:
        data["-s"] = sequence
        response = requests.post(url, data=data)
        
    elif sequence is not None and sequence_file is not None:
        raise Warning("You have passed both sequence and sequence_file arguments. \n\
        Pass only on of these arguments, please.")

    elif sequence is None and sequence_file is None:
        raise ValueError("You can't post both sequence and sequence_file as None. You need to put data into one of them")
    
    # CDSs list creating
    pattern_cds = re.compile(r"GENSCAN_predicted_peptide.+?(\n\n[A-Z\n]+)")
    cdss = re.findall(pattern_cds, response.text)
    if len(cdss) == 0:
        print("There are no any exons.\n\
        Your responce may content non-nucleotide letters, be too small or have incorrect attributes.")
        return GenscanOutput(status=status,
                        cds_list=[],
                        intron_list=[],
                        exon_list=[])
    cds_list = cdss[0].split()[:-1]
    
    # Exons list creating
    pattern_exon1 = re.compile(r"\s([\d\.]+?)\sInit ([+-])\s+?([\d]+)\s+?([\d]+)")
    pattern_exon2 = re.compile(r"\s([\d+\.\d+]+?)\sIntr ([+-])\s+?([\d]+)\s+?([\d]+)")
    pattern_exon3 = re.compile(r"\s([\d\.]+?)\sTerm ([+-])\s+?([\d]+)\s+?([\d]+)")
    init, inter, term = re.findall(pattern_exon1, response.text), re.findall(pattern_exon2, response.text), re.findall(pattern_exon3, response.text)
    exon_list = inter
    exon_list += init
    exon_list += term
    
    # Introns finding and passing to the list
    in_st, in_fin, intron_list = 1, None, []
    for number in range(len(exon_list)):
        curr_exon = exon_list[number]
        if curr_exon[1] == "+":
            in_fin = int(curr_exon[2]) - 1
            intron_list.append((number + 1, in_st, in_fin))
            in_st = int(curr_exon[3]) + 1
        elif curr_exon[1] == "-":
            in_fin = int(curr_exon[3]) - 1
            intron_list.append((number + 1, in_st, in_fin))
            in_st = int(curr_exon[2]) + 1
    
    # Status writng
    status = response.status_code

    
    return GenscanOutput(status=status,
                        cds_list=cds_list,
                        intron_list=intron_list,
                        exon_list=exon_list)
