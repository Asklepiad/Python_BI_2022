# Python_BI_2022
Repository for bioinformatics institute

## Setup of pain.py


### System properties

Script was runned on the GNU Linux **Ubuntu 20.04** LTS, with **Python** version **3.10.6**
I used **pip** version **20.0.2**


### Fast description

It's important to use virtual environments when using different tools and python scripts for escaping incompartibilities.
1. On the first stage it's need to create new conda virtual environment for exact python version. You need to input on command line described below script. First it's need to check if the name of the next virtual environment has already existed.
`conda env list`

If "py310" is not in apeeared list, you may use it while creating new virtual environment. If not, you may use other name. In this guide I will use "py310" name. If it has already existed, you need to use other name of virtual environment.
`conda create -n py310 python=3.10`

Then you need to activate this virtual environment.
`conda activate py310`

If name "py310" will appear on the left part of the command line, it's all correct.


2. On the next step you need to create pip venv (virtual environment) for using python modules and packages.
  First, you need to create directory, when your script will be situated.
  `mkdir pain_directory`
  `cd ./pain_directory`
  
  Second, you need create venv and activate it.
  `pip -m venv pain`
  `source pain/bin/activate`
  
  On this stage you need to have (pain)(py310) on the left part of the of the command line.
  
  
 3. Next step is cloning the repository with script and requirements.txt
  `git clone <repository_url>`
  
  You need to install requirements with command:
  `pip install -r requirements.txt`
  
  Making file executable is realized by the next command:
  `chmod +x ./<directory with pain.py>/pain.py`
  
  Finally you need to execute script:
  `python3 ./<directory with pain.py>/pain.py`
  
P.S. Sometimes samurai has a target.
