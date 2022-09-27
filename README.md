# Python_BI_2022
Repository for bioinformatics institute

## "NucAUt" - Nucleic acid utility


### Fast description

This is the utility for performing some basic manipulations with nucleic acids. 


### About commands

You can input one of five command: exit, transcribe, reverse, complement and reverse complement.

After first one programm ends.

If you will choose "transcribe" command the utility yields RNA product for DNA template or vice versa. If user's NA has uracil, utilite does reverse trancription. If user's NA has thymin, utilite does usual trancription. If it has both uracil and thymin error message will appear. If it has neither uracil nor thymin, user need to choose type of NA acid.

If you will choose "reverse" command the utility yields input sequence from its end to start.

If you will choose "complement" command the utility yields nucleic acid complementary to user's input.

"Reverse complement" command's output is surprising: it combines "reverse" and "complement" functions.

If user enter uncorrect command utility takes message about it. After five unsuccessful attempts utility stops.


### About nucleic acid input

After entering command user need to print or paste nucleic acid sequence. It must contain only symbols 'A', 'C', 'G', 'T', 'U', 'R', 'Y', 'N' in uppercase or lowercase mode. If it contains some other symbols utility says about it.

The other mistacable thing is mixing 'U' and 'T' in one aminoacide. If it appears utility send warning message to user.
If nucleic acid has neither 'U', nor 'T' "NucAUt" send warning message too. If user prints 'yes' (or 'YES', or 'YeS' or something else) acid will be processed as DNA. If user enters something different - acid will be processed as RNA.
