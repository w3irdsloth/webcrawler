     ##############
    ##  MEDIATOR  ##
     ##############

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

