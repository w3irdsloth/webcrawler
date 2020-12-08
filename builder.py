     ###########
    ## Builder ##
     ###########

import os

class Builder(object):
    """ Creates an object for building rnn architectures """
    def __init__(self):
        self.weight = ""

    #Build weight using textgenrnn
    def build_weight(self, source, epochs, gen_epochs, weight_name):
        print("importing rnn architecture...")
        from textgenrnn import textgenrnn
        textgen = textgenrnn()
        try:
            print("training from file...")
            textgen.train_from_file(source, num_epochs=epochs, gen_epochs=gen_epochs)
            textgen.save(weight_name)

        except:
            print("training failed")

        try:
            print("cleaning build directory...")
            os.remove("textgenrnn_weights.hdf5")
        
        except:
            pass