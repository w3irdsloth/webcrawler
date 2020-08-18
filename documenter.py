
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
        if os.path.exists(document):
            doc = Document(document)

        else: 
            doc = Document()

        if len(self.tag) >= 1:
            tag_check = False
            for prgph in doc.paragraphs:
                if self.tag in prgph.text:
                    prgph.text = self.text
                    tag_check = True

            if tag_check == False:
                print("tag not found")
        
        else:
            print("no tag selected...")
            doc.add_paragraph(self.text)

        doc.save(document)
