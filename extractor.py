 #############
## Extractor ##
 #############

from os.path import splitext
import os

import pdftotext

class Extractor(object):
    """ Creates an object for extracting text from files """
    def __init__(self):
        self.text = ""
        self.ext = ""

    def get_ext(self):
        return self.ext

    def set_ext(self, ext):
        self.ext = ext

    def get_text(self):
        return self.text

    def set_text(self, text):
        self.text = text

    #Split filepath for extension
    def split_ext(self, source):
        ext = splitext(source)[1]
        self.ext = ext

    #Extract text from source file
    def extract_text(self, source):
        temp_text = ""
        if self.ext == ".txt":
            print("extracting from .txt...")
            try:
                temp_doc = open(source, "r")
                temp_text = temp_doc.read()

            except:
                print("extraction failed")

        elif self.ext == ".docx":
            print("extracting from .docx...")
            try:
                from docx import Document
                temp_doc = Document(source)
                for prgrph in temp_doc.paragraphs:
                    for char in prgrph.text:
                        temp_text = temp_text + char
            
            except:
                print("extraction failed")

        elif self.ext == ".pdf":
            print("extracting from .pdf...")
            try:
                print("trying...")
                pdfobj = open(source, "rb")
                print("object set")
                pdf = pdftotext.PDF(pdfobj)
                print("pdf set")
                for pg in pdf:
                    temp_text = temp_text + pg

                pdf.close()

            # try:
            #     import PyPDF2
            #     pdf = open(source, "rb")
            #     reader = PyPDF2.PdfFileReader(pdf)
            #     print("reader set")
            #     pages = reader.numPages
            #     temp_text = ""
            #     for pg in range(pages):
            #         page = reader.getPage(pg)
            #         temp_text = temp_text + page.extractText()

            #     pdf.close()

            except:
                print("extraction failed")

        else:
            print("unsupported file type")

        self.text.strip()
        self.text = self.text + temp_text
