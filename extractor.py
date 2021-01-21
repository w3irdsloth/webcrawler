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

        elif ".pdf" in ext:
            # #Use pdftotext
            # try:
            #     import pdftotext
            #     pdfobj = open(source, "rb")
            #     pdf = pdftotext.PDF(pdfobj)
            #     for pg in pdf:
            #         temp_text = temp_text + pg

            # # Use PyMuPDF
            try:
                import fitz
                pdf = fitz.open(source)
                for pg in pdf:
                    temp_text = temp_text + pg.get_text("text")

            except:
                print(".pdf extraction failed")
    

        else:
            print("unsupported file type")


        self.text = temp_text

    def extract_keywords(self):
        from rake_nltk import Rake
        r = Rake(max_length=1)
        r.extract_keywords_from_text(self.text)
        return r.get_ranked_phrases()[0:50]

    def strip_pars(self):
        temp_text = self.text
        #temp_text = re.sub(r'\([^)]*\)', '', temp_text)
        temp_text = re.sub(r"[\(\[].*?[\)\]]", "", temp_text)
        self.text = temp_text


    # def strip_pars(self):
    #     print("stripping parentheses..")
    #     temp_text = self.text
    #     temp_text = re.sub(r" ?\([^)]+\)", "", temp_text)
    #     temp_text = re.sub(r" ?\[[^)]+\]", "", temp_text)
    #     temp_text = re.sub(r" ?\{[^)]+\}", "", temp_text)
    #     self.text = temp_text

    # #This removes between quotes they just need to be taken out
    # def strip_quotes(self):
    #     print("stripping quotes...")
    #     temp_text = self.text
    #     temp_text = re.sub(r" ?\"[^)]+\"", "", temp_text)
    #     self.text = temp_text

    # def strip_quotes(self):
    #     print("stripping quotes...")
    #     temp_text = self.text
    #     temp_text = temp_text.replace('"', '')
    #     temp_text = temp_text.replace("'", '')
    #     self.text = temp_text

    def strip_tags(self):
        print("stripping tags...")
        temp_text = self.text
        cleaner = re.compile('<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});')
        temp_text = re.sub(cleaner, '', temp_text)
        #temp_text = re.sub(r" ?\<[^)]+\>", "", temp_text)
        self.text = temp_text

    # #This functionality was added to strip_tags
    # def strip_codes(self):
    #     print("stripping codes...")
    #     temp_text = self.text
    #     temp_text = re.sub(r" ?\&[^)]+\;", "", temp_text)
    #     self.text = temp_text

    # def strip_newlines(self):
    #     print("stripping newlines...")
    #     temp_text = self.text
    #     temp_text = temp_text.replace("\n", " ")
    #     self.text = temp_text

    # def strip_bars(self):
    #     print("stripping bars...")
    #     temp_text = self.text
    #     for char in temp_text:
    #         if char == "\\":
    #             temp_text = temp_text.replace(char, "")

    #     self.text = temp_text

    def strip_numbers(self):
        print("stripping numbers...")
        pattern = r'[0-9]'
        temp_text = re.sub(pattern, '', self.text)
        self.text = temp_text

    def strip_chars(self):
        bad_chars = ["{", "}", "#", "+", "-", "=", ">", "<" "@", "$", "|", "*", "_", "(", ")", "[", "]", ":", "\n", '"', ";", "/", "~", "`"]
        temp_text = self.text
        temp_text = ''.join(i for i in temp_text if not i in bad_chars)
        
        self.text = temp_text

    
