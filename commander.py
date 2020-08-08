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

    def apply_text(self, text, textfile):
        """Apply text to text document

        Parameters:
        text: Input text string
        document: Output path or name for document

        """
        applicator = Applicator()
        applicator.set_text(text)
        applicator.apply_text(textfile)



     #######################
    ## Extractor Functions ##
     #######################

    def extract_text(self, source):
        """Extract text from document

        Parameters:
        source: Source to extract from
        extension: Extension for source document

        """
        extractor = Extractor()
        splitter = Splitter()
        splitter.split_source(source)
        ext = splitter.get_ext()
        extractor.set_ext(ext)
        extractor.extract_text(source)
        return extractor.get_text()



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

    def gen_text(self, lines, temperature, weight="textgenrnn_weights.hdf5"):
        """Generate unique text from weight

        Parameters:
        weight: Weight to generate with
        lines: Number of lines to generate
        temperature: uniqueness of generated text

        """
        generator = Generator()
        generator.set_weight(weight)
        generator.gen_text(num_lines=lines, temp=temperature)
        text_list = generator.get_text()
        text = ""
        for char in text_list:
            text += char
        
        return text


     ######################
    ## Splitter Functions ##
     ######################

    def split_path(self, source):
        """Split pathname from source

        Parameters:
        source: source file or directory to split

        """
        splitter = Splitter()
        splitter.split_source(source)
        return splitter.get_path

    def split_flname(self, source):
        """Split filename with extension from source

        Parameters:
        source: source file or directory to split

        """
        splitter = Splitter()
        splitter.split_source(source)
        return splitter.get_flname

    def split_name(self, source):
        """Split filename without extension from source

        Parameters:
        source: source file or directory to split

        """
        splitter = Splitter()
        splitter.split_source(source)
        return splitter.get_name

    def split_ext(self, source):
        """Split extension from source

        Parameters:
        source: source file or directory to split

        """
        splitter = Splitter()
        splitter.split_source(source)
        return splitter.get_ext



     ######################
    ## Stripper Functions ##
     ######################

    def strip_string(self, text, string):
        """Strip string from text

        Parameters:
        text: Text to strip
        string: String to strip from text

        """
        stripper = Stripper()
        stripper.set_text(text)
        stripper.strip_string(string)
        return stripper.get_text()

    def strip_slice(self, text, char1, char2):
        """Strip slice form text

        Parameters:
        ext: Text to strip
        char1: Start of slice
        char2: End of slice

        """
        stripper = Stripper()
        stripper.set_text(text)
        stripper.strip_slice(char1, char2)
        return stripper.get_text()

    def strip_page(self, text, string):
        """Strip remaining pages from text

        Parameters:
        text: Text to strip
        string: Start of page

        """
        stripper = Stripper()
        stripper.set_text(text)
        stripper.strip_page(string)
        return stripper.get_text()


      ##########################
    #####  Complex Functions  #####
      ##########################

    def batch(self, document, textfile="tmp.txt"):
        """Batch a single document and print to a .txt file

        Parameters:
        document: Document to be stripped
        textfile: File to print to 

        """
        text = self.extract_text(document)
        self.apply_text(text, textfile)
       

    def generate(self, lines, temperature, document, weight="textgenrnn_weights.hdf5"):
        """Generate unique text and apply it to a document """
        print("generating...")
        text = self.gen_text(lines, temperature)        
        self.apply_text(text, document)


