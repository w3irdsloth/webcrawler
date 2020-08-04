from modeler import *

class Builder(object):
    """ Creates a builder object for building weights from collected text """
    def __init__(self, model):
        self.model = model
        self.command = ""
        self.construct = model.rnn

    #Get command to be run by builder
    def get_command(self):
        return self.command

    #Set command to be run by builder
    def set_command(self, function, args):
        self.command = "self.construct" + function + args

    #Build weight from text file
    def build_weight(self):
        print("building weight...")
        try:
            print("Attempting weight command...")
            exec(self.command)

        except:
            print("Build failed...")



###Functions###

#Create a modeler
model = Modeler()

#Set model to textgenrnn
model.set_model("textgenrnn")

#Activate model
model.activate_model()

#Create builder and pass in model
builder = Builder(model)

#Set function and arguments
function = ".train_from_file"
args = "('/home/lux/Downloads/test/test.txt', 1)"

#Build command
builder.set_command(function, args)

#Print command
cmd = builder.get_command()
print(cmd)

#Build weight
builder.build_weight()

