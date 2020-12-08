     ################
    ##  APPLICATOR  ##
     ################

import os
from os.path import splitext
from docx import Document

class Applicator(object):
    """ Creates an object for applying text to a file """
    def __init__(self):
        self.text = ""
        self.ext = ""
        self.tag = ""

    def get_text(self):
        return self.text

    def set_text(self, text):
       self.text = text
    
    def set_tag(self, tag):
        self.tag = tag

    def set_ext(self, ext):
        self.ext = ext
    
    #Split filepath for extension
    def split_ext(self, source):
        ext = splitext(source)[1]
        return ext

    #Apply text to .txt file
    def apply_text(self, document):
        print("applying text...")
        try:
            with open(document, "a") as temp_file:
                temp_file.write(self.text)
                temp_file.close()

        except:
            print("text application failed")
            raise SystemExit
