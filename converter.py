##############################################################
# Strip text from documents to .txt for RNN machine learning #
##############################################################

class Converter(object):
    """ Creates a converter object for converting text from source documents to .txt files"""
    def __init__(self):
        self.text= ""

    #Get collected text
    def get_text(self):
        return self.text

    


converter = Converter()
text = converter.get_text()
print(text)
