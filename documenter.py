     ################
    ##  Documenter  ##
     ################

import os
from docx import Document

class Documenter(object):
    """Add text to a new or existing document based on a specified placeholder tag """

    def __init__(self):
        self.text = ""
        self.ext = ""
        self.tag = ""

    def get_text(self):
        return self.text

    def set_text(self, text):
        self.text = text

    def set_tag(self, tag):
        self.tag = tag

    def document_text(self, document):
        if os.path.isfile(document):
            try:
                doc = Document(document)
            
            except:
                print("unsupported document")
                raise SystemExit

        else: 
            doc = Document()

        if len(self.tag) >= 1:
            tag_check = False
            try:
                for prgph in doc.paragraphs:
                    if self.tag in prgph.text:
                        prgph.text = self.text
                        tag_check = True
            
                doc.save(document)
            
            except:
                print("unsupported document")
                raise SystemExit                

            if tag_check == False:
                print("tag not found")
                raise SystemExit

        else:
            print("no tag selected...")
            try:
                doc.add_paragraph(self.text)
                doc.save(document)

            except:
                print("unsupported document")
                raise SystemExit


