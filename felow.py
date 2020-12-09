           
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
from extractor import Extractor
#from generator import Generator

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
    path = args.path
    filename = args.filename
    if os.path.isdir(path):
        print("batching text...")
        extractor = Extractor()
        cleaner = Cleaner()
        for doc in os.listdir(path):
            extractor.split_ext(doc)
            ext = extractor.get_ext()
            extractor.set_ext(ext)
            extractor.extract_text(os.path.join(path, doc))
            text = extractor.get_text()
            cleaner.set_text(text)
            #strip cover
            string_list = ["Name", "Academic Institution", "Author Note", "Class", "Professor", "Date"]
            cleaner.remv_strings(string_list)
            
            #strip pars
            char1 = "("
            char2 = ")"
            cleaner.remv_slices(char1, char2)
        
            #strip quotes
            char1 = "\""
            char2 = "\""
            cleaner.remv_slices(char1, char2)

            #strip refs
            page_list = ["References", "Works Cited", "Bibliography"]
            cleaner.remv_pages(page_list)

            text = text + cleaner.get_text()
    else:
        print("not a path")
        raise SystemExit

    #send text for cleaning
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
    from generator import Generator
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
        #Generate text
        generator.gen_text(numwords, lines, temp)
        generated_text = generator.get_text()
    
        #Get length of generated text plus stored text
        len_check = len(text.split()) + len(generated_text.split())
        print(str(len_check) + " words generated...")
        old_len = len_check

        #Collect text and build sentence list
        cleaner.set_text(generated_text)
        cleaner.build_sentlist()

        #Clean text in sentence list
        cleaner.remv_nodeclare()
        cleaner.remv_nums()
        cleaner.remv_wtspc()
        cleaner.remv_noalead()
        cleaner.trim_sentlist(28, 140)
        cleaner.remv_language()
        
        #Format cleaned text list as string
        cleaner.frmt_textstring()
        cleaned_text = cleaner.get_text()
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

elif args.command == "cmd":
    commander = Commander()
    commander.cmd_mode()

else:
    print("command not found")
    print("use -h or --help for available commands")
 
