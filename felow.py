
    #################################
    ############  FELOW  ############
    #################################

import argparse
from commander import Commander

#Create parser
parser = argparse.ArgumentParser(description="filter arguments")

#Add arguments to parser
parser.add_argument("command")
parser.add_argument('-s', "--string",  action="store", dest="string")
parser.add_argument("-p", "--path", action="store", dest="path")
parser.add_argument("-t", "--type", action="store", dest="filetype") 
parser.add_argument("-f", "--filename", action="store", dest="filename") 
parser.add_argument("-i", "--integer", action="store",type=int, dest="integer")

parser.add_argument("-tmp", "--temperature", action="store", type=float, dest="temperature")
parser.add_argument("-epo", "--epochs", action ="store", type=int, dest="epochs")

#Set variables to parsed arguments
args = parser.parse_args()

string = args.string
path = args.path
filetype = args.filetype
filename = args.filename
integer = args.integer

temperature = args.temperature
epochs = args.epochs

#Build commander 
commander = Commander()

#Set argument commands
if args.command == "get_functions":
    functions = commander.get_functions()
    print(functions)

elif args.command == "get_attributes":
    attributes = commander.get_attributes(string)
    print(attributes)

elif args.command == "batch":
    commander.batch(path)

elif args.command == "build":
    commander.gen_weight(path, integer) 

elif args.command == "generate":
    commander.gen_text(integer, temperature, string) 

else: 
   print("command not found")

