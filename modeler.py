import models

class Modeler(object):
    """ Creates an object for selecting and running a default rnn model """
    def __init__(self):
        self.model = "n/a"
        self.mod_list = models.mod_list 
        self.imp_key = models.imp_key
        self.fun_key = models.fun_key
        self.constructors = models.con_key
 
    #Get current model
    def get_model(self):
        return self.model

    #Get list of available models
    def get_modlist(self):
        return self.mod_list

    #Get list of necessary imports for a model
    def get_imports(self, model):
        return self.imp_key.get(model)

    #Get list of available commands for selected model
    def get_functions(self, model):
        return self.fun_key.get(model)

    #Get constructor for selected model
    def get_constructor(self):
        return self.constructors

    #Set current model
    def set_model(self, model):
        if  model in self.mod_list:
            print("Selected " + model + "...")
            self.model = model

        else:
            print("Model not found")

    def update_models(self):
        print("Updating model...")
        self.mod_list = models.mod_list 
        self.imp_key = models.imp_key
        self.fun_key = models.fun_key
        self.constructors = models.con_key

    #Activate current model
    def activate_model(self):
        model = self.model


####Functions####

#Construct model object
model = Modeler()

#Get selected model
modname=model.get_model()
print("Current model: ")
print(modname)
#print("\n")

#Get list of models
modlist = model.get_modlist()
print("List of models: ")
print(modlist)
#print("\n")

#Set a new model
model.set_model("textgenrnn")
modelname=model.get_model()
print(modelname)
#print("\n")

#Get selected model
#modname=model.get_model()
#print("Current model: ")
#print(modname)
#print("\n")

#Get list of imports
implist = model.get_imports("textgenrnn")
print("List of imports: ")
print(implist)
#print("\n")

#Get list of commands
cmdlist = model.get_functions("textgenrnn")
print("List of commands: ")
print(cmdlist)
#print("\n")

#Get the constructor
#construct = model.get_constructor()
#print("Constructor: ")
#print(construct)
#print("\n")

