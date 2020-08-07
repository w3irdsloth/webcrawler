     ###############
    ##  MODULATOR  ##
     ###############

from commander import Commander

class Modulator(object):
    """ Creates an object for modulating function calls """
    def __init__(self):
        self.functions = [] 

    def get_functions(self):
        return self.functions

    def get_attributes(self, function):
        return getattr(Modulator, function).__doc__

    def set_functions(self):
        functions = []
        for attr in dir(Commander):
            if callable(getattr(Commander, attr)) and "__" not in attr:
                functions.append(attr)

        self.functions = functions


