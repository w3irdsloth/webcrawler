from modeler import *

class Builder(object):
    """ Creates a builder object for building weights from collected text """
    def __init__(self, model):
        self.model = model
        self.rnn = model.get_constructor()
        self.construct = "rnn"
        self.build_command = ""
        model.activate_model()

    #Get command to be run by builder
    def get_command(self):
        return self.build_command

    #Set command to be run by builder
    def set_command(self, function, args):
        self.build_command = self.construct + function + "(" + args + ")"


    #Build weight from text file
    def build_weight(self):
        print("building weight...")
        try:
            print("Attempting weight command...")
            exec(self.build_command)

        except:
            print("Build failed...")


#Create a modeler
model = Modeler()

#Set model to textgenrnn
model.set_model("textgenrnn")

#Get and print the model name
#modelname=model.get_model()
#print(modelname)

#Activate model
model.activate_model()

#Construct selected model
rnn = model.get_constructor()

#rnn.train_from_file("/home/lux/Downloads/test/test.txt", 1)

#Create builder and pass in model
builder = Builder(model)

#command = ".train_from_file("/home/lux/Downloads/test/test.txt", 1)"

cmd = builder.get_command()
print(cmd)


#builder.set_command('.train_from_file(/home/lux/Downloads/test/test.txt, 1)")
cmd = builder.get_command()
print(cmd)

builder.build_weight()


#Get list of functions available
#fncs = builder.get_functions()
#print(fncs)

#Get paremeters for a selected function
#parms = builder.get_parms(".train_from_file")
#print(parms)

#import necessary dependencies
#builder.import_deps()

#exec model.get_constructor()

#textgen = textgenrnn()

#construct = eval(model.get_constructor())

#construct.train_from_file("/home/lux/Downloads/test/test.txt", 1)

#exec(rnn)
#print(rnn)
#rnn.train_from_file("/home/lux/Downloads/test/test.txt", 1)

#Build weight
#builder.build_weight(".train_from_file('/home/lux/Downloads/test/test.txt)', 1")
