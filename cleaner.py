 ###########
## Cleaner ##
 ###########

import language_tool_python

class Cleaner(object):
    def __init__(self):
        self.text = ""
        self.sent_list = []

    def get_text(self):
        return self.text

    def set_text(self, text):
        self.text = text

    def get_sentlist(self):
        return self.sent_list

    #Generate sentence list from text
    def build_sentlist(self):
        print("Building sentence list...")
        pun_list = [".", "?", "!"]
        temp_text = ""
        for char in self.text:
            temp_text = temp_text + char
            if char in pun_list:
                self.sent_list.append(temp_text)
                temp_text = ""

    #Trim length of sentences in sentence list
    def trim_sentlist(self, sent_min, sent_max):
        print("Trimming sentence list...")
        temp_list = []
        for sentc in self.sent_list:
            if len(sentc) >= sent_min and len(sentc) <= sent_max:
                temp_list.append(sentc)
                
        self.sent_list = temp_list

    #remove sentence from sentence list
    def remv_sen(self, sent_num):
        try:
            self.sent_list.pop(sent_num - 1)
        
        except:
            print("Sentence not found")

    #Remove sentences starting with non-alphabetical and lowercase characters from sentences in list
    def remv_noalead(self):
        print("Checking leading characters...")
        temp_list = []
        alpha_list = ["A", "B", "C", "D", "E", "F", 
                        "G", "H", "I", "J", "K", "L", 
                        "M", "N", "O", "P", "Q", "R", 
                        "S", "T", "U", "V", "W", "X", 
                        "Y", "Z"]

        for sentc in self.sent_list:
            if sentc[0] in alpha_list:
                temp_list.append(sentc)

        self.sent_list = temp_list

    #Remove empty whitespace from sentences in list
    def remv_wtspc(self):
        print("Cleaning whitespace...")
        temp_list = []
        for sentc in self.sent_list:           
            sentc = sentc.strip()
            end_indx = len(sentc) - 1
            if sentc[end_indx] == " ":
                try:
                    sentc = sentc.replace(sentc[end_indx], "")
                except:
                    pass

            if sentc[end_indx - 1] == " ":
                try:
                    sentc = sentc[:end_indx - 1:end_indx]
                
                except:
                    pass
            
            if "\t" not in sentc:
                temp_list.append(sentc)

        self.sent_list = temp_list

    def fix_language(self):
        print("Fixing spelling and grammar errors...")
        lang_tool = language_tool_python.LanguageTool('en-US')
        for sentc in self.sent_list:
            errors = lang_tool.check(sentc)
            if len(errors) > 0:
                error_index = self.sent_list.index(sentc)
                print(sentc)
                fix_sentc = lang_tool.correct(sentc)
                print(fix_sentc)
                self.sent_list[error_index] = fix_sentc

    def remv_language(self):
        print("Removing spelling and grammar errors...")
        lang_tool = language_tool_python.LanguageTool('en-US')
        for sentc in self.sent_list:
            errors = lang_tool.check(sentc)
            if len(errors) > 0:
                self.sent_list.remove(sentc)

    #Print sentence list to .txt file formatted as a list
    def frmt_textlist(self):
        print("Formatting text as list...")
        temp_text = ""
        for sentc in self.sent_list:
            temp_text = temp_text + sentc
            temp_text = temp_text + "\n"
        
        return temp_text

    #Print sentences to .txt file formated as a block
    def frmt_textblock(self, par_len):
        print("Formatting text as block...")
        temp_text = "\t"
        text_check = ""
        par_check = 0
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

        return temp_text
