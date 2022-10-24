# Python_BI_2022
Repository for bioinformatics institute

## "NucAUt" - Nucleic acid utility


### Fast description

This is the utility for performing some basic manipulations with nucleic acids. 


### About commands

You can input one of five commands: exit, transcribe, reverse, complement and reverse complement.


![Entering commands](/hw_2/1print.png)

After first one programm ends.

If you will choose "transcribe" command the utility yields RNA product for DNA template or vice versa. If user's NA has uracil, utilite does reverse trancription. If user's NA has thymine, utility does usual trancription. If it has both uracil and thymine error message will appear. If it has neither uracil nor thymine, the user needs to choose the type of NA acid.

If you will choose "reverse" command the utility yields an input sequence from its end to start.

If you will choose "complement" command the utility yields nucleic acid complementary to user's input.

"Reverse complement" command's output is surprising: it combines "reverse" and "complement" functions.

If user enter uncorrect command utility takes a message about it. After five unsuccessful attempts utility stops.


![Incorrect command](/hw_2/2sleep.png)


### About nucleic acid input

![Entering NA](/hw_2/3Nucleotide.png)

After entering command user need to print or paste nucleic acid sequence. It must contain only symbols 'A', 'C', 'G', 'T', 'U', 'R', 'Y', 'N' in uppercase or lowercase mode. If it contains some other symbols utility says about it.

![DNA or RNA, what is a quetion](/hw_2/4DR.png)

The other mistacable thing is mixing 'U' and 'T' in one aminoacid. If it appears utility sends a warning message to user.
If nucleic acid has neither 'U', nor 'T' "NucAUt" sends a warning message too. If the user prints 'yes' (or 'YES', or 'YeS' or something else) an acid will be processed as DNA. If user enters something different - the acid will be processed as RNA.

![The end](/hw_2/5exit.png)
