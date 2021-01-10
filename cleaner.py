 ###########
## Cleaner ##
 ###########

import re

class Cleaner(object):
    """ Creates an object for building and cleaning sentences """
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
        print("checking keywords...")
        temp_list = []
        for sentc in self.sent_list:
            for wrd in keywords:
                if wrd in sentc:
                    temp_list.append(sentc)
                    break

        self.sent_list = temp_list

    #Remove duplicate sentences
    def remv_duplicates(self):
        print("removing duplicate sentences...")
        temp_list = []
        for sentc in self.sent_list:
            if sentc not in temp_list:
                temp_list.append(sentc)

        self.sent_list = temp_list

    #Remove sentences with duplicate words
    def remv_dupwrds(self):
        print("removing duplicate words...")
        temp_list = []
        temp_list = temp_list + self.sent_list
        for sentc in self.sent_list:
            temp_sentc = re.sub(r'[^\w\s]', '', sentc)
            check_list = temp_sentc.split()
            word_list = []
            for wrd in check_list:
                if wrd.lower() not in word_list:
                    word_list.append(wrd.lower())

                else:
                    temp_list.remove(sentc)
                    break

        self.sent_list = temp_list

    #Remove sentences with firs-person language
    def remv_firstperson(self):
        print("removing first-person language...")
        word_list = ["I", "me", "Me", "my", "My", "mine", "Mine", "our", "Our", "ours", "Ours", "us", "Us", "we", "We"]
        temp_list = []
        temp_list = temp_list + self.sent_list
        for sentc in self.sent_list:
            temp_sentc = re.sub(r'[^\w\s]', '', sentc)
            check_list = temp_sentc.split()
            for wrd in check_list:
                if wrd not in word_list:
                    pass

                else:
                    temp_list.remove(sentc)
                    break

        self.sent_list = temp_list

    #Remove sentences with second-person language
    def remv_secondperson(self):
        print("removing second-person language...")
        word_list = ["you", "You", "your", "Your", "yours", "Yours"]
        temp_list = []
        temp_list = temp_list + self.sent_list
        for sentc in self.sent_list:
            temp_sentc = re.sub(r'[^\w\s]', '', sentc)
            check_list = temp_sentc.split()
            for wrd in check_list:
                if wrd not in word_list:
                    pass

                else:
                    temp_list.remove(sentc)
                    break

        self.sent_list = temp_list

    #Remove non-declarative sentences from sentence list
    def remv_nodeclare(self):
        print("removing non-declaratives...")
        temp_list = []
        for sentc in self.sent_list:
            try:
                sentc = sentc.strip()
                if sentc[-1] == ".":
                    temp_list.append(sentc)

            except:
                pass
            
        self.sent_list = temp_list

    #Remove sentences with numbers
    def remv_nums(self):
        print("removing numbers...")
        temp_list = []
        temp_list = temp_list + self.sent_list
        for sentc in self.sent_list:
            for char in sentc:
                if char.isdigit():
                    try:
                        temp_list.remove(sentc)
                        break

                    except:
                        break

        self.sent_list = temp_list
                    
    #Strip spaces from beginning and end of sentences
    def remv_wtspc(self):
        print("removing whitespace...")
        temp_list = []
        for sentc in self.sent_list:
            sentc = sentc.strip()
            temp_list.append(sentc)
        
        self.sent_list = temp_list

    #Remove extra spaces from sentences
    def remv_dblspaces(self):
        print("removing excess spaces...")
        temp_list = []
        for sentc in self.sent_list:
        #     for char in sentc:
        #         if char == "  ":
        #             sentc = sentc.replace(char, " ")

        #     temp_list.append(sentc)

            sentc = " ".join(sentc.split())
            temp_list.append(sentc)

        self.sent_list = temp_list

    #Remove sentences that don't begin with uppercase letters
    def remv_noleadcap(self):
        print("removing unwanted leading characters...")
        temp_list = []
        for sentc in self.sent_list:
            if sentc[0].isupper():
                temp_list.append(sentc)

        self.sent_list = temp_list

    #Remove sentences with extra capital letters
    def remv_excap(self):
        print("removing extra capitals...")
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
        print("removing endspaces...")
        temp_list = []
        for sentc in self.sent_list:  
            try:
                sentc.strip()         
                end_indx = len(sentc) - 1
                if sentc[end_indx - 1] == " ":
                    print(sentc)
                    sentc = sentc[:end_indx - 1:end_indx]
                    print(sentc)

            except:
                pass
            
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

    def check_spelling(self):
        print("checking for spelling errors...")
        from spellchecker import SpellChecker
        spellchecker = SpellChecker()
        temp_list = []
        for sentc in self.sent_list:
            word_list = re.sub(r'[^\w\s]', '', sentc).split()
            misspelled = spellchecker.unknown(word_list)
            if len(misspelled) == 0:
                temp_list.append(sentc)
            
        self.sent_list = temp_list


    # #LANGUAGE=TOOL Functions
    # #Fix spelling and grammar errors in sentence list
    # def fix_language(self):
    #     import language_tool_python
    #     print("fixing spelling and grammar errors...")
    #     lang_tool = language_tool_python.LanguageTool('en-US')
    #     temp_list = []
    #     for sentc in self.sent_list:
    #         errors = lang_tool.check(sentc)
    #         if len(errors) > 0:
    #                 sentc = lang_tool.correct(sentc)
                    
    #         temp_list.append(sentc)

    #     self.sent_list = temp_list

    # #Remove sentences with spelling and grammar errors from sentence list
    # def remv_badlanguage(self):
    #     import language_tool_python
    #     print("removing spelling and grammar errors...")
    #     lang_tool = language_tool_python.LanguageTool('en-US')
    #     temp_list = []
    #     for sentc in self.sent_list:
    #         errors = lang_tool.check(sentc)
    #         if len(errors) == 0:
    #             temp_list.append(sentc)

    #     self.sent_list = temp_list      

