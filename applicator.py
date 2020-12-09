     ################
    ##  APPLICATOR  ##
     ################

import os
from os.path import splitext
#from docx import Document

class Applicator(object):
    """ Creates an object for applying text to a file """
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

    def get_ext(self):
        return self.ext
    
    def set_ext(self, ext):
        self.ext = ext
    
    #Split filepath for extension
    def split_ext(self, source):
        ext = splitext(source)[1]
        self.ext = ext

    #Apply text to .txt file
    def apply_text(self, document):
        if self.ext == ".txt":
            print("applying text to .txt file...")
            try:
                with open(document, "a") as temp_file:
                    temp_file.write(self.text)
                    temp_file.close()

            except:
                print("text application failed")
                raise SystemExit

        elif self.ext == ".docx":
            from docx import Document
            print("printing to .docx file...")
            try:
                doc = Document(document)
            
            except:
                doc = Document()

            tag_check = False
            if len(self.tag) >= 1:
                for prgph in doc.paragraphs:
                    if self.tag in prgph.text:
                        print("printing to selected tag...")
                        prgph.text = self.text                    
                        doc.save(document)
                        tag_check = True       
                        break

                if tag_check == False:
                    print("tag not found")
                    print("printing to end of file...")
                    doc.add_paragraph(self.text)
                    doc.save(document)

            else:
                print("no tag selected")
                print("printing to end of file...")
                doc.add_paragraph(self.text)
                doc.save(document)

        else:
            print("unsupported file type")
