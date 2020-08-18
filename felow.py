    #################################
    ############  FELOW  ############
    #################################

import argparse
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
build = subparsers.add_parser(name="build")
build.add_argument("-p", "--path", action="store", dest="path", required=True)
build.add_argument("-i", "--integer", action="store",type=int, dest="integer", required=True)

#Docgen parser
docgen = subparsers.add_parser(name="docgen")
docgen.add_argument("-num", "--numwords", action="store", dest="numwords", type=int, required=True)
docgen.add_argument("-f", "--filename", action="store", dest="filename", required=True) 
docgen.add_argument("-tag", "--tag", action="store", dest="tag", default="<tag>")
docgen.add_argument("-lns", "--lines", action="store", dest="lines", type=int, default=1)
docgen.add_argument("-tmp", "--temp", action="store", dest="temp", type=float, default= 0.5)
docgen.add_argument("-wgt", "--weight", action="store", dest="weight", default="textgenrnn_weights.hdf5")

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

elif args.command == "build":
    print("build selected...")
    path = args.path
    integer = args.integer
    commander.gen_weight(path, integer) 

elif args.command == "docgen":
    print("docgen selected...")
    numwords = args.numwords
    filename = args.filename
    tag = args.tag
    lines = args.lines
    temp = args.temp
    weight = args.weight
    commander.gen_doc(numwords, filename, tag, lines, temp, weight) 

else:
    print("command not found")
