 ###############
##  GENERATOR  ##
 ###############

class Generator(object):
    """ Creates an object for generating unique text with an rnn architecture  """
    def __init__(self):
        self.weight = ""
        self.text = ""

    def get_text(self):
        return self.text

    def get_weight(self):
        return self.weight

    def set_weight(self, weight):
        self.weight = weight

    def gen_weight(self, source, epochs):
        print("training weight...")
        from textgenrnn import textgenrnn
        textgen = textgenrnn()
        try:
            textgen.train_from_file(source, num_epochs=epochs)

        except:
            print("weight generation failed")

    def gen_text(self, num_lines, temp):
        print("generating text...") 
        from textgenrnn import textgenrnn
        textgen = textgenrnn(self.weight)
        try:
            temp_text = textgen.generate(num_lines, temperature=temp, return_as_list=True)
            self.text = temp_text
        
        except:
            print("text generation failed")

