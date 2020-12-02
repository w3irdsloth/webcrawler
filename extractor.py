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
                print(source)
                temp_doc = Document(source)
                for prgrph in temp_doc.paragraphs:
                    for char in prgrph.text:
                        temp_text = temp_text + char
            
            except:
                print("extraction failed")

        else:
            print("unsupported file type")

        self.text = self.text + temp_text

