 ############
# Applicator #
 ############

class Applicator(object):
    """ Creates an object for applying text to a file """
    def __init__(self):
        self.text = ""
    
    def get_text(self):
        return self.text

    def set_text(self, text):
       self.text = text

    def apply_text(self, docname):
        with open(docname, "a") as temp_file:
            temp_file.write(self.text)

            temp_file.close()

##Applicator Functions##

text = """ Here is a test string """

applicator = Applicator()

applicator.set_text(text)

#my_text = applicator.get_text()

#print(my_text)

applicator.apply_text("mydoc.txt")

