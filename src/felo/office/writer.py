 ##############
## Applicator ##
 ##############

import os
from os.path import splitext, isfile

class Writer(object):
    """ Write text to files """

    def write_txt(self, txt_name, txt_content):
        if os.path.isfile(txt_name):
            print("file exists")
            return False
        
        else:
            try:
                with open(txt_name, 'w') as f:
                    f.write(txt_content)
                    f.close()
                    return True
                
            except:
                print("something went wrong")
                return False

    def append_txt(self, txt_name, txt_content):
        if os.path.isfile(txt_name):
            try:
                with open(txt_name, 'a') as f:
                    f.write(txt_content)    
                    f.close()
                    return True
                
            except:
                print("something went wrong")
                return False
            
        else:
            print("file doesn't exist")
            return False
        

    def save_txt(self, txt_name, txt_content):
        if self.append_txt(txt_name, txt_content):
            return True
        
        elif self.write_txt(txt_name, txt_content):
            return True
        
        else:
            return False
