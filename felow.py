           
           ##   ###########   ##                            
        ###########################               ###################
      ####  ###################  ####           ## Hello, I'm Felow. ##
     #################################       ########################
    #############  FELOW  #############    #####          
     #############abcdefg############  ######
      ############ ###### ########### ####
        ###########      ###########
                ############        
                 ##########
                 
import argparse
import os

from applicator import Applicator
from builder import Builder
from cleaner import Cleaner
#from documenter import Documenter
from extractor import Extractor
#from finder import Finder
from generator import Generator

#Construct parsers
parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(title="commands", dest="command")

#batch text subparsers
batch = subparsers.add_parser(name="btc")
batch.add_argument("-p", "--path", action="store", dest="path", required=True)
batch.add_argument("-f", "--filename", action="store", dest="filename", default="extract.txt")

#build weight subparsers
build = subparsers.add_parser(name="bld")
build.add_argument("-f", "--filename", action="store", dest="filename", required=True)
build.add_argument("-epo", "--epochs", action="store", type=int, dest="epochs", required=True) 
build.add_argument("-num", "--numepochs", action="store", type=int, dest="numepochs", default=False)
build.add_argument("-wgt", "--weightname", action="store", dest="weightname", default="weight.hdf5")

#generate document subparsers
generate = subparsers.add_parser(name="gen")
generate.add_argument("-num", "--numwords", action="store", dest="numwords", type=int, required=True)
generate.add_argument("-lns", "--lines", action="store", dest="lines", type=int, default=1)
generate.add_argument("-tmp", "--temp", action="store", dest="temp", type=float, default= 0.5)
generate.add_argument("-wgt", "--weight", action="store", dest="weight", required=True)
generate.add_argument("-tag", "--tag", action="store", dest="tag", default="<content>")
generate.add_argument("-f", "--filename", action="store", dest="filename", required=True)
generate.add_argument("-t", "--title", action="store", dest="title", default="Title")


#Get arguments
args = parser.parse_args()

#Batch text from documents to .txt file
if args.command == "btc":
    path = args.path
    filename = args.filename
    if os.path.isdir(path):
        print("batching text...")
        extractor = Extractor()
        cleaner = Cleaner()
        for doc in os.listdir(path):
            #extract text from document
            ##The splitter function sets the ext internally##
            extractor.split_ext(doc)
           
            ##Is this necessary?##
            # ext = extractor.get_ext()
            # extractor.set_ext(ext)
           
            extractor.extract_text(os.path.join(path, doc))
            text = extractor.get_text()
            
            #Add text to cleaner
            cleaner.set_text(text)

            #clean cover
            string_list = ["Name", "Academic Institution", "Author Note", "Class", "Professor", "Date"]
            cleaner.remv_strings(string_list)
            
            #clean pars
            char1 = "("
            char2 = ")"
            cleaner.remv_slices(char1, char2)
        
            #clean quotes
            char1 = "\""
            char2 = "\""
            cleaner.remv_slices(char1, char2)

            #clean refs
            page_list = ["References", "Works Cited", "Bibliography"]
            cleaner.remv_pages(page_list)

            text = text + cleaner.get_text()
            
    else:
        print("not a path")
        raise SystemExit

    #Add collected text to cleaner
    cleaner.set_text(text)
    cleaner.build_sentlist()
    cleaner.remv_nodeclare()
    cleaner.remv_nums()
    cleaner.remv_wtspc()
    cleaner.remv_noalead()
    cleaner.trim_sentlist(28, 140)
    cleaner.remv_excap()
    #cleaner.fix_language() 
    cleaner.remv_language()

    #Format text as list
    cleaner.frmt_textlist()
    text = cleaner.get_text()

    #apply text to .txt doc
    applicator = Applicator()
    applicator.set_text(text)
    applicator.split_ext(filename)
    applicator.apply_text(filename)

#Build weight from .txt file
elif args.command == "bld":
    print("building weight...")
    filename = args.filename
    epochs = args.epochs
    numepochs = args.numepochs
    weightname = args.weightname
    builder = Builder()
    builder.build_weight(filename, epochs, numepochs, weightname)

#Generate document from weight
elif args.command == "gen":
    print("generating document...")
    numwords = args.numwords
    lines = args.lines
    temp = args.temp
    weight = args.weight
    tag = args.tag
    filename = args.filename
    title = args.title
    
    text = ""
    len_check = 0 
    cleaner = Cleaner()
    generator = Generator()
    generator.set_weight(weight)
    
    #Generate text based on word count
    while True:
        #Get remaining word count
        text_len = len(text.split())
        gen_num = numwords - text_len
        
        #Generate text based on remaining word count
        generator.gen_text(gen_num, lines, temp)
        text_list = generator.get_text_list()
        
        #Get length of generated text plus stored text
        gen_len = generator.get_textlength()
        len_check = text_len + gen_len
        print(str(len_check) + " words collected...")

        #Store text length before cleaning generated text
        old_len = len_check

        #Collect text and build sentence list
        cleaner.set_sentlist(text_list)
        cleaner.frmt_textstring()
        cleaner.build_sentlist()

        #Clean text in sentence list
        cleaner.remv_nodeclare()
        cleaner.remv_nums()
        cleaner.remv_wtspc()
        cleaner.remv_noalead()
        cleaner.trim_sentlist(28, 140)
        cleaner.fix_language()
        cleaner.remv_excap()
        cleaner.remv_language()
        
        #Format cleaned sentence list as string
        cleaner.frmt_textstring()
        cleaned_text = cleaner.get_text()
        
        #Collect cleaned text
        text = text + cleaned_text

        #Check length again
        new_len = len(text.split())
        disc_len = old_len - new_len
        print("old length: " + str(old_len))
        print("new length: " + str(new_len))
        len_check = new_len
        
        ####This wil be negative if no words are discarded###
        print(str(disc_len) + " words discarded...")
            
        #Break loop when word count reached
        if len_check >= numwords:
            break

    #Format generated text
    par_len = 175
    cleaner.set_text(text)
    cleaner.build_sentlist()
    cleaner.remv_wtspc()
    cleaner.frmt_textblock(par_len)
    text = cleaner.get_text()

    #Apply title to document
    applicator = Applicator()
    applicator.set_text(title)
    applicator.set_tag("Title")
    applicator.split_ext(filename)
    applicator.apply_text(filename)
    
    #Apply generated text to document
    applicator.set_text(text)
    applicator.set_tag(tag)
    applicator.split_ext(filename)
    applicator.apply_text(filename)

else:
    print("command not found")
    print("use -h or --help for available commands")