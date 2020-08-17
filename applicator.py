     ################
    ##  APPLICATOR  ##
     ################

class Applicator(object):
    """ Creates an object for applying text to a file """
    def __init__(self):
        self.text = ""

    def get_text(self):
        return self.text

    def set_text(self, text):
       self.text = text

    def apply_text(self, document):
        print("applying text...")
        try:
            with open(document, "a") as temp_file:
                temp_file.write(self.text)
                temp_file.close()

        except:
            print("text application failed")

