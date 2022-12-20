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
File (or directory with all content) vanishing in the original place with the original name. File (or directory) appears in the new path or with new name.
![Illustartion of command `mv.py pencil.txt ../another_folder`](./pencil.jpg)


> Conditions, warnings and errors
If you didn't save the script in the one of the directories, which is output of `sys.path` command, script will work only if you write path to folder with script, as example `/home/name/IB/python/mv.py dir1 dir2`. Also ot can't work if you will use a directory as first argument and a file as a second one.

#### rm.py

```python
rm.py <file> 
rm.py -r <dir>
```
> Functional
This script can remove files and directories.

> Input data
Path to file or path to directory with the `-r` flag.

> Output data
File (or directory with all content) vanishing in the original place and didn't appears in the new one.

> Conditions, warnings and errors
If you didn't save the script in the one of the directories, which is output of `sys.path` command, script will work only if you write path to folder with script, as example `/home/name/IB/python/rm.py -r dir1`. You can't remove directory without `-r` flag.

#### wc.py

```python
wc.py -wcl wc.py
```
> Functional
This script counts number of symbols, words (1+ symbol between spaces) and lines.

> Input data
File or stdin. You need to use flags: `-b` for counting symbols, `-w` for counting words, `-l` for counting lines.

> Output data
Number of lines, words and bytes (all countings are conditional).

> Conditions, warnings and errors
If you didn't save the script in the one of the directories, which is output of `sys.path` command, script will work only if you write path to folder with script, as example `/home/name/IB/python/wc.py -w `. If you use noone of flags, script counts all three flags. `wc.py` can work in a pipe, as example ```grep "pattern" <file> | wc -wl```
  
#### ls.py

```python
ls.py 
ls.py -a <dir>
```
> Functional
This script can show content of the directory (including hidden files).

> Input data
Path to the directory. If you need to show the hidden files, you need to use `-a` flag.

> Output data
Files and directories, included in the directory of interest.

> Conditions, warnings and errors
If you didn't save the script in the one of the directories, which is output of `sys.path` command, script will work only if you write path to folder with script, as example `/home/name/IB/python/ls.py -a ../dir1`. 
  
#### sort.py

```python
sort.py wc.py
```
> Functional
This script returns lexicographically written lines of file.

> Input data
File or stdin. 
  
> Output data
Lexicographically sorted strings.

> Conditions, warnings and errors
If you didn't save the script in the one of the directories, which is output of `sys.path` command, script will work only if you write path to folder with script, as example `/home/name/IB/python/sort.py wc.py`. You can't put text in the `sort.py` explicitly, you can only put the file or ptint something in the stdin. `sort.py` can work with pipes. As example: `grep "pattern" <file> | sort"

 Dixi et, animam levavi
