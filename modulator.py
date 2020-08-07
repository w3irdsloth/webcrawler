     ###############
    ##  MODULATOR  ##
     ###############

from commander import Commander

class Modulator(object):
    """ Creates an object for modulating command functions """
    def __init__(self):
        self.commander = ""
        self.functions = [] 

    def get_commander(self, commander):
        self.commander = commander

    def get_functions(self):
        return self.functions

    def get_attributes(self, function):
        return getattr(Commander, function).__doc__

    def set_functions(self):
        functions = []
        for attr in dir(Commander):
            if callable(getattr(Commander, attr)) and "__" not in attr:
                functions.append(attr)

        self.functions = functions


#Modulator functions#

# modulator = Modulator()

# commander = Commander

# modulator.get_commander(commander)

# modulator.set_functions()

# functions = modulator.get_functions()
# print(functions)

# attrs = modulator.get_attributes("extract_text")
# print(attrs)

