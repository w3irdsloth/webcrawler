     ##############
    ##  STRIPPER  ##
     ##############

class Stripper(object):
    """ Creates an object for stripping unwanted characters from text """
    def __init__(self):
        self.text= ""

    #Return collected text
    def get_text(self):
        return self.text

    def set_text(self, text):
        self.text = text

    #Strip string from collected text   
    def strip_string(self, string):
        print("\rstripping string...", end='')
        temp_text = self.text
        if string in temp_text:
            temp_text = temp_text.replace(string, "")
            self.text = temp_text
 
        else:
            print("\rstring not found...", end='')
       
    #Strip slice from collected text
    def strip_slice(self, char1, char2):
        print("\rstripping slice...", end='')
        temp_text = self.text
        if char1 in temp_text:
            try:
                slice_start = temp_text.find(char1)
                slice_end = temp_text.find(char2, slice_start + 1)
                temp_text = temp_text.replace(temp_text[slice_start:slice_end + 1], "")
                
                self.text = temp_text
        
            except:
                print("\rslice end not found", end='')

        else:
            print("\rslice start not found", end='')

    #Discard collected text that appears after the given string
    def strip_page(self, string):
        print("\rstripping page...", end='')
        temp_text = self.text
        if string in temp_text:
            slice_start = temp_text.index(string)
            temp_text = temp_text[:slice_start]
            self.text = temp_text   
        
        else:
            print("\rpage not found", end='')
        
