     ###############
    ##  COMMANDER  ##
     ###############

from applicator import Applicator
from extractor import Extractor
from generator import Generator
from splitter import Splitter
from stripper import Stripper

class Commander(object):
    """ Creates an object for getting and setting function commands """
    def __init__(self):
        functions = []
        for attr in dir(self):
            if callable(getattr(self, attr)) and "__" not in attr:
                functions.append(attr)

        self.functions = functions

    def get_functions(self):
        return self.functions

    def get_attributes(self, function):
        if function in self.functions:
            return getattr(self, function).__doc__

        else: 
            print("attribute not found")

     ########################
    ## Applicator Functions ##
     ########################

#     def apply_text(self, text, document):
#         """Apply text to document

#         Parameters:
#         text: Input text string
#         document: Output path or name for document

#         """
#         applicator = Applicator()
#         applicator.set_text(text)
#         applicator.apply_text(document)



     #######################
    ## Extractor Functions ##
     #######################

#     def extract_text(self, source, ext):
#         """Extract text from document

#         Parameters:
#         source: Source to extract from
#         extension: Extension for source document

#         """
#         extractor = Extractor()
#         extractor.set_ext(ext)
#         extractor.extract_text(source)
#         return extractor.get_text()



     #######################
    ## Generator Functions #
     #######################

    def gen_weight(self, source, epochs):
        """Generate weight from source file

        Parameters:
        source: Source to generate from
        epochs: Number of passes to train on

        """
        generator = Generator()
        generator.gen_weight(source, epochs)

#     def gen_text(self, weight, lines, temperature):
#         """Generate unique text from weight

#         Parameters:
#         weight: Weight to generate with
#         lines: Number of lines to generate
#         temperature: uniqueness of generated text

#         """
#         generator = Generator()
#         generator.set_weight(weight)
#         generator.gen_text(num_lines=lines, temp=temperature)
#         return generator.get_text()



     ######################
    ## Splitter Functions ##
     ######################

#     def split_path(self, source):
#         """Split pathname from source

#         Parameters:
#         source: source file or directory to split

#         """
#         splitter = Splitter()
#         splitter.split_source(source)
#         return splitter.get_path

#     def split_flname(self, source):
#         """Split filename with extension from source

#         Parameters:
#         source: source file or directory to split

#         """
#         splitter = Splitter()
#         splitter.split_source(source)
#         return splitter.get_flname

#     def split_name(self, source):
#         """Split filename without extension from source

#         Parameters:
#         source: source file or directory to split

#         """
#         splitter = Splitter()
#         splitter.split_source(source)
#         return splitter.get_name

#     def split_ext(self, source):
#         """Split extension from source

#         Parameters:
#         source: source file or directory to split

#         """
#         splitter = Splitter()
#         splitter.split_source(source)
#         return splitter.get_ext



     ######################
    ## Stripper Functions ##
     ######################

#     def strip_string(self, text, string):
#         """Strip string from text

#         Parameters:
#         text: Text to strip
#         string: String to strip from text

#         """
#         stripper = Stripper()
#         stripper.set_text(text)
#         stripper.strip_string(string)
#         return stripper.get_text()

#     def strip_slice(self, text, char1, char2):
#         """Strip slice form text

#         Parameters:
#         ext: Text to strip
#         char1: Start of slice
#         char2: End of slice

#         """
#         stripper = Stripper()
#         stripper.set_text(text)
#         stripper.strip_slice(char1, char2)
#         return stripper.get_text()

#     def strip_page(self, text, string):
#         """Strip remaining pages from text

#         Parameters:
#         text: Text to strip
#         string: Start of page

#         """
#         stripper = Stripper()
#         stripper.set_text(text)
#         stripper.strip_page(string)
#         return stripper.get_text()


    def batch(self, document, txtfile="tmp.txt"):
        """Batch a single document and print to a .txt file

        Parameters:
        document: Document to be stripped
        txtfile: File to print to 

        """
        splitter = Splitter()
        extractor = Extractor()
        applicator = Applicator()
        splitter.split_source(document)
        ext = splitter.get_ext()
        extractor.set_ext(ext)
        extractor.extract_text(document)
        txt = extractor.get_text()
        applicator.set_text(txt)
        applicator.apply_text(txtfile)
       


##################
##Function Calls##
##################

#################
#Applicator#
#################

##Build Applicator
#applicator = Applicator()

##Pass in text
#text = """ Here is a test string """
#applicator.set_text(text)

##Return text and print
#my_text = applicator.get_text()
#print(my_text)

##Paste text into document
#applicator.apply_text("mydoc.txt")


#################
#Extractor#
#################

##Set source file
#source = "/home/lux/Downloads/test/test.txt"
#source2 = "/home/lux/Downloads/test/test2.docx"

##Get extensions from splitter
#splitter = Splitter()

#splitter.split_source(source)
#ext = splitter.get_ext()

#splitter.split_source(source2)
#ext2 = splitter.get_ext()

##Build extractor
#extractor = Extractor()

##Pass in extension
#extractor.set_ext(ext)

##Call extract function
#extractor.extract_text(source)

##Print extracted text
#text = extractor.get_text()
#print(text)

##Do it again
#extractor.set_ext(ext2)
#extractor.extract_text(source2)
#text = extractor.get_text()
#print(text)

##Discard collected text
#extractor.discard_text()

##########################
#Generator#
#################

##Build generator object
#generator = Generator()

##Set source and epochs
#source = "/home/lux/Downloads/test/test.txt"
#epochs=1

##Generate a new weight
#generator.gen_weight(source, epochs)

##Set weight
#weight = "textgenrnn_weights.hdf5"
#generator.set_weight(weight)

##Generate text from weight
#generator.gen_text(num_lines=1, temp=0.5)

##Get the generated text and print
#text = generator.get_text()
#print(text)



##########################
#Splitter#
#################

##Build splitter object
#splitter = Splitter()

##Set source file
#source = "mysource"

##Split source path
#splitter.split_source(source)

##Return source path, filename, name with ext, and extension
#path = splitter.get_path()
#flname = splitter.get_flname()
#name = splitter.get_name()
#ext = splitter.get_ext()
#print(path)
#print(flname)
#print(name)
#print(ext)


##########################
#Stripper#
#################

##scrape text to string
#extractor = Extractor()
#source = "/home/lux/Downloads/test/test.txt"
#ext = ".txt"
#extractor.set_ext(ext)
#extractor.extract_text(source)
#text = extractor.get_text()

##Construct object
#stripper = Stripper()

##Pass collected text into object
#stripper.set_text(text)
#text1 = stripper.get_text()
#print("This is the text that was passed in: ")
#print(text1)

##strip string from text
#string = "This is a test"
#stripper.strip_string(string)

##strip slice from string
#slc1 = '"'
#slc2 = '"'
#stripper.strip_slice(slc1, slc2)

#slc1 = '!!'
#slc2 = '!!'
#stripper.strip_slice(slc1, slc2)

##strip page following string
#stripper.strip_page("End page here")

##Return collected text
#new_text = stripper.get_text()
#print("This is the text after being stripped: ")
#print(new_text)
#print(new_tex


