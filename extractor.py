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

    def get_text(self):
        return self.text

    #Extract text from source file
    def extract_text(self, source):
        print("extracting from " + source + "...")
        ext = splitext(source)[1]
        temp_text = ""
        if ".txt" in ext:
            print(".txt extraction started...")
            try:
                temp_doc = open(source, "r")
                temp_text = temp_doc.read()

            except:
                print("extraction failed")

        elif ".docx" in ext:
            print(".docx extraction started...")
            try:
                from docx import Document
                temp_doc = Document(source)

                for prgrph in temp_doc.paragraphs:
                    for char in prgrph.text:
                        temp_text = temp_text + char
            
            except:
                print("extraction failed")

        elif ".pdf" in ext:
            print(".pdf extraction started...")
            # try:
            #     import pdftotext
            #     pdfobj = open(source, "rb")
            #     pdf = pdftotext.PDF(pdfobj)
            #     for pg in pdf:
            #         temp_text = temp_text + pg

            # #Use pypdf2 instead of pdftotext (doesn't pull as much for some reason and removes spaces at times)
            # try:
            #     import PyPDF2
            #     pdf = open(source, "rb")
            #     reader = PyPDF2.PdfFileReader(pdf)
            #     pages = reader.numPages
            #     temp_text = ""
            #     for pg in range(pages):
            #         page = reader.getPage(pg)
            #         temp_text = temp_text + page.extractText()

            #     pdf.close()

            try:
                import fitz
                pdf = fitz.open(source)
                for pg in pdf:
                    temp_text = temp_text + pg.get_text("text")

            except:
                print("extraction failed")

        else:
            print("unsupported file type")

        self.text = temp_text

    def extract_keywords(self):
        print("extracting keywords...")
        from rake_nltk import Rake
        r = Rake(max_length=1)
        r.extract_keywords_from_text(self.text)
        keyword_list = r.get_ranked_phrases()
        return keyword_list

    def strip_pars(self):
        print("stripping parentheses..")
        temp_text = self.text
        temp_text = re.sub(r" ?\([^)]+\)", "", temp_text)
        self.text = temp_text

    def strip_quotes(self):
        print("stripping quotes...")
        temp_text = self.text
        temp_text = re.sub(r" ?\"[^)]+\"", "", temp_text)
        self.text = temp_text

    def strip_tags(self):
        print("stripping tags...")
        temp_text = self.text
        temp_text = re.sub(r" ?\<[^)]+\>", "", temp_text)
        self.text = temp_text

    def strip_newlines(self):
        print("stripping newlines...")
        temp_text = self.text
        for char in temp_text:
            if char == "\n":
                temp_text = temp_text.replace(char, " ")

        self.text = temp_text

    def strip_bars(self):
        temp_text = self.text
        for char in temp_text:
            if char == "\\":
                temp_text = temp_text.replace(char, "")

        self.text = temp_text

    
