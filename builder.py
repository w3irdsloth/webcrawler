     ###########
    ## Builder ##
     ###########

class Builder(object):
    """ Creates an object for building rnn architectures """
    def __init__(self):
        self.weight = ""

    def build_weight(self, source, epochs):
        print("training weight...")
        from textgenrnn import textgenrnn
        textgen = textgenrnn()
        try:
            textgen.train_from_file(source, num_epochs=epochs)

        except:
            print("weight generation failed")
