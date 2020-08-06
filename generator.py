 ###########
# Generator #
 ##########

from textgenrnn import textgenrnn

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
        print("Training weight...")
        textgen = textgenrnn()
        textgen.train_from_file(source, num_epochs=epochs)

    def gen_text(self, num_lines, temp):
        print("generating text...") 
        textgen = textgenrnn(self.weight)
        temp_text = textgen.generate(num_lines, temperature=temp, return_as_list=True)
        self.text = temp_text


##Generator Functions##

#Build generator object
generator = Generator()

#Build textgen object
textgen = textgenrnn()

#Set source and epochs
source = "/home/lux/Downloads/test/test.txt"
epochs=1

#Generate a new weight
generator.gen_weight(source, epochs)

#Set weight
weight = "textgenrnn_weights.hdf5"
generator.set_weight(weight)

#Generate text from weight
generator.gen_text(num_lines=1, temp=0.5)

#Get the generated text and print
text = generator.get_text()
print(text)
