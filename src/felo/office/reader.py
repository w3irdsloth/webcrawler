 ##########
## Reader ##
 ##########

# from os.path import splitext
# from mimetypes import guess_extension
# import os
# import re

class Reader(object):
    """ Creates an object for extracting text from files """


    def read_text(self, doc_name):
        try:
            doc = open(doc_name, "r")
            text = doc.read()
            return text

        except:
            print("something went wrong")



    #         except:
    #             print(".txt extraction failed")
    #             return False

    # def __init__(self):
    #     self.ext_list = [".txt", ".doc", ".docx", ".pdf"]
    #     self.text = ""

    # def get_text(self):
    #     return self.text

    # def split_ext(self, source):
    #     ext = splitext(source)[1]
    #     return ext

    # def guess_ext(self, source):
    #     ext_guess = guess_extension(source)
    #     return ext_guess

    # def check_ext(self, source):
    #     temp_ext = self.split_ext(source)
    #     if temp_ext not in self.ext_list:
    #         temp_ext = self.guess_ext(source)

    #     return temp_ext

    # #Extract text from source file
    # def extract_text(self, source):
    #     print("extracting from " + source + "...")
    #     ext = self.check_ext(source)
    #     temp_text = ""
    #     if ext == ".txt":
    #         try:
    #             temp_doc = open(source, "r")
    #             temp_text = temp_doc.read()

    #         except:
    #             print(".txt extraction failed")
    #             return False

    #     elif ext == ".doc" or ext == ".docx":
    #         try:
    #             from docx import Document
    #             temp_doc = Document(source)

    #             for prgrph in temp_doc.paragraphs:
    #                 for char in prgrph.text:
    #                     temp_text = temp_text + char

    #         except:
    #             print(".doc(x) extraction failed")
    #             return False

    #     elif ext == ".pdf":
    #         # #Use pdftotext
    #         # try:
    #         #     import pdftotext
    #         #     pdfobj = open(source, "rb")
    #         #     pdf = pdftotext.PDF(pdfobj)
    #         #     for pg in pdf:
    #         #         temp_text = temp_text + pg

    #         # Use PyMuPDF
    #         try:
    #             import fitz
    #             pdf = fitz.open(source)
    #             for pg in pdf:
    #                 temp_text = temp_text + pg.get_text("text")

    #         except:
    #             print(".pdf extraction failed")
    #             return False

    #     else:
    #         print("filetype not supported")
    #         return False

    #     self.text = temp_text
    #     return True


    # def extract_references(self, source):
    #     import fitz
    #     temp_refs = {}
    #     try:
    #         doc = fitz.open(source)
    #         temp_refs["file"] = os.path.basename(source)
    #         if len(doc.metadata["author"]) > 0:
    #             temp_refs["author"] = doc.metadata["author"]
        
    #         if len(doc.metadata["title"]) > 0:
    #             temp_refs["title"] = doc.metadata["title"]
            
    #         if len(doc.metadata["subject"]) > 0:
    #             temp_refs["subject"] = doc.metadata["subject"]
            
    #         if len(doc.metadata["creationDate"]) > 0:
    #             temp_refs["date"] = doc.metadata["creationDate"]

    #     except:
    #         print("unsupported document")
        
    #     return temp_refs

    # def extract_keywords(self, phrase_len, max_keywords):
    #     from rake_nltk import Rake
    #     r = Rake(max_length=phrase_len)
    #     r.extract_keywords_from_text(self.text)
    #     return r.get_ranked_phrases()[0:max_keywords]

    # def extract_meta(self, source):
    #     import fitz
    #     doc = fitz.open(source)
    #     return doc.metadata

    
