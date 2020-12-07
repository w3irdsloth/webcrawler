           
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
from commander import Commander
from mediator import Mediator

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
generate.add_argument("-tmp", "--temp", action="store", dest="temp", type=float, default= 0.3)
generate.add_argument("-wgt", "--weight", action="store", dest="weight", required=True)
generate.add_argument("-tag", "--tag", action="store", dest="tag", default="<content>")
generate.add_argument("-f", "--filename", action="store", dest="filename", required=True)
generate.add_argument("-t", "--title", action="store", dest="title", default="Title")

#command mode subparsers
mediate = subparsers.add_parser(name="hlo")

#Get arguments
args = parser.parse_args()

#Construct commander
commander = Commander()

if args.command == "btc":
    #Batch text from documents to .txt file
    print("batching text...")
    path = args.path
    filename = args.filename
    text = ""
    extractor = commander.construct_extractor()
    stripper = commander.construct_stripper()
    for doc in os.listdir(path):
        temp_text = commander.extract_text(extractor, os.path.join(path, doc))
        #strip cover
        string_list = ["Name", "Academic Institution", "Author Note", "Class", "Professor", "Date"]
        temp_text = commander.strip_strings(stripper, temp_text, string_list)
        
        #strip pars
        char1 = "("
        char2 = ")"
        temp_text = commander.strip_slices(stripper, temp_text, char1, char2)
    
        #strip quotes
        char1 = "\""
        char2 = "\""
        temp_text = commander.strip_slices(stripper, temp_text, char1, char2)

        #strip refs
        page_list = ["References", "Works Cited", "Bibliography"]
        temp_text = commander.strip_pages(stripper, temp_text, page_list)

        text = text + temp_text

    #send text for cleaning
    cleaner = commander.construct_cleaner()
    text = commander.clean_text(cleaner, text)

    #Format text as list
    text = commander.format_list(cleaner, text)

    #apply text to .txt doc
    applicator = commander.construct_applicator()
    commander.apply_text(applicator, text, filename)

elif args.command == "bld":
    #Build weight from .txt file
    print("building weight...")
    filename = args.filename
    epochs = args.epochs
    numepochs = args.numepochs
    weightname = args.weightname
    builder = commander.construct_builder()
    commander.build_weight(builder, filename, epochs, numepochs, weightname)

elif args.command == "gen":
    #Generate document from weight
    print("generating document...")
    numwords = args.numwords
    lines = args.lines
    temp = args.temp
    weight = args.weight
    tag = args.tag
    filename = args.filename
    title = args.title
    
    len_check = 0 
    text = ""
    cleaner = commander.construct_cleaner()
    generator = commander.construct_generator()
    #Generate text in a loop
    while True:
        text_list = commander.gen_text(generator, lines, temp, weight)
        for sentc in text_list:
            text = text + sentc
            text = text + "  "

        len_check = len(text.split())
        print(str(len_check) + " words generated...")
        
        #Discard unwanted text
        if len_check >= numwords:
            disc_check = len_check
            text = commander.clean_text(cleaner, text)
            len_check = len(text.split())
            print(str(disc_check - len_check) + " words discarded...")

        #Break loop when word count reached
        if len_check >= numwords:
            break

    par_len = 175
    text = commander.format_block(cleaner, text, par_len)

    #Apply title to document
    documenter = commander.construct_documenter()
    commander.document_text(documenter, title, "Title", filename)
    
    #Apply generated text to document
    commander.document_text(documenter, text, tag, filename)
   

elif args.command == "hlo":
    mediator = Mediator()
    mediator.med_cmd()

else:
    print("command not found")
    print("use -h or --help for available commands")
 
