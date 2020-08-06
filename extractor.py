 ###########
# Extractor #
 ###########

from splitter import Splitter

class Extractor(object):
    """ Creates an object for extracting text from files """
    def __init__(self):
        self.text = ""
        self.ext = ""

    def set_ext(self, ext):
        self.ext = ext

    def get_text(self):
        return self.text

    def discard_text(self):
        self.text = ""

    ##Call object for extracting text from files
    def extract_text(self, source):
        temp_text = ""
        if self.ext == ".txt":
            print("extracting from .txt...")
            temp_doc = open(source, "r")
            temp_text = temp_doc.read()

        if self.ext == ".docx":
            print("extracting from .docx...")
            from docx import Document
            temp_doc = Document(source)
            for prgrph in temp_doc.paragraphs:
                for char in prgrph.text:
                    temp_text = temp_text + char

        self.text = self.text + temp_text

##Extractor Functions##

#Set source file
#source = "/home/lux/Downloads/test/test.txt"
#source2 = "/home/lux/Downloads/test/test2.docx"

#Get extensions from splitter
#splitter = Splitter()

#splitter.split_source(source)
#ext = splitter.get_ext()

#splitter.split_source(source2)
#ext2 = splitter.get_ext()

#Build extractor
#extractor = Extractor()

#Pass in extension
#extractor.set_ext(ext)

#Call extract function
#extractor.extract_text(source)

#Print extracted text
#text = extractor.get_text()
#print(text)

#extractor.set_ext(ext2)
#extractor.extract_text(source2)
#text = extractor.get_text()
#print(text)

#Discard collected text
#extractor.discard_text()

#text = extractor.get_text()
#print("After discard...")
#print(text)

