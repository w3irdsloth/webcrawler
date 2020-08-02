##############################################################
# Strip text from documents to .txt for RNN machine learning #
##############################################################
import os
import textract

class Converter(object):
    """ Creates a converter object for converting text from source documents to .txt files"""
    def __init__(self):
        self.text= ""

    #Return collected text
    def get_text(self):
        return self.text

    #Scrape text from source document
    def scrape_text(self, source):
        temp_text = textract.process(source)
        self.text = self.text + str(temp_text)
        

#Construct object
converter = Converter()

#Return collected text
text = converter.get_text()
print(text)

converter.scrape_text("/home/lux/Downloads/test/test3.docx")
text = converter.get_text()
print("doc3")
print(text)
