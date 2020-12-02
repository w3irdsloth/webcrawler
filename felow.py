                ###########       
        ###########################    
      ###############################
     #################################
    #############  FELOW  #############
     #################################
      ###############################
        ###########################
                ###########        
                   
import argparse
import os
from commander import Commander

#Construct parsers
parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(title="commands", dest="command")

#batch parser
batch = subparsers.add_parser(name="btc")
batch.add_argument("-p", "--path", action="store", dest="path", required=True)
batch.add_argument("-f", "--filename", action="store", dest="filename", default="tmp.txt")

#build parser
build = subparsers.add_parser(name="bld")
build.add_argument("-p", "--path", action="store", dest="path", required=True)
build.add_argument("-epo", "--epochs", action="store", type=int, dest="epochs", required=True) 
build.add_argument("-i", "--integer", action="store",type=int, dest="integer", default=1)

#generate parser
generate = subparsers.add_parser(name="gen")
generate.add_argument("-num", "--numwords", action="store", dest="numwords", type=int, required=True)
generate.add_argument("-f", "--filename", action="store", dest="filename", required=True) 
generate.add_argument("-tag", "--tag", action="store", dest="tag", default="<content>")
generate.add_argument("-lns", "--lines", action="store", dest="lines", type=int, default=5)
generate.add_argument("-tmp", "--temp", action="store", dest="temp", type=float, default= 0.5)
generate.add_argument("-wgt", "--weight", action="store", dest="weight", default="textgenrnn_weights.hdf5")

#Get arguments
args = parser.parse_args()

#Construct commander
commander = Commander()

if args.command == "btc":
    print("text batcher selected...")
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

elif args.command == "bld":
    print("weight builder selected...")
    path = args.path
    epochs = args.epochs
    integer = args.integer
    commander.build_weight(path, epochs)

elif args.command == "gen":
    print("document generator selected...")
    numwords = args.numwords
    filename = args.filename
    tag = args.tag
    lines = args.lines
    temp = args.temp
    weight = args.weight

    len_check = 0 
    text = ""
    while len_check < numwords:
        text = text + commander.gen_text(lines, temp, weight)         
        len_check = len(text.split())
        print(str(len_check) + " words generated...")
        
    commander.document_text(text, tag, filename)

else:
    print("command not found")
    print("use -h or --help for available commands")
 
## Add cmd mode ##