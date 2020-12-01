    #################################
    ############  FELOW  ############
    #################################

import argparse
import os
from commander import Commander

#Construct parsers
parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(title="commands", dest="command")

#Batch parser
batch = subparsers.add_parser(name="batch")
batch.add_argument("-p", "--path", action="store", dest="path", required=True)
batch.add_argument("-f", "--filename", action="store", dest="filename", default="tmp.txt") 

#Batchall parser
batchall = subparsers.add_parser(name="batchall")
batchall.add_argument("-p", "--path", action="store", dest="path", required=True)
batchall.add_argument("-f", "--filename", action="store", dest="filename", default="tmp.txt") 

#Build parser
build = subparsers.add_parser(name="bld")
build.add_argument("-p", "--path", action="store", dest="path", required=True)
build.add_argument("-epo", "--epochs", action="store", type=int, dest="epochs", required=True) 
build.add_argument("-i", "--integer", action="store",type=int, dest="integer", default=1)

#Docgen parser
docgen = subparsers.add_parser(name="docgen")
docgen.add_argument("-num", "--numwords", action="store", dest="numwords", type=int, required=True)
docgen.add_argument("-f", "--filename", action="store", dest="filename", required=True) 
docgen.add_argument("-tag", "--tag", action="store", dest="tag", default="<content>")
docgen.add_argument("-lns", "--lines", action="store", dest="lines", type=int, default=5)
docgen.add_argument("-tmp", "--temp", action="store", dest="temp", type=float, default= 0.5)
docgen.add_argument("-wgt", "--weight", action="store", dest="weight", default="textgenrnn_weights.hdf5")

#btc parser
btc = subparsers.add_parser(name="btc")
btc.add_argument("-p", "--path", action="store", dest="path", required=True)
btc.add_argument("-f", "--filename", action="store", dest="filename", default="tmp.txt")

#Get arguments
args = parser.parse_args()

#Construct commander
commander = Commander()

#Set command arguments
if args.command == "batch":
    print("batch command selected...")
    path = args.path
    filename = args.filename
    commander.batch(path, filename)  

elif args.command == "batchall":
    print("batchall selected...")
    path = args.path
    filename = args.filename
    commander.batch_all(path, filename)

elif args.command == "bld":
    print("build selected...")
    path = args.path
    epochs = args.epochs
    integer = args.integer
    commander.build_weight(path, epochs)

elif args.command == "docgen":
    print("docgen selected...")
    numwords = args.numwords
    filename = args.filename
    tag = args.tag
    lines = args.lines
    temp = args.temp
    weight = args.weight
    commander.gen_doc(numwords, filename, tag, lines, temp, weight)

elif args.command == "btc":
    print("batch selected...")
    path = args.path
    filename = args.filename
    text = ""
    for doc in os.listdir(path):
        temp_text = commander.extract_text(os.path.join(path, doc))
        #strip cover
        string_list = ["Name", "Academic Institution", "Author Note", "Class", "Professor", "Date"]
        temp_text = commander.strip_strings(temp_text, string_list)
        
        #strip pars
        char1 = "("
        char2 = ")"
        temp_text = commander.strip_slices(temp_text, char1, char2)
    
        #strip quotes
        char1 = "\""
        char2 = "\""
        temp_text = commander.strip_slices(temp_text, char1, char2)

        #strip refs
        page_list = ["References", "Works Cited", "Bibliography"]
        temp_text = commander.strip_pages(temp_text, page_list)

        text = text + temp_text

    #send text for cleaning
    text = commander.clean_text(text)

    #apply text to .txt doc
    commander.apply_text(text, "tmp.txt")



else:
    print("command not found")
    print("use -h or --help for available commands")
 
## Add btc, bld, gen, and cmd modes ##