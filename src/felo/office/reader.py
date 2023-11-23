 ##########
## Reader ##
 ##########

from os.path import isfile

class Reader(object):
    """Constructs an object for extracting text from files."""

    def __init__(self):
        """Constructs the necessary attributes for the Reader object."""
        self.handlers = {}
        
    def set_handlers(self, handlers):
        """Sets doctype handlers."""
        self.handlers = handlers
    
    def get_handlers(self, handlers):
        """Returns doctype handlers."""
        return self.handlers

    def read_text(self, txt_name):
        """Reads text from .txt files."""
        if isfile(txt_name):
            pass

        else:
            print("not a file")
            return None
        
        try:
            doc = open(txt_name, "r")
            text = doc.read()
            return text
        except:
            print("read failed")
            return None
            

    def read_doc(self, doc_name):
        """Reads text from .doc files."""
        if isfile(doc_name):
            pass

        else:
            print("not a file")
            return None
        
        doc_text = ""
        print("reading .doc file")

        # Use docx
        if self.handlers[".doc"] == "docx":
            try:
                from docx import Document
                temp_doc = Document(doc_name)
                for prgrph in temp_doc.paragraphs:
                    for char in prgrph.text:
                        doc_text = doc_text + char

            except:
                    print("read failed [docx]")
                    doc_text = None

        ## Add more .doc handlers here ##
            
        else:
            print("no .docx handlers available")
            doc_text = None

        return doc_text

    def read_pdf(self, pdf_name):
        """Reads text from .pdf files."""
        if isfile(pdf_name):
            pass

        else:
            print("not a file")
            return None
        
        pdf_text = ""
        print("reading .pdf file...")
        
        # USe pdftotext
        if self.handlers[".pdf"] == "pdftotext":
            try:
                import pdftotext
                pdfobj = open(pdf_name, "rb")
                pdf = pdftotext.PDF(pdfobj)
                for pg in pdf:
                    pdf_text = pdf_text + pg

            except:
                print("read failed [pdftotext]")
                return None

        # Use PyMuPdf
        elif self.handlers[".pdf"] == "pymupdf":
            try:
                import fitz
                pdf = fitz.open(pdf_name)
                for pg in pdf:
                    pdf_text = pdf_text + pg.get_text("text")
            except:
                print("read failed [pymupdf]")

        ## Add more .pdf handlers here ##

        else:
            print("no .pdf handlers available")
            return None
        
        return pdf_text
