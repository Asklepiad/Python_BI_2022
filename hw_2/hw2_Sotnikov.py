#!/usr/bin/env python
# coding: utf-8


# Nucleotide list for checking correctness of user's input. Vocabularies for commands.

nucl_data = ['A', 'G', 'T', 'C', 'U', 'R', 'Y', 'N']
dna2dna = {'A':'T', 'G':'C', 'T':'A', 'C':'G', 'a':'t', 'g':'c', 't':'a', 'c':'g', 'R':'Y', 'r':'y','Y':'R','y':'r','N':'N', 'n':'n'}
dna2rna = {'A':'U', 'G':'C', 'T':'A', 'C':'G', 'a':'u', 'g':'c', 't':'a', 'c':'g', 'R':'Y', 'r':'y','Y':'R','y':'r','N':'N', 'n':'n'}
rna2dna = {'A':'T', 'G':'C', 'U':'A', 'C':'G', 'a':'t', 'g':'c', 'u':'a', 'c':'g', 'R':'Y', 'r':'y','Y':'R','y':'r','N':'N', 'n':'n'}
rna2rna = {'A':'U', 'G':'C', 'U':'A', 'C':'G', 'a':'u', 'g':'c', 'u':'a', 'c':'g', 'R':'Y', 'r':'y','Y':'R','y':'r','N':'N', 'n':'n'}
command_flag = 5


# nucl_input checking nucleotide input's correctness and type of nucleic acid.

def nucl_input():
    nucl_flag = True
    # If nucleotide sequence is correct in common case flag stops 'while' cycle. 
    # Else it repeats cycle.
    # After five mistakes cycle stops.
    while nucl_flag:
        nucl_acid = input("Paste nucleotide sequence: ")
        nucl_point = len(nucl_acid)
        for nucleotide in nucl_acid.upper():
            if nucleotide in nucl_data:
                nucl_point -= 1
                if nucl_point == 0:    
                    if 'U' in nucl_acid.upper() and 'T' in nucl_acid.upper():
                        print("Your sequence must contain either 'U' or 'T'" "\n"
                                 "Paste correct sequence again, please: ")
                        continue
                    else:
                        nucl_flag = False
                        if 'U' in nucl_acid.upper():
                            nucl_type = "R"
                        elif 'T' in nucl_acid.upper():
                            nucl_type = "D"
                        else:
                            na_type_answer = input("If your nucleotide sequence is DNA print 'yes', else print something else: ")
                            if na_type_answer.lower() == "yes":
                                nucl_type = "D"
                            else:
                                nucl_type = "R"
                        break
                continue
            else:
                print("You are print a non-nucleotide symbol." "\n" 
                        "Please, use latin letters 'A', 'C', 'G', 'T', 'U', 'R', 'Y', 'N' in uppercase or lowercase mode." "\n" 
                        "Try again.")
                break
    
    return(nucl_acid, nucl_type)


# Commands

while command_flag:
    command = input("If you want to exit print 'exit'." "\n"
                    "If you want to take trancribed RNA sequence print 'transcribe'." "\n"
                    "If you want to take reverse nucleotide sequence print 'reverse'." "\n"
                    "If you want to take complementary nucleotide sequence print 'complement'." "\n"
                    "If you want to print take reverse complementary nucleotide sequence 'reverse complement'." "\n"
                    "Print your command here: ")
    
    if command.lower() == "exit":
        command_flag = 5
        print("It was a good hunt!")
        break
        
    elif command.lower() == "transcribe":
        command_flag = 5
        nucl_info = nucl_input()
        nucl_acid = nucl_info[0]
        nucl_type = nucl_info[1]
        if nucl_type == "R":
            print("Result is", end=" ")
            for nucleotide in nucl_acid:
                print(rna2dna[nucleotide], end="")
        elif nucl_type == "D":
            print("Result is", end=" ")
            for nucleotide in nucl_acid:
                print(dna2rna[nucleotide], end="")
        print()
        
    elif command.lower() == "reverse":
        command_flag = 5
        print("Result is", end=" ")
        nucl_acid = nucl_input()[0]
        print(nucl_acid[::-1])
        print()
        
    elif command.lower() == "complement":
        command_flag = 5
        nucl_info = nucl_input()
        nucl_acid = nucl_info[0]
        nucl_type = nucl_info[1]
        if nucl_type == "R":
            print("Result is", end=" ")
            for nucleotide in nucl_acid:
                print(rna2rna[nucleotide], end="")
        elif nucl_type == "D":
            print("Result is", end=" ")
            for nucleotide in nucl_acid:
                print(dna2dna[nucleotide], end="")
        print()
        
    elif command.lower() == "reverse complement":
        command_flag = 5
        nucl_info = nucl_input()
        nucl_acid = nucl_info[0]
        nucl_type = nucl_info[1]
        if nucl_type == "R":
            print("Result is", end=" ")
            for nucleotide in nucl_acid[::-1]:
                print(rna2rna[nucleotide], end="")
        elif nucl_type == "D":
            print("Result is", end=" ")
            for nucleotide in nucl_acid[::-1]:
                print(dna2dna[nucleotide], end="")
        print()
        
    else:
        command_flag -= 1
        if command_flag > 0:
            print("Command doesn't exists." "\n"
                    "Try again." "\n"
                    "You have left", command_flag, "attempts")
            continue
        else:
            print("I'm sorry, you have no more atempts." "\n"
                    "You need to start again.")
            continue

