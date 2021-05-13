 ###########
## Builder ##
 ###########

import os

class Builder(object):
    """ Creates an object for building rnn architectures """
    
    #Build weight using textgenrnn
    def build_weight(self, source, epochs, gen_epochs, weight_name, is_new):
        print("importing rnn architecture...")
        from textgenrnn import textgenrnn
        textgen = textgenrnn()
        if is_new:
            try:
                print("training from file...")
                textgen.reset()
                textgen.train_from_file(source, num_epochs=epochs, gen_epochs=gen_epochs, new_model=True, train_size=0.8, dropout=0.2)

            except:
                return False

        else:
            try:
                print("training on texts")
                text = open(source, "r")
                text_list = text.read().splitlines()
                textgen.train_on_texts(text_list, num_epochs=epochs, gen_epochs=gen_epochs)


            except:
                return False
        
        textgen.save(weight_name)
        print("cleaning build directory...")
        os.remove("textgenrnn_weights.hdf5")
        return True



