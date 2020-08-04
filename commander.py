from modeler import *

class Commander(object):
    """ Creates an object for unpacking and executing commands """
    def __init__(self, model):
        self.model = model
        self.command = ""
        self.construct = model.construct

    #Get command to be run by builder
    def get_command(self):
        return self.command

    #Set command to be run by builder
    def set_command(self, function, args):
        self.command = "self.construct" + function + args

    #Build weight from text file
    def execute_command(self):
        try:
            print("attempting to execute...")
            exec(self.command)

        except:
            print("command failed...")



###Functions###

#Create a modeler
model = Modeler()

#Set model to textgenrnn
model.set_model("textgenrnn")

#Activate model
model.activate_model()

#Create builder and pass in model
commander = Commander(model)

#Set function and arguments
function = ".train_from_file"
args = "('/home/lux/Downloads/test/test.txt', 1)"

#Build command
commander.set_command(function, args)

#Print command
cmd = commander.get_command()
print(cmd)

#Build weight
commander.execute_command()

