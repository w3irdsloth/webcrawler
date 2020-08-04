class Modeler(object):
    """ Creates an object for selecting and running a default rnn model """
    def __init__(self):
        self.model = "n/a"
        self.mod_list = ["textgenrnn"]
        self.fun_key = {"textgenrnn": {".train_from_file": ["source", "epochs"]}
                }
        self.rnn = ""

    #Get current nodel
    def get_model(self):
        return self.model

    #Get list of available models
    def get_modlist(self):
        return self.mod_list

    #Get list of available commands for selected model
    def get_functions(self, model):
        return self.fun_key.get(model)

    #Set model
    def set_model(self, model):
        if  model in self.mod_list:
            print(model + " selected...")
            self.model = model

        else:
            print("Model not found")

    def activate_model(self):
        if self.model == "textgenrnn":
            print("textgenrnn activated...")
            from textgenrnn import textgenrnn
            self.rnn = textgenrnn()

        else:
            print("Model not found")

####Functions####

#Construct model object
model = Modeler()

#Get selected model
#modname=model.get_model()
#print("Current model: )
#print(modname)

#Get list of models
#modlist = model.get_modlist()
#print("List of models: ")
#print(modlist)

#Set a new model
model.set_model("textgenrnn")
#modelname=model.get_model()
#print(modelname)


model.activate_model()


#Get list of imports
#implist = model.get_imports("textgenrnn")
#print("List of imports: ")
#print(implist)

#Get list of commands
#cmdlist = model.get_functions("textgenrnn")
#print("List of commands: ")
#print(cmdlist)

#Get list of constructors
#constructs = model.get_constructors()
#print("Constructors: ")
#print(constructs)

#Update models from file
#model.update_models()

