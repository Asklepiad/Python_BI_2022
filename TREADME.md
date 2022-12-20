# Python_BI_2022
Repository for bioinformatics institute

## Linux-imitation scripts

### System properties

The script was run on the GNU Linux **Ubuntu 20.04** LTS, with **Python** version **3.9.13**

### Fast description
Scripts in this folder imitate (on different similiarity level) basic bash utilities: rm, wc, ls, sort and mv.

### Installation
You need to download scripts **mv.py**,**ls.py**, **rm.py**, **sort.py**, **wc.py** and save them in one of folders in the one of the directories, which is output of `sys.path` command.

### Scripts

#### mv.py


```python
mv.py <file_or_dir1> <file_or_dir2>
```
> Functional
This script can rename file, move file into another directory or move directory into another directory.

> Input data
Pathes (absolute or relative) to two files (for renaming mode), file and directory (for moving file) two directories (for moving directories).

> Output data
File (or directory) vanishing in the original place with the original name. File (or directory) appears in the new path or with new name.
![Illustartion of command `mv.py pencil.txt ../another_folder`](./pencil.jpg)

> Conditions, warnings and errors
If the number of columns in first matrix is not equal to the number of rows in second matrix, tool returns typical error. Example is given below:
