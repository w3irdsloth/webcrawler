import sys
from modeler import *

class Builder(object):
    """ Creates a builder object for building weights from collected text """
    def __init__(self, model):
        self.model = model
        self.constructors = model.get_constructors()
        self.imports = model.get_imports(model.get_model())


    #Get command to be run by builder
    def get_command(self):
        return self.build_command

    #Set command to be run by builder
    #def set_command(self, function, args):
    #    self.build_command = self.construct + function + "(" + args + ")"

    #Import dependencies for selected model
    def import_deps(self):
        imp_list = self.imports
        for cmd in imp_list:
            exec(cmd)

    #Build weight from text file
    def build_weight(self):
        print("building weight...")
        try:
            print("Attempting weight command...")
            #exec(self.build_command)

        except:
            print("Build failed...")

#Functions

#Create a modeler
model = Modeler()

#Set model to textgenrnn
model.set_model("textgenrnn")

#rnn.train_from_file("/home/lux/Downloads/test/test.txt", 1)

#Create builder and pass in model
builder = Builder(model)

builder.import_deps()

if "textgenrnn" in sys.modules:
    rnn = textgenrnn()

#builder.build_model()

#from textgenrnn import textgenrnn
#string = "rnn = builder.build_model()"
#exec(string)
#print(rnn)
#command = "rnn.train_from_file('/home/lux/Downloads/test/test.txt', 1)"
#exec(command)
#exec("rnn.train_from_file('/home/lux/Downloads/test/test.txt', 1)")


#command = ".train_from_file("/home/lux/Downloads/test/test.txt", 1)"


#builder.set_command('.train_from_file(/home/lux/Downloads/test/test.txt, 1)")
#cmd = builder.get_command()
#print(cmd)

#builder.build_weight()

