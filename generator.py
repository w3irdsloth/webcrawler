from modeler import *

class Generator(object):
    """ Creates an object for generating unique text from a weight file """
    def __init__(self, model):
        self.model = model
        self.command = ""
        self.construct = model.rnn

    #Get command to be run by generator
    def get_command(self):
        return self.command

    #Set command to be run by generator
    def set_command(self, function, args):
        self.command = "self.construct" + function + args

    #Generate text from weight file
    print("generating text...")
    try:
        print("Attempting text command...")
        
    
    except:
        print("generation failed...")
