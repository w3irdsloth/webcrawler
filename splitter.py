 ##############
##  SPLITTER  ##
 ##############

import os

class Splitter(object):
    """ Creates an object for splitting filetype extensions """
    def __init__(self):
        self.path = "no source"
        self.filename = "no source"
        self.name = "no source"
        self.ext = "no source"

    def split_source(self, source):
        print("splitting source...")
        try:
            split_name = os.path.split(source)
            split_ext = os.path.splitext(split_name[1])
            path = split_name[0]
            flname = split_name[1]  
            name = split_ext[0]
            ext = split_ext[1]
            self.path = path
            self.filename = flname
            self.name = name
            self.ext = ext
        
        except:
            print("split failed")

    def get_path(self):
        return self.path

    def get_flname(self):
        return self.filename

    def get_name(self):
        return self.name

    def get_ext(self):
        return self.ext



