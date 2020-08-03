class Modeler(object):
    """ Creates an object for selecting and running a default rnn model """
    def __init__(self):
        self.model = "n/a"
        self.modlist = ["textgenrnn"]
        self.implist = []
        self.fnckey = []
        self.constructor = "n/a"

    #Get current model
    def get_model(self):
        return self.model

    #Get list of available models
    def get_modlist(self):
        return self.modlist

    #Get list of necessary imports for selected model
    def get_imports(self):
        return self.implist

    #Get list of available commands for selected model
    def get_functions(self):
        return self.fnckey

    #Get constructor for selected model
    def get_constructor(self):
        return self.constructor

    #Set current model
    def set_model(self, model):
        if  model in self.modlist:
            print("Selected " + model + "...")
            self.model = model

        else:
            print("Model not found")

    #Activate current model
    def activate_model(self):
        model = self.model
        if model == "textgenrnn":
            self.implist = ["textgenrnn"]
            from textgenrnn import textgenrnn
            self.fnckey.append(".train_from_file(source, epochs)")
            self.constructor = textgenrnn()

        else:
            print("No active model found")

    #import new model
    #def import_model(self, model):
    #    self.modlist.append(model)



####Functions####

#Construct model object
#model = Modeler()

#Get selected model
#modname=model.get_model()
#print("Current model: ")
#print(modname)
#print("\n")

#Get list of models
#modlist = model.get_modlist()
#print("List of models: ")
#print(modlist)
#print("\n")

#Set a new model
#model.set_model("textgenrnn")
#modelname=model.get_model()
#print(modelname)
#print("\n")

#Get selected model
#modname=model.get_model()
#print("Current model: ")
#print(modname)
#print("\n")

#Get list of imports
#implist = model.get_imports()
#print("List of imports: ")
#print(implist)
#print("\n")

#Get list of commands
#cmdlist = model.get_commands()
#print("List of commands: ")
#print(cmdlist)
#print("\n")

#Get the constructor
#construct = model.get_constructor()
#print("Constructor: ")
#print(construct)
#print("\n")

