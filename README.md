----- FELOW - Fellow Editor and Logical Office Writer -----

FELOW is a set of command line tools to aid in the collection and generation of unique text.

Requirements:
python 3.8
tensorflow 
textgenrnn
python-language-tool
requests

optional (for file support):
python-docx
PyPDF2

Installation:
FELOW can be installed by cloning from the git repository and running /path/to/felow.py

Use:
dnl - downloads files from the internet (--query)
ext - extracts text from documents (--path)
bld - builds weight from text (--filename --epochs)
gen - generates unique text from weight (--numwords --weight --filename)
