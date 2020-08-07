    #################################
    ############  FELOW  ############
    #################################

import argparse
from commander import Commander


#Create parser
parser = argparse.ArgumentParser(description="filter arguments")

#Create functions
parser.add_argument("command")
parser.add_argument('-s', "--string",  action="store", dest="string")
parser.add_argument("-p", "--path", action="store", dest="path")
parser.add_argument("-t", "--type", action="store", dest="filetype") 
parser.add_argument("-f", "--filename", action="store", dest="filename") 

#Set variables to parsed arguments
args = parser.parse_args()

string = args.string
path = args.path
filetype = args.filetype
filename = args.filename

#Build commander 
commander = Commander()

if args.command == "get_functions":
    functions = commander.get_functions()
    print(functions)

elif args.command == "get_attributes":
    attributes = commander.get_attributes(string)
    print(attributes)

elif args.command == "batch":
    commander.batch(path)

# elif args.command == "batch_doc":
#     commander.batch_doc(path)

else: 
   print("command not found")

