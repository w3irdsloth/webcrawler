 #############
## Extractor ##
 #############

from os.path import splitext
import os
import re

class Extractor(object):
    """ Creates an object for extracting text from files """
    def __init__(self):
        self.text = ""

    def set_text(self, text):
        self.text = text

    def get_text(self):
        return self.text

    #Extract text from source file
    def extract_text(self, source):
        print("extracting from " + source + "...")
        ext = splitext(source)[1]
        temp_text = ""
        if ".txt" in ext:
            try:
                temp_doc = open(source, "r")
                temp_text = temp_doc.read()

            except:
                print(".txt extraction failed")

        elif ".doc" in ext:
            try:
                from docx import Document
                temp_doc = Document(source)

                for prgrph in temp_doc.paragraphs:
                    for char in prgrph.text:
                        temp_text = temp_text + char
            
            except:
                print(".doc extraction failed")

        # elif ".pdf" in ext:
            # #Use pdftotext
            # try:
            #     import pdftotext
            #     pdfobj = open(source, "rb")
            #     pdf = pdftotext.PDF(pdfobj)
            #     for pg in pdf:
            #         temp_text = temp_text + pg

            # # Use PyMuPDF
        else:
            try:
                import fitz
                pdf = fitz.open(source)
                for pg in pdf:
                    temp_text = temp_text + pg.get_text("text")

            except:
                print(".pdf extraction failed")
    

        # else:
        #     print("unsupported file type")


        self.text = temp_text

    def extract_references(self, source):
        import fitz
        temp_refs = {}
        try:
            doc = fitz.open(source)
            temp_refs["file"] = os.path.basename(source)
            if len(doc.metadata["author"]) > 0:
                temp_refs["author"] = doc.metadata["author"]
        
            if len(doc.metadata["title"]) > 0:
                temp_refs["title"] = doc.metadata["title"]
            
            if len(doc.metadata["subject"]) > 0:
                temp_refs["subject"] = doc.metadata["subject"]
            
            if len(doc.metadata["creationDate"]) > 0:
                temp_refs["date"] = doc.metadata["creationDate"]

        except:
            print("unsupported document")
        
        return temp_refs

    def extract_keywords(self, phrase_len, max_keywords):
        from rake_nltk import Rake
        r = Rake(max_length=phrase_len)
        r.extract_keywords_from_text(self.text)
        return r.get_ranked_phrases()[0:max_keywords]

    # def extract_meta(self, source):
    #     import fitz
    #     doc = fitz.open(source)
    #     return doc.metadata

    
