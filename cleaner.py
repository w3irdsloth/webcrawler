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

    #Strip string from collected text   
    def remv_string(self, string):
        print("removing string...")
        temp_text = self.text
        if string in temp_text:
            temp_text = temp_text.replace(string, "")
            self.text = temp_text
 
        else:
            print("string not found...")

    def remv_strings(self, string_list):
        for strng in string_list:
            while strng in self.text:
                self.remv_string(strng)

       
    #Strip slice from collected text
    def remv_slice(self, char1, char2):
        print("removing slice...")
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

    def remv_slices(self, char1, char2):
        for char1 in self.text:
            self.remv_slice(char1, char2)


    #Discard collected text that appears after the given string
    def remv_page(self, string):
        print("removing page...")
        temp_text = self.text
        if string in temp_text:
            slice_start = temp_text.index(string)
            temp_text = temp_text[:slice_start]
            self.text = temp_text   
        
        else:
            print("page not found")

    def remv_pages(self, page_list):
        for pg in page_list:
            while pg in self.text:
                self.remv_page(pg) 
    
    #Generate sentence list from collected text
    def build_sentlist(self):
        print("building sentence list...")
        pun_list = [".", "?", "!"]
        temp_text = ""
        temp_list = []
        for char in self.text:
            temp_text = temp_text + char
            if char in pun_list:
                temp_list.append(temp_text)
                temp_text = ""

        self.sent_list = temp_list   
    
    #Remove sentences that don't begin with uppercase letters from sentence list
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

    #Remove sentences with extra capital letters
    def remv_excap(self):
        alpha_list = ["A", "B", "C", "D", "E", "F", 
                        "G", "H", "J", "K", "L", "M", 
                        "N", "O", "P", "Q", "R", "S", 
                        "T", "U", "V", "W", "X", "Y", 
                        "Z"]
        
        for sentc in self.sent_list:
            for char in alpha_list:
                if char in sentc[1:]:
                    try:
                        self.sent_list.remove(sentc)
    
                    except:
                        break

    #Remove sentences with numbers from sentence list
    def remv_nums(self):
        print("checking for numbers...")
        num_list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        for sentc in self.sent_list:
            for num in num_list:
                if num in sentc:
                    try:
                        self.sent_list.remove(sentc)
                    
                    except:
                        break

    #Remove non-declarative sentences from sentence list
    def remv_nodeclare(self):
        for sentc in self.sent_list:
            if "?" in sentc or "!" in sentc:
                try:
                    self.sent_list.remove(sentc)
                
                except:
                    break

    #Remove empty whitespace from sentences in sentence list
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

    #Fix spelling and grammar errors in sentence list
    def fix_language(self):
        print("fixing spelling and grammar errors...")
        lang_tool = language_tool_python.LanguageTool('en-US')
        for sentc in self.sent_list:
            errors = lang_tool.check(sentc)
            for err in errors:
                try:
                    error_index = self.sent_list.index(sentc)
                    fix_sentc = lang_tool.correct(sentc)
                    self.sent_list[error_index] = fix_sentc
                    errors.remove(err)

                except:
                    break


    #Remove sentences with spelling and grammar errors from sentence list
    def remv_language(self):
        print("removing spelling and grammar errors...")
        lang_tool = language_tool_python.LanguageTool('en-US')
        for sentc in self.sent_list:
            errors = lang_tool.check(sentc)
            for err in errors:
                try:
                    self.sent_list.remove(sentc)
                    errors.remove(err)

                except:
                    break            

    #Remove sentences in sentence list based on sentence length
    def trim_sentlist(self, sent_min, sent_max):
        print("trimming sentence list...")
        temp_list = []
        for sentc in self.sent_list:
            if len(sentc) >= sent_min and len(sentc) <= sent_max:
                temp_list.append(sentc)
                
        self.sent_list = temp_list

    #Format sentence list as string
    def frmt_textstring(self):
        print("formatting text as string...")
        temp_text = ""
        for sentc in self.sent_list:
            temp_text = temp_text + sentc
            temp_text = temp_text + " "
        
        self.text = temp_text
    
    #Format text as list
    def frmt_textlist(self):
        print("formatting text as list...")
        temp_text = ""
        for sentc in self.sent_list:
            temp_text = temp_text + sentc
            temp_text = temp_text + "\n"
        
        self.text = temp_text

    #Format text as block
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

    