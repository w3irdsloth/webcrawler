##############################################################
# Strip text from documents to .txt for RNN machine learning #
##############################################################
import os
import textract
from unidecode import unidecode

class Converter(object):
    """ Creates a converter object for converting text from source documents to .txt files"""
    def __init__(self):
        self.text= ""

    #Return collected text
    def get_text(self):
        return self.text

    #Scrape text from source document to string for manipulation
    def scrape_text(self, source):
        temp_text = textract.process(source)
        self.text = self.text + str(temp_text)
       
    #Strip characters from collected text   
    def strip_text(self, word):
        temp_text = unidecode(self.text)
        if word in temp_text:
            temp_text = temp_text.replace(word, "")

        self.text = temp_text

    #Strip string from collected text
    #def strip_string(self, start_char, end_char):



#Construct object
converter = Converter()

#Return collected text
text = converter.get_text()

#scrape text to string
converter.scrape_text("/home/lux/Downloads/test/test3.docx")
text = converter.get_text()
print(text)

#strip word from string
converter.strip_text("test")
text = converter.get_text()
print(text)


