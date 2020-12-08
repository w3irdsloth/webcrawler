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

    def set_sentlist(self, sent_list):
        self.sent_list = sent_list

    #Generate sentence list from text
    def build_sentlist(self):
        print("building sentence list...")
        pun_list = [".", "?", "!"]
        temp_text = ""
        for char in self.text:
            temp_text = temp_text + char
            if char in pun_list:
                self.sent_list.append(temp_text)
                temp_text = ""

    #Strip string from collected text   
    def strip_string(self, string):
        print("stripping string...")
        temp_text = self.text
        if string in temp_text:
            temp_text = temp_text.replace(string, "")
            self.text = temp_text
 
        else:
            print("string not found...")

    def strip_strings(self, string_list):
        for strng in string_list:
            while strng in self.text:
                self.strip_string(strng)

       
    #Strip slice from collected text
    def strip_slice(self, char1, char2):
        print("stripping slice...")
        temp_text = self.text
        if char1 in temp_text:
            try:
                slice_start = temp_text.find(char1)
                slice_end = temp_text.find(char2, slice_start + 1)
                temp_text = temp_text.replace(temp_text[slice_start:slice_end + 1], "")
                
                self.text = temp_text
        
            except:
                print("slice end not found")

        else:
            print("slice start not found")

    def strip_slices(self, char1, char2):
        for char1 in self.text:
            self.strip_slice(char1, char2)


    #Discard collected text that appears after the given string
    def strip_page(self, string):
        print("stripping page...")
        temp_text = self.text
        if string in temp_text:
            slice_start = temp_text.index(string)
            temp_text = temp_text[:slice_start]
            self.text = temp_text   
        
        else:
            print("page not found")

    def strip_pages(self, page_list):
        for pg in page_list:
            while pg in self.text:
                self.strip_page(pg)    
    
    #Trim sentence length in sentence list
    def trim_sentlist(self, sent_min, sent_max):
        print("trimming sentence list...")
        temp_list = []
        for sentc in self.sent_list:
            if len(sentc) >= sent_min and len(sentc) <= sent_max:
                temp_list.append(sentc)
                
        self.sent_list = temp_list

    #remove sentence from sentence list
    # def remv_sen(self, sent_num):
    #     try:
    #         self.sent_list.pop(sent_num - 1)
        
    #     except:
    #         print("sentence not found")

    #Remove sentences starting with non-alphabetical and lowercase characters
    def remv_noalead(self):
        print("checking leading characters...")
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

    #Remove non-declarative sentences
    def remv_nodeclare(self):
        for sentc in self.sent_list:
            if "?" in sentc or "!" in sentc:
                self.sent_list.remove(sentc)

    #Remove sentences with numbers
    def remv_nums(self):
        print("checking for numbers...")
        num_list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        for sentc in self.sent_list:
            for num in num_list:
                if num in sentc:
                    self.sent_list.remove(sentc)
                    break

    #Remove empty whitespace from sentences in list
    def remv_wtspc(self):
        print("cleaning whitespace...")
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

    #Fix spelling and grammar issues of sentences in list
    def fix_language(self):
        print("fixing spelling and grammar errors...")
        lang_tool = language_tool_python.LanguageTool('en-US')
        for sentc in self.sent_list:
            errors = lang_tool.check(sentc)
            if len(errors) > 0:
                error_index = self.sent_list.index(sentc)
                print(sentc)
                fix_sentc = lang_tool.correct(sentc)
                print(fix_sentc)
                self.sent_list[error_index] = fix_sentc

    #Remove sentences with spelling and grammar issues from list
    def remv_language(self):
        print("removing spelling and grammar errors...")
        lang_tool = language_tool_python.LanguageTool('en-US')
        for sentc in self.sent_list:
            errors = lang_tool.check(sentc)
            if len(errors) > 0:
                self.sent_list.remove(sentc)

    #Format cleaned text as list
    def frmt_textlist(self):
        print("formatting text as list...")
        temp_text = ""
        for sentc in self.sent_list:
            temp_text = temp_text + sentc
            temp_text = temp_text + "\n"
        
        self.text = temp_text

    #Format cleaned text as block
    def frmt_textblock(self, par_len):
        print("formatting text as block...")
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

        self.text = temp_text
