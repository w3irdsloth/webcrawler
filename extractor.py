 ###############
##  EXTRACTOR  ##
 ###############

class Extractor(object):
    """ Creates an object for extracting text from files """
    def __init__(self):
        self.text = ""
        self.ext = ""

    def set_ext(self, ext):
        self.ext = ext

    def get_text(self):
        return self.text

    def discard_text(self):
        self.text = ""

    ##Call object for extracting text from files
    def extract_text(self, source):
        temp_text = ""
        if self.ext == ".txt":
            print("extracting from .txt...")
            temp_doc = open(source, "r")
            temp_text = temp_doc.read()

        if self.ext == ".docx":
            print("extracting from .docx...")
            from docx import Document
            temp_doc = Document(source)
            for prgrph in temp_doc.paragraphs:
                for char in prgrph.text:
                    temp_text = temp_text + char

        else:
            print("unsupported file type")

        self.text = self.text + temp_text

