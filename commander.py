     ###############
    ##  COMMANDER  ##
     ###############

import os
from applicator import Applicator
from builder import Builder
from cleaner import Cleaner
from documenter import Documenter
from extractor import Extractor
from generator import Generator
#from splitter import Splitter
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
    # Applicator Functions #
    ########################

    def construct_applicator(self):
        applicator = Applicator()
        return applicator

    def apply_text(self, applicator, text, textfile):
        """Apply text to text document

        Parameters:
        text: Input text string
        document: Output path or name for document

        """
        applicator.set_text(text)
        applicator.apply_text(textfile)
        
    #####################
    # Builder Functions #
    #####################

    def construct_builder(self):
        builder = Builder()
        return builder

    def build_weight(self, builder, source, epochs, gen_epochs, weight_name):
        """Generate weight from source file

        Parameters:
        source: Source .txt file to generate from
        epochs: Number of passes to train on

        """
        builder.build_weight(source, epochs, gen_epochs, weight_name)
      
    #####################
    # Cleaner Functions #
    #####################

    def construct_cleaner(self):
        cleaner = Cleaner()
        return cleaner
    
    def clean_text(self, cleaner, text):
        """Clean unwanted symbols and characters from text

        Parameters:
        text: Input text string
        
        """
        cleaner.set_text(text)
        cleaner.build_sentlist()
        cleaner.remv_nodeclare()
        cleaner.remv_nums()
        cleaner.remv_wtspc()
        cleaner.remv_noalead()
        cleaner.trim_sentlist(28, 140) 
        cleaner.remv_language()
        return cleaner.get_text()
        
    def format_list(self, cleaner, text):
        return cleaner.frmt_textlist()

    #Separate set text, format textblock, and Cleaner constructor into their own function.
    # def clean_textblock(self, cleaner, text):
    #     cleaner.set_text(text)
    #     cleaner.build_sentlist()
    #     cleaner.remv_nodeclare()
    #     cleaner.remv_nums()
    #     cleaner.remv_wtspc()
    #     cleaner.remv_noalead()
    #     cleaner.trim_sentlist(28, 140)
    #     cleaner.remv_language()
    #     return cleaner.get_text()
    
    def format_block(self, cleaner, text, par_len):
        return cleaner.frmt_textblock(par_len)

    ########################     
    # Documenter Functions #
    ########################

    def construct_documenter(self):
        documenter = Documenter()
        return documenter

    def document_text(self, documenter, text, tag, document):
        """Create a document from text

        Parameters:
        text: Input text string
        tag: tag name for paragraph input
        document: Output path name for document
        
        """
        documenter.set_text(text)
        documenter.set_tag(tag)
        documenter.document_text(document)

    #######################
    # Extractor Functions #
    #######################

    def construct_extractor(self):
        extractor = Extractor()
        return extractor
    
    def extract_text(self, extractor, source):
        """Extract text from document

        Parameters:
        source: Source to extract from
        extension: Extension for source document

        """
        #splitter = Splitter()
        #splitter.split_source(source)
        ext = extractor.split_ext(source)
        extractor.set_ext(ext)
        extractor.extract_text(source)
        return extractor.get_text()

    #######################
    # Generator Functions #
    #######################

    def construct_generator(self):
        generator = Generator()
        return generator
    
    def gen_text(self, generator, lines, temperature, weight):
        """Generate unique text from weight

        Parameters:
        weight: Weight to generate with
        lines: Number of lines to generate
        temperature: uniqueness of generated text

        """
        generator.set_weight(weight)
        generator.gen_text(num_lines=lines, temp=temperature)
        text_list = generator.get_text()
        # text =""
        # for sentc in text_list:
        #     text = text + sentc
        #     text = text + "  "

        return text_list

    ######################
    # Splitter Functions #
    ######################

    # def split_path(self, source):
    #     """Split pathname from source

    #     Parameters:
    #     source: source file or directory to split

    #     """
    #     splitter = Splitter()
    #     splitter.split_source(source)
    #     return splitter.get_path

    # def split_flname(self, source):
    #     """Split filename with extension from source

    #     Parameters:
    #     source: source file or directory to split

    #     """
    #     splitter = Splitter()
    #     splitter.split_source(source)
    #     return splitter.get_flname

    # def split_name(self, source):
    #     """Split filename without extension from source

    #     Parameters:
    #     source: source file or directory to split

    #     """
    #     splitter = Splitter()
    #     splitter.split_source(source)
    #     return splitter.get_name

    # def split_ext(self, source):
    #     """Split extension from source

    #     Parameters:
    #     source: source file or directory to split

    #     """
    #     splitter = Splitter()
    #     splitter.split_source(source)
    #     return splitter.get_ext

    ######################
    # Stripper Functions #
    ######################

    def construct_stripper(self):
        stripper = Stripper()
        return stripper
    
    def strip_string(self, stripper, text, string):
        """Strip string from text

        Parameters:
        text: Text to strip
        string: String to strip from text

        """
        stripper.set_text(text)
        stripper.strip_string(string)
        return stripper.get_text()

    def strip_strings(self, stripper, text, string_list):
        for strng in string_list:
            while strng in text:
                text = self.strip_string(stripper, text, strng)
        
        return text

    def strip_slice(self, stripper, text, char1, char2):
        """Strip slice form text

        Parameters:
        ext: Text to strip
        char1: Start of slice
        char2: End of slice

        """
        stripper.set_text(text)
        stripper.strip_slice(char1, char2)
        return stripper.get_text()

    def strip_slices(self, stripper, text, char1, char2):
        for char1 in text:
            text = self.strip_slice(stripper, text, char1, char2)
        
        return text

    def strip_page(self, stripper, text, string):
        """Strip remaining pages from text

        Parameters:
        text: Text to strip
        string: Start of page

        """
        stripper.set_text(text)
        stripper.strip_page(string)
        return stripper.get_text()

    def strip_pages(self, stripper, text, page_list):
        for pg in page_list:
            while pg in text:
                text = self.strip_page(stripper, text, pg)

        return text


