#!/usr/bin/env python
# coding: utf-8


# Function for counting GC-percent. Returns "True" if GC-content is in given interval, returns "False" otherwise.

def gc_p(str2, gc_bounds):
    gc_count = 0
    for nucleotide in str2:
        if nucleotide == "G" or nucleotide == "C":
            gc_count += 1
    gc_percent = (gc_count/len(str2))*100
    
    if type(gc_bounds) == int:
        if gc_percent <= gc_bounds:
            return True
        else:
            return False
    else:
        if (gc_percent <= gc_bounds[1]) and (gc_percent >= gc_bounds[0]):
            return True
        else:
            return False

        
# Function for counting length of sequence. Returns "True" if length is in given interval, returns "False" otherwise.

def len_s(str2, length_bounds):
    if type(length_bounds) == int:
        if len(str2) <= length_bounds:
            return True
        else:
            return False
    else:
        if len(str2) <= length_bounds[1] and len(str2) >= length_bounds[0]:
            return True
        else:
            return False

        
# Function for counting quality threshold. Returns "True" if qt greater or equal then given number, returns "False" otherwise.

def qt(str4, quality_threshold):
    sum = 0
    for qual in str4:
        sum += (ord(qual) - 33)
        qual_mean = sum/len(str4)
    if qual_mean >= quality_threshold:
        return True
    else:
        return False


# Writing four fastq lines in one of the files

def filtrate(str1, str2, str3, str4, file_output, file_error, gc_bounds, length_bounds, quality_threshold, save_filtered = False):
    if gc_p(str2, gc_bounds) and len_s(str2, length_bounds) and qt(str4, quality_threshold):
        file_output.write(str1)
        file_output.write(str2)
        file_output.write(str3)
        file_output.write(str4)
    else:
        if save_filtered == True:
            file_error.write(str1)
            file_error.write(str2)
            file_error.write(str3)
            file_error.write(str4)
                   
                
# Taking every four lines of fastq

def master(file_input, file_output, gc_bounds, length_bounds, quality_threshold, save_filtered, file_error=None):
    count = 0
    for line in file_input:
        count+=1
        if count % 4 == 1:
            string1 = line
        elif count % 4 == 2:
            string2 = line
        elif count % 4 == 3:
            string3 = line
        elif count % 4 == 0:
            string4 = line

            filtrate(string1, string2, string3, string4, file_output, file_error, gc_bounds, length_bounds, quality_threshold, save_filtered)
            
            
# Main function: inputting values and taking them. Variables are:
# File path
# Output file path
# Needed gc-content: tuple(x,y) or higher bound - x
# Needed length: tuple(x,y) or higher bound - x
# Lower bound of quality of sequence
# Flag if it need to save unfiltered data in other file

def main(input_fastq, 
         output_file_prefix, 
         gc_bounds = (0,100), 
         length_bounds = (0, 2**32), 
         quality_threshold = 0, 
         save_filtered = False):
    
    
# Choosing of branch depends on save_filtered

    if save_filtered == False:
        with open(input_fastq, "r+") as file_input, open(output_file_prefix + "_passed.fastq", "w") as file_output:
            master(file_input, file_output, gc_bounds, length_bounds, quality_threshold, save_filtered = False)
    else:
        with open(input_fastq, "r+") as file_input, open(output_file_prefix+"_passed.fastq", "w") as file_output, open(output_file_prefix+"_failed.fastq", "w") as file_error:
            master(file_input, file_output, gc_bounds, length_bounds, quality_threshold, file_error = file_error, save_filtered = True)



