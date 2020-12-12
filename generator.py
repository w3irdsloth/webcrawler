     ############### 
    ##  GENERATOR  ##
     ###############

class Generator(object):
    """ Creates an object for generating unique text with an rnn architecture  """
    def __init__(self):
        self.weight = ""
        self.text_list = []
        self.textgen = object
        self.gen_loop = True

    def get_text_list(self):
        return self.text_list

    #Set RNN weight for generating text 
    def set_weight(self, weight):
        try:
            print("importing rnn architecture...")
            from textgenrnn import textgenrnn

            print("importing weight...")
            self.textgen = textgenrnn(weight)
        
        except:
            print("import failed")
            print("make sure a valid weight is set")
            raise SystemExit

    #Generate text list using selected RNN weight
    def gen_text(self, num_words, num_lines, temp):
        print("generating text...")
        len_check = 0
        self.text_list = []
        while len_check < num_words:
            temp_textlist = self.textgen.generate(num_lines, temperature=temp, return_as_list=True)
            self.text_list = self.text_list + temp_textlist
            len_check = self.get_textlength()
            print(str(len_check) + " words generated...")

    def get_textlength(self):
        len_check = 0
        for txt in self.text_list:
            len_check += len(txt.split())
        
        return len_check