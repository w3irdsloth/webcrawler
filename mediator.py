

from modulator import Modulator

class Mediator(object):
    """ Creates an object for mediating user input """
    def __init__(self):
        self.input = ""
        self.check_list = []

    def get_input(self):
        return self.input

    def set_input(self):
        temp_input = input()
        self.input = temp_input

    def set_checklist(self, checklist):
        self.check_list = checklist

    def check_input(self, user_input):
        if user_input in self.check_list:
            return True

        else:
            return False

# mediator = Mediator()

# print("Input a command: ")
# mediator.set_input()

# user_input = mediator.get_input()
# print("Your command was: ")
# print(user_input)

# cmd_list = ["sometext", "apply_text", "some other text"]
# mediator.set_checklist(cmd_list)
# is_input = mediator.check_input("apply_text and some other test")
# print(is_input)
#importlib.import_module("modulator.apply_text")

modulator = Modulator()

modulator.set_functions()

functions = modulator.get_functions()
print(functions)

#attrs = modulator.get_attributes("extract_text")
#print(attrs)


