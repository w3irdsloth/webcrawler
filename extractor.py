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

    def get_text(self):
        return self.text

    # def set_text(self, text):
    #     self.text = text

    #Extract text from source file
    def extract_text(self, source):
        ext = splitext(source)[1]
        temp_text = ""
        if ext == ".txt":
            print("extracting from .txt...")
            try:
                temp_doc = open(source, "r")
                temp_text = temp_doc.read()

            except:
                print("extraction failed")

        elif ext == ".docx":
            print("extracting from .docx...")
            try:
                from docx import Document
                temp_doc = Document(source)

                for prgrph in temp_doc.paragraphs:
                    for char in prgrph.text:
                        temp_text = temp_text + char
            
            except:
                print("extraction failed")

        elif ext == ".pdf":
            print("extracting from .pdf...")
            try:
                pdfobj = open(source, "rb")
                pdf = pdftotext.PDF(pdfobj)
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
