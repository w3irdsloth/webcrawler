     ############### 
    ##  GENERATOR  ##
     ###############

from textgenrnn import textgenrnn

class Generator(object):
    """ Creates an object for generating unique text with an rnn architecture  """
    def __init__(self):
        self.weight = ""
        self.text_list = []
        self.text = ""

    def get_text(self):
        return self.text

    def get_text_list(self):
        return self.text_list

    def get_weight(self):
        return self.weight

    def set_weight(self, weight):
        self.weight = weight

    #Convert text list to string
    def cnvrt_text(self):
        temp_text = ""
        for txt in self.text_list:
            temp_text = temp_text + txt
            temp_text = temp_text + " "
            self.text = temp_text

    #Generate text list using textgenrnn
    def gen_text(self, num_lines, temp):
        try:
            print("generating text...")
            textgen = textgenrnn(self.weight)
            temp_textlist = textgen.generate(num_lines, temperature=temp, return_as_list=True)
            self.text_list = temp_textlist
        
        except:
            print("text generation failed")
            print("ensure a weight is available")
            raise SystemExit
