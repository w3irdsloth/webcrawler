 ###########
## Cleaner ##
 ###########

import language_tool_python

class Cleaner(object):
    """ Creates an object for finding and cleaning sentences """
    def __init__(self):
        self.text = ""
        self.sent_list = []

    def set_text(self, text):
        self.text = text

    def get_sentlist(self):
        return self.sent_list

    def set_sentlist(self, sent_list):
        self.sent_list = sent_list

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
    
    #Keep sentences that contain a keyword
    def check_kywrds(self, keywords):
        temp_list = []
        for sentc in self.sent_list:
            for wrd in keywords:
                if wrd in sentc:
                    print("keyword found: " + wrd)
                    temp_list.append(sentc)
                    print("sentence" + sentc)
                    break

        self.sent_list = temp_list

    def remv_quotes(self):
        char1 = "\""
        char2 = "\""
        temp_list = []
        for sentc in self.sent_list:
            for char in sentc:
                if char == char1:
                    slice_start = sentc.find(char1)
                    slice_end = sentc.find(char2, slice_start + 1)
                    sentc = sentc.replace(sentc[slice_start:slice_end + 1], "")

            temp_list.append(sentc)

        self.sentc_list = temp_list

    #Remove paranthesis from sentences
    def remv_pars(self):
        char1 = "("
        char2 = ")"
        temp_list = []
        for sentc in self.sent_list:
            for char in sentc:
                if char == char1:
                    slice_start = sentc.find(char1)
                    slice_end = sentc.find(char2, slice_start + 1)
                    sentc = sentc.replace(sentc[slice_start:slice_end + 1], "")

            temp_list.append(sentc)

        self.sentc_list = temp_list
            

    #Remove newline characters from sentence list
    def remv_newlines(self):
        temp_list = []
        for sentc in self.sent_list:
            for char in sentc:
                if char == "\n":
                    sentc = sentc.replace(char, "")

            temp_list.append(sentc)

        self.sent_list = temp_list

    #Remove non-declarative sentences from sentence list
    def remv_nodeclare(self):
        temp_list = []
        for sentc in self.sent_list:
            if "." in sentc:
                temp_list.append(sentc)
            
        self.sent_list = temp_list

    #Remove sentences with numbers
    def remv_nums(self):
        print("checking for numbers...")
        temp_list = []
        temp_list = temp_list + self.sent_list
        for sentc in self.sent_list:
            for char in sentc:
                if char.isdigit():
                    try:
                        temp_list.remove(sentc)

                    except:
                        break

        self.sent_list = temp_list
                    
    #Strip spaces from beginning and end of sentences
    def remv_wtspc(self):
        temp_list = []
        for sentc in self.sent_list:
            sentc = sentc.strip()
            temp_list.append(sentc)
        
        self.sent_list = temp_list

    #Remove extra spaces from sentences
    def remv_dblspaces(self):
        temp_list = []
        for sentc in self.sent_list:
            for char in sentc:
                if char == "  ":
                    sentc = sentc.replace(char, " ")

            temp_list.append(sentc)

        self.sent_list = temp_list

    #Remove sentences that don't begin with uppercase letters
    def remv_noleadcap(self):
        print("checking leading characters...")
        temp_list = []
        for sentc in self.sent_list:
            if sentc[0].isupper():
                temp_list.append(sentc)

        self.sent_list = temp_list

    #Remove sentences with extra capital letters
    def remv_excap(self):
        temp_list = [] 
        temp_list = temp_list + self.sent_list
        for sentc in self.sent_list:
            for char in sentc[1:]:
                if char.isupper():
                    try:
                        temp_list.remove(sentc)
                    
                    except:
                        break

        self.sent_list = temp_list

    #Remove empty whitespace from before punctuation
    def remv_endspc(self):
        print("cleaning endspaces...")
        temp_list = []
        for sentc in self.sent_list:  
            sentc.strip()         
            end_indx = len(sentc) - 1
            if sentc[end_indx - 1] == " ":
                print(sentc)
                sentc = sentc[:end_indx - 1:end_indx]
                print(sentc)
            
            temp_list.append(sentc)

        self.sent_list = temp_list

    #Remove sentences in sentence list based on min and max word length
    def trim_sentlist(self, sent_min, sent_max):
        print("trimming sentence list...")
        temp_list = []
        for sentc in self.sent_list:
            if len(sentc.split()) >= sent_min and len(sentc.split()) <= sent_max:
                temp_list.append(sentc)
                
        self.sent_list = temp_list

    #Fix spelling and grammar errors in sentence list
    def fix_language(self):
        print("fixing spelling and grammar errors...")
        lang_tool = language_tool_python.LanguageTool('en-US')
        for sentc in self.sent_list:
            errors = lang_tool.check(sentc)
            if len(errors) > 0:
                try:
                    error_index = self.sent_list.index(sentc)
                    fix_sentc = lang_tool.correct(sentc)
                    self.sent_list[error_index] = fix_sentc

                except:
                    break

    #Remove sentences with spelling and grammar errors from sentence list
    def remv_badlanguage(self):
        print("removing spelling and grammar errors...")
        lang_tool = language_tool_python.LanguageTool('en-US')
        temp_list = []
        for sentc in self.sent_list:
            errors = lang_tool.check(sentc)
            if len(errors) == 0:
                temp_list.append(sentc)

        self.sent_list = temp_list      

