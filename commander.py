     ##############
    ##  MEDIATOR  ##
     ##############
import random

class Commander(object):
    """ Creates an object for mediating user input """
    def __init__(self):
        self.greet_list = ["Hello!", "How are you today?", "What's going on?", "Greetings", "I'm here to help!", "How can I help?", "What?"]
        self.bye_list = ["Goodbye!", "Have a good one", "See ya!", "Later!", "Until next time...", "I'm always here to help!", "Finally..."] 
        self.list_index = 0
        self.input = ""

    def get_input(self):
        return self.input

    def set_input(self):
        greeting = self.greet_list[int(self.list_index)]
        self.input = input(greeting +": ")

    def set_index(self, index):
        self.list_index = index

    def get_index(self):
        return self.list_index

    def roll_index(self, index_list):
        self.list_index = random.randint(0, len(index_list) - 1)

    def cmd_mode(self):
        self.roll_index(self.greet_list)
        self.set_input()
        while True:
            temp_input = self.get_input()
            if temp_input == "q":
                self.roll_index(self.bye_list) 
                print(self.bye_list[self.list_index])
                break
           
            elif temp_input == "t":
                from datetime import datetime
                now = datetime.now()
                time = now.strftime("%I:%M:%S")
                print(time)

            elif temp_input == "d":
                from datetime import datetime
                now = datetime.now()
                date = now.strftime("%A %B,%d %Y")
                print(date)
                
            else:
                print("command not recognized")
               

            self.roll_index(self.greet_list)
            self.set_input()


                
