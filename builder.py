     ###########
    ## Builder ##
     ###########

class Builder(object):
    """ Creates an object for building rnn architectures """
    def __init__(self):
        self.weight = ""

    #Build weight using textgenrnn
    def build_weight(self, source, epochs, gen_epochs, weight_name):
        print("training weight...")
        from textgenrnn import textgenrnn
        textgen = textgenrnn()
        try:
            textgen.train_from_file(source, num_epochs=epochs, gen_epochs=gen_epochs)
            textgen.save(weight_name)

        except:
            print("weight generation failed")
