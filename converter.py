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

        #pthsplit = os.path.split(source)
        #flname = pthsplit[1]
        #flsplit = os.path.splitext(flname)
        #extn = flsplit[1]
        

        #print(source)
        #print(flname)
        #print(extn)
        #print(extn[1])

#Construct object
converter = Converter()

#Return collected text
text = converter.get_text()
print(text)


converter.scrape_text("/home/lux/Downloads/test/test1.docx")
text = converter.get_text()
print("doc1")
print(text)

converter.scrape_text("/home/lux/Downloads/test/test2.docx")
text = converter.get_text()
print("doc2")
print(text)

converter.scrape_text("/home/lux/Downloads/test/test3.docx")
text = converter.get_text()
print("doc3")
print(text)
