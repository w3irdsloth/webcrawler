import os
from docx import Document

class Extender(object):
    """ Creates an extender object for handling extraction from filetype extensions """
    def __init__(self, source):
        self.source = source
        self.split_path = os.path.split(self.source)
        self.source_name = self.split_path[1]
        self.split_ext = os.path.splitext(self.source_name)
        self.ext = self.split_ext[1]

    #Call extractors for scraping text from various extensions
    def call_extract(self):
        temp_text = ""
        if self.ext == ".docx":
            print("sourcing .docx...")

            temp_text = ""
            temp_doc = Document(self.source)
            for prgrph in temp_doc.paragraphs:
                for char in prgrph.text:
                    temp_text = temp_text + char

        return temp_text
            
