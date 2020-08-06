 ##########
# Stripper #
 ##########

import os
from unidecode import unidecode

from extractor import Extractor

class Stripper(object):
    """ Creates an object for stripping unwanted characters from text """
    def __init__(self):
        self.text= ""

    #Return collected text
    def get_text(self):
        return self.text

    def set_text(self, text):
        self.text = text

    #Strip string from collected text   
    def strip_string(self, string):
        temp_text = unidecode(self.text)
        if string in temp_text:
            temp_text = temp_text.replace(string, "")

        self.text = temp_text

    #Strip slice from collected text
    def strip_slice(self, char1, char2):
        temp_text = unidecode(self.text)
        slice_start = temp_text.find(char1)
        slice_end = temp_text.find(char2, slice_start + 1)
        temp_text = temp_text.replace(temp_text[slice_start:slice_end + 1], "")
        self.text = temp_text

    #Discard collected text that appears after the given string
    def strip_page(self, string):
        temp_text = self.text
        if string in temp_text:
            slice_start = temp_text.index(string)
            temp_text = temp_text[:slice_start]

        self.text = temp_text



##Stripper Functions##

#scrape text to string
extractor = Extractor()

source = "/home/lux/Downloads/test/test.txt"
ext = ".txt"

extractor.set_ext(ext)
extractor.extract_text(source)

text = extractor.get_text()


#Construct object
stripper = Stripper()

#Pass collected text into object
stripper.set_text(text)
text1 = stripper.get_text()
print("This is the text that was passed in: ")
print(text1)



#strip string from text
string = "This is a test"
stripper.strip_string(string)

#strip slice from string
slc1 = '"'
slc2 = '"'
stripper.strip_slice(slc1, slc2)

slc1 = '!!'
slc2 = '!!'
stripper.strip_slice(slc1, slc2)

#strip page following string
stripper.strip_page("End page here")

#Return collected text
new_text = stripper.get_text()
print("This is the text after being stripped: ")
print(new_text)


