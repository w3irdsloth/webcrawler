import commandmods

class Modulator(object):
    """ Creates an object for selecting and running command modules """
    def __init__(self):
        self.module = "none"
        self.mod_list = commandmods.mod_list
        self.fun_key = commandmods.fun_list 

    #Get selected`module
    def get_module(self):
        return self.module

    #Get list of available modules`
    def get_modlist(self):
        return self.mod_list

    #Get functions for a module
    def get_function(self, module):
        return self.fun_key

    #Set module
    def set_module(self, module):
        if  module in self.mod_list:
            print(module + " selected...")
            self.module = module

        else:
            print("Module not found")

    def activate_module(self):
        print(commandmods.mod_list)
        commandmods.activate_module(self.module)
            


####Functions####

#Construct model object
module = Modulator()

#Get selected model
modname=module.get_module()
print("Current model:" )
print(modname)

#Get list of models
modlist = module.get_modlist()
print("List of models: ")
print(modlist)

#Set a new model
module.set_module("textgenrnn")

modulename=module.get_module()
print(modulename)

#Activate the selected model
module.activate_module()

#Get a list of functions for a given model
fncts = module.get_function(module)
print(fncts)

#Update models
#model.update_models()

