 ###########
## Builder ##
 ###########

import os

class Builder(object):
    """Constructs an object for building rnn architectures."""
    
    def __init__(self):
        self.textgen = object

    def set_weights(self, weights_path, vocab_path, config_path):
        try:
            print("importing rnn architecture...")
            from textgenrnn import textgenrnn

            print("importing weights...")

            if config_path is not None and vocab_path is not None:
                self.textgen = textgenrnn(weights_path=weights_path, vocab_path=vocab_path, config_path=config_path)

            elif weights_path is not None:
                self.textgen = textgenrnn(weights_path=weights_path)

            else:
                self.textgen = textgenrnn()
        
        except:
            print("import failed")
            print("make sure valid weights are set")
            raise SystemExit

    
    #Build weight using textgenrnn
    def build_weights(self, source, epochs, gen_epochs, is_new):
        if is_new:
            try:
                print("training new weight from file...")
                self.textgen.reset()
                self.textgen.train_from_file(source, num_epochs=epochs, gen_epochs=gen_epochs, new_model=True, train_size=0.8, dropout=0.2)

            except:
                return False

        else:
            try:
                print("training weight on new texts")
                text = open(source, "r")
                text_list = text.read().splitlines()
                self.textgen.train_on_texts(text_list, num_epochs=epochs, gen_epochs=gen_epochs)

            except:
                return False
        
        return True



