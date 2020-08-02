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

    #Scrape text from source document to string for manipulation
    def scrape_text(self, source):
        extndr = Extender(source)
        temp_text = extndr.call_extract()
        self.text = self.text + str(temp_text) + "\n"
       
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

#Construct object
converter = Converter()

#Return collected text
text = converter.get_text()

#scrape text to string
converter.scrape_text("/home/lux/Downloads/test/test3.docx")
text = converter.get_text()
print(text)

#strip word from string
#converter.strip_string("test")
#text = converter.get_text()
#print(text)

#strip slice from string
converter.strip_slice('"', '"')
text = converter.get_text()
print(text)

converter.strip_slice('!!', '!!')
text = converter.get_text()
print(text)



