 #############
## Formatter ##
 #############

class Formatter(object):
    """ Creates an object for formatting text lists """
    def _init_(self):
        self.text = ""
        self.sent_list = []

    def get_text(self):
        return self.text

    def set_sentlist(self, sent_list):
        self.sent_list = sent_list

    #Format sentence list as string
    def frmt_textstring(self):
        print("formatting text as string...")
        temp_text = ""
        try:
            for sentc in self.sent_list:
                temp_text = temp_text + sentc
                temp_text = temp_text + " "
            
            self.text = temp_text

        except:
            print("error, no text formatted")

    
    #Format sentence list as text list
    def frmt_textlist(self):
        print("formatting text as list...")
        temp_text = ""
        try:
            for sentc in self.sent_list:
                temp_text = temp_text + sentc
                temp_text = temp_text + "\n"
            
            self.text = temp_text

        except:
            print("error, no text formatted")


    #Format sentence list as text block
    def frmt_textblock(self, par_len):
        print("formatting text as block...")
        temp_text = "\t"
        text_check = ""
        par_check = 0
        try:
            for sentc in self.sent_list:
                temp_text = temp_text + sentc
                temp_text = temp_text + "  "
            
                text_check = text_check + sentc
                text_check = text_check + "  "
                par_check = len(text_check.split())
                if par_check >= par_len:
                    temp_text = temp_text + "\n"
                    temp_text = temp_text + "\t"
                    text_check = ""

            self.text = temp_text

        except:
            print("error, no text formatted")

    def frmt_references(self, ref_list, style):
        if style == "MLA":
            template = "<author>. <title>. <subject>. <date>. <file>. \n"
        elif style == "APA":
            template = "<author>. (<date>). <title>. <subject>. <file>. \n"

        template_list = []
        for ref_dict in ref_list:
            temp_string = template
            if "file" in ref_dict:
                temp_string = temp_string.replace("<file>", ref_dict["file"])
            
            if "author" in ref_dict:
                temp_string = temp_string.replace("<author>", ref_dict["author"])

            if "title" in ref_dict:
                temp_string = temp_string.replace("<title>", ref_dict["title"])

            if "subject" in ref_dict:
                temp_string = temp_string.replace("<subject>", ref_dict["subject"])

            if "date" in ref_dict:
                temp_string = temp_string.replace("<date>", ref_dict["date"])

            template_list.append(temp_string)
        
        return template_list





    


