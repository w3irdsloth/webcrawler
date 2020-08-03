##############################################################
# Strip text from documents to .txt for RNN machine learning #
##############################################################
import os
from unidecode import unidecode

from extender import Extender

class Converter(object):
    """ Creates a converter object for converting text from source documents to .txt files """
    def __init__(self):
        self.text= ""

    #Return collected text
    def get_text(self):
        return self.text

    #Scrape and collect text
    def scrape_text(self, source):
        extndr = Extender(source)
        temp_text = extndr.call_extract()
        self.text = self.text + str(temp_text) #+ "\n"
       
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

    #Print collected text to a .txt file
    def print_text(self, file_name):
        with open(file_name, "w") as temp_file:
            for char in self.text:
                temp_file.write(char)
                if char == ".":
                    temp_file.write("\n")



#Construct object
converter = Converter()

#Return collected text
text = converter.get_text()

#scrape text to string
converter.scrape_text("/home/lux/Downloads/test/test3.docx")
text = converter.get_text()
#print(text)

#strip word from string
#converter.strip_string("test")
#text = converter.get_text()
#print(text)

#strip slice from string
#converter.strip_slice('"', '"')
#text = converter.get_text()
#print(text)

converter.strip_slice('!!', '!!')
text = converter.get_text()
print(text)

#strip page following string
#converter.strip_page("References")
#text = converter.get_text()
#print(text)

converter.print_text("myfile")

