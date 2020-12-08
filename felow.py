           
           ##   ###########   ##                            
        ###########################               ###################
      ####  ###################  ####           ## Hello, I'm Felow. ##
     #################################       ########################
    #############  FELOW  #############    #####          
     #################################  ######
      ############ ###### ########### ####
        ###########      ###########
                ############        
                 ##########
                 
import argparse
import os

from applicator import Applicator
from builder import Builder
from commander import Commander
from cleaner import Cleaner
from documenter import Documenter
from extractor import Extractor
from generator import Generator
from stripper import Stripper

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

#command mode subparsers
mediate = subparsers.add_parser(name="cmd")

#Get arguments
args = parser.parse_args()

#Construct commander
commander = Commander()

#Batch text from documents to .txt file
if args.command == "btc":
    print("batching text...")
    path = args.path
    filename = args.filename
    extractor = Extractor()
    stripper = Stripper()
    for doc in os.listdir(path):
        extractor.split_ext(doc)
        ext = extractor.get_ext()
        extractor.set_ext(ext)
        extractor.extract_text(os.path.join(path, doc))
        text = extractor.get_text()
        stripper.set_text(text)
        #strip cover
        string_list = ["Name", "Academic Institution", "Author Note", "Class", "Professor", "Date"]
        stripper.strip_strings(string_list)
        
        #strip pars
        char1 = "("
        char2 = ")"
        stripper.strip_slices(char1, char2)
    
        #strip quotes
        char1 = "\""
        char2 = "\""
        stripper.strip_slices(char1, char2)

        #strip refs
        page_list = ["References", "Works Cited", "Bibliography"]
        stripper.strip_pages(page_list)

        text = text + stripper.get_text()

    #send text for cleaning
    cleaner = Cleaner()
    cleaner.set_text(text)
    cleaner.build_sentlist()
    cleaner.remv_nodeclare()
    cleaner.remv_nums()
    cleaner.remv_wtspc()
    cleaner.remv_noalead()
    cleaner.trim_sentlist(28, 140) 
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
    temp_text = ""
    len_check = 0 
    cleaner = Cleaner()
    generator = Generator()
    generator.set_weight(weight)
    
    #Generate text based on word count
    while True:
        #Generate text list
        generator.gen_text(lines, temp)

        #Convert text list to string
        generator.cnvrt_text()
        generated_text = generator.get_text()

        #Collect generated text into string
        temp_text = temp_text + generated_text
        generated_text = ""
    
        #Get length of generated text plus stored text
        len_check = len(text.split()) + len(temp_text.split())
        print(str(len_check) + " words generated...")
        
        #Clean generated text if page count has been reached
        if len_check >= numwords:
            old_len = len_check
            cleaner.set_text(temp_text)
            cleaner.build_sentlist()
            cleaner.remv_nodeclare()
            cleaner.remv_nums()
            cleaner.remv_wtspc()
            cleaner.remv_noalead()
            cleaner.trim_sentlist(28, 140) 
            cleaner.remv_language()
            cleaned_text = cleaner.get_text()
            text = text + cleaner.get_text()
            temp_text = ""

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

    par_len = 175
    cleaner.set_text(text) 
    cleaner.frmt_textblock(par_len)
    text = cleaner.get_text()

    # documenter = Documenter()

    # #Apply title to document
    # documenter.set_text(title)
    # documenter.set_tag("Title")
    # documenter.document_text(filename)

    # #Apply generated text to document
    # documenter.set_text(text)
    # documenter.set_tag(tag)
    # documenter.document_text(filename)

    applicator = Applicator()
    
    #Apply generated text to document
    applicator.set_text(text)
    applicator.set_tag(tag)
    applicator.split_ext(filename)
    applicator.apply_text(filename)

elif args.command == "cmd":
    commander = Commander()
    commander.cmd_mode()

else:
    print("command not found")
    print("use -h or --help for available commands")
 
