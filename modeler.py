class Modeler(object):
    """ Creates an object for selecting and running a default rnn model """
    def __init__(self):
        self.model = "n/a"
        self.modlist = ["textgenrnn"]
        self.implist = []
        self.cmdkey = {}
        self.construct = "n/a"

    #Get current model
    def get_model(self):
        return self.model

    #Get list of available models
    def get_modlist(self):
        for mdl in self.modlist:
            return mdl

    #Get list of necessary imports
    def get_imports(self):
        for impt in self.implist:
            return impt

    #Get list of available commands
    def get_commands(self):
        return self.cmdkey

    #Get the construct for selected model
    def get_construct(self):
        return self.construct

    #Set current model
    def set_model(self, model):
        if  model == "textgenrnn":
            print("Selected textgenrnn...")
            self.model = model
            self.implist.append("from textgenrnn import textgenrnn")
            self.cmdkey[".train_from_file"] = ["source", "epochs"]
            self.construct = "textgenrnn()"

        else:
            print("Model not found")



#Construct model object
model = Modeler()

#Get selected model
modname=model.get_model()
print("Current model: ")
print(modname)
print("\n")

#Get list of models
modlist = model.get_modlist()
print("List of models: ")
print(modlist)
print("\n")

#Set a new model
model.set_model("textgenrnn")
modelname=model.get_model()
print(modelname)
print("\n")

#Get selected model
modname=model.get_model()
print("Current model: ")
print(modname)
print("\n")

#Get list of imports
implist = model.get_imports()
print("List of imports: ")
print(implist)
print("\n")

#Get list of commands
cmdlist = model.get_commands()
print("List of commands: ")
print(cmdlist)
print("\n")

#Get the constructor
construct = model.get_construct()
print("Constructor: ")
print(construct)
print("\n")

