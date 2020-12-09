     ############### 
    ##  GENERATOR  ##
     ###############

class Generator(object):
    """ Creates an object for generating unique text with an rnn architecture  """
    def __init__(self):
        self.weight = ""
        self.text_list = []
        self.text = ""
        self.textgen = object

    def get_text(self):
        return self.text

    def get_text_list(self):
        return self.text_list

    def get_weight(self):
        return self.weight

    def set_weight(self, weight):
        try:
            print("\nimporting rnn architecture...")
            from textgenrnn import textgenrnn

            print("\nimporting weight...")
            self.textgen = textgenrnn(weight)
        
        except:
            print("import failed")
            print("make sure a valid weight is set")
            raise SystemExit

    #Generate text list using textgenrnn
    def gen_text(self, num_words, num_lines, temp):
        len_check = len(self.text)
        
        
        while len_check < num_words:
            print("generating text...")
            temp_textlist = self.textgen.generate(num_lines, temperature=temp, return_as_list=True)
            self.text_list = self.text_list + temp_textlist
            self.cnvrt_text()
            temp_text = self.text
            len_check = len(temp_text.split())
            print(str(len_check) + " words generated...")

    #Convert text list to string
    def cnvrt_text(self):
        temp_text = ""
        for txt in self.text_list:
            temp_text = temp_text + txt
            temp_text = temp_text + " "
            self.text = temp_text