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

