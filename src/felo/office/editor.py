 ##########
## Editor ##
 ##########

import re

class Editor(object):
    """Constructs an object for cleaning and formatting sentences."""
    
    def __init__(self):
        """Constructs the necessary attributes for the Editor object."""
        self.sentc_list = []

    def set_sentc_list(self, sentc_list):
        """Sets a list of sentences to work with."""
        self.sentc_list = sentc_list

    def get_sentc_list(self):
        """Returns the current sentence list."""
        return self.sentc_list

    def create_sentc_list(self, text):
        """Creates a list of sentences out of text."""
        print("creating sentence list...")
        temp_list = re.findall(r'([A-Z][^\.!?]*[\.!?])', text)
        self.sentc_list = temp_list

    def check_keywords(self, keywords):
        """Returns list of sentences that contain a keyword."""
        print("checking for keywords...")
        temp_list = []
        for sentc in self.sentc_list:
            for kywrd in keywords:
                if kywrd in sentc:
                    print(sentc)
                    print(kywrd)
                    temp_list.append(sentc)
                    break

        self.sentc_list = temp_list

    def frmt_textstring(self):
        """Formats sentence list as string."""
        print("formatting text as string...")
        formatted_text = ""
        try:
            for sentc in self.sent_list:
                formatted_text = formatted_text + sentc + " "

        except:
            print("error, no text formatted")
            return None

        return formatted_text
    

    def frmt_newlines(self):
        """Formats sentence list with newlines."""
        print("formatting text with newlines...")
        formatted_text = ""
        try:
            for sentc in self.sent_list:
                formatted_text = formatted_text + sentc + "\n"

        except:
            print("error, no text formatted")
            return None

        return formatted_text


    def remv_duplicates(self):
        """Removes duplicates from sentence list."""
        print("removing duplicates...")
        temp_list = list(set(self.sentc_list))
        self.sentc_list = temp_list
        
    def remv_newlines(self):
        """Removes newlines from sentences in list."""
        print("removing newlines...")
        temp_list = []
        for sentc in self.sentc_list:
            sentc = sentc.replace("-\n", "")
            sentc = " ".join(sentc.splitlines())
            temp_list.append(sentc)

        self.sentc_list = temp_list

    def remv_dupwords(self):
        """Removes sentences with duplicate words."""
        print("removing duplicate words...")
        #List of commonly used conjunctions, articles, and prepositions to ignore
        pass_list = ["is", "for", "and", "or", "are", "the", "a", "an", "at", "of", "to", "in", "on", "they", "there"]
        temp_list = []
        temp_list = temp_list + self.sentc_list
        for sentc in self.sentc_list:
            temp_sentc = re.sub(r'[^\w\s]', '', sentc)
            check_list = temp_sentc.split()
            word_list = []
            for wrd in check_list:
                if wrd in pass_list:
                    pass
                    
                elif wrd.lower() not in word_list:
                    word_list.append(wrd.lower())

                else:
                    with open("duplicatewords.txt", "a") as temp_file:
                        temp_file.write(wrd + "\n")
                        temp_file.close()
                    temp_list.remove(sentc)
                    break

        self.sentc_list = temp_list

    def remv_pars(self):
        """Removes parentheses from sentences in list."""
        print("removing parentheses...")
        temp_list = []
        for sentc in self.sentc_list:
            sentc = re.sub(r"[\(\[].*?[\)\]]", "", sentc)
            temp_list.append(sentc)

        self.sentc_list = temp_list

    def remv_noalpha(self):
        """Removes sentences that contain non-alphabetical characters from list."""
        print("removing non-alphabetical characters...")
        pun_list = [".", "?", "!"]
        pass_list = [" ", ",", "'"]
        temp_list = []
        for sentc in self.sentc_list:
            temp_sent = ""
            for char in sentc:
                if char.isalpha() or char in pass_list:
                    temp_sent = temp_sent + char

                elif char in pun_list:
                    temp_sent = temp_sent + char
                    temp_list.append(temp_sent)
                    break

        self.sentc_list = temp_list

    def remv_nodeclare(self):
        """Removes non-declarative sentences from list."""
        print("removing non-declaratives...")
        temp_list = []
        for sentc in self.sentc_list:
            try:
                sentc = sentc.strip()
                if sentc[-1] == ".":
                    temp_list.append(sentc)

            except:
                pass
            
        self.sentc_list = temp_list

    def remv_firstperson(self):
        """Removes sentences with first-person language from list."""
        print("removing first-person language...")
        word_list = ["I", "me", "Me", "my", "My", "mine", "Mine", "our", "Our", "ours", "Ours", "us", "Us", "we", "We"]
        temp_list = []
        temp_list = temp_list + self.sentc_list
        for sentc in self.sentc_list:
            temp_sentc = re.sub(r'[^\w\s]', '', sentc)
            check_list = temp_sentc.split()
            for wrd in check_list:
                if wrd not in word_list:
                    pass

                else:
                    temp_list.remove(sentc)
                    break

        self.sentc_list = temp_list

    def remv_secondperson(self):
        """Removes sentences with second-person language from list."""
        print("removing second-person language...")
        word_list = ["you", "You", "your", "Your", "yours", "Yours"]
        temp_list = []
        temp_list = temp_list + self.sentc_list
        for sentc in self.sentc_list:
            temp_sentc = re.sub(r'[^\w\s]', '', sentc)
            check_list = temp_sentc.split()
            for wrd in check_list:
                if wrd not in word_list:
                    pass

                else:
                    temp_list.remove(sentc)
                    break

        self.sentc_list = temp_list

    def remv_excaps(self):
        """Removes sentences with extra capital letters from list."""
        print("removing extra capitals...")
        temp_list = [] 
        temp_list = temp_list + self.sentc_list
        for sentc in self.sentc_list:
            for char in sentc[1:]:
                if char.isupper():
                    temp_list.remove(sentc)
                    break

        self.sentc_list = temp_list

    def remv_exletters(self):
        """Remove sentences with single letters from list."""
        print("removing extra letters...")
        temp_list = []
        temp_list = temp_list + self.sentc_list
        for sentc in self.sentc_list:
            temp_sentc = re.sub(r'[^\w\s]', '', sentc)
            check_list = temp_sentc.split()
            for wrd in check_list:
                if len(wrd) == 1 and wrd != "a":
                    temp_list.remove(sentc)
                    break

        self.sentc_list = temp_list

    def remv_badpgs(self):
        """Removes page indicators from list."""
        print("removing page indicators...")
        temp_list = []
        for sentc in self.sentc_list:
            sentc = sentc.replace(" pp", "")
            temp_list.append(sentc)

        self.sentc_list = temp_list

    def remv_badcoms(self):
        """Fix poor comma spacing for sentences in list."""
        print("removing bad comma spacing...")
        temp_list = []
        for sentc in self.sentc_list:
            sentc = sentc.strip()
            sentc = sentc.replace(",.", ".")
            sentc = sentc.replace(", .", ".")
            sentc = sentc.replace(",,", "")
            sentc = sentc.replace(", ,", "")
            temp_list.append(sentc)

        self.sentc_list = temp_list

    def remv_wtspace(self):
        """Removes whitespace from sentences in list."""
        print("removing whitespace...")
        temp_list = []
        for sentc in self.sentc_list:
            sentc = " ".join(sentc.split())
            temp_list.append(sentc)

        self.sentc_list = temp_list

    def remv_endspace(self):
        """Removes space after punctuation from sentences in list."""
        print("removing bad end spacing...")
        temp_list = []
        for sentc in self.sentc_list:
            sentc = sentc.strip()
            while " ." in sentc:
                sentc = sentc.replace(" .", ".")
            
            temp_list.append(sentc)

        self.sentc_list = temp_list
    
    def remv_punspace(self):
        """Removes empty space from between sentences and append to new list."""
        print("removing punctuation space...")
        temp_list = []
        for sentc in self.sentc_list:
            sentc = " ".join(sentc.split())
            sentc = re.sub(r'\s([?.!",](?:\s|$))', r'\1', sentc)
            temp_list.append(sentc)

        self.sentc_list = temp_list

    def trim_sentlist(self, sent_min, sent_max):
        """Removes sentences in sentence list based on min and max word length."""
        print("trimming sentence list...")
        temp_list = []
        for sentc in self.sentc_list:
            if len(sentc.split()) >= sent_min and len(sentc.split()) <= sent_max:
                temp_list.append(sentc)
                
        self.sentc_list = temp_list


    def check_misspelled(self, words):
        """Check words against dictionary for rudimentary spellchecking."""
        print("checking for spelling errors...")
        dict_list = [""]
        words = open(words, 'r')
        wrdlines = words.readlines()
        for wrd in wrdlines:
            dict_list.append(re.sub('\n', '', wrd.lower()))
            
        temp_list = []
        for sentc in self.sentc_list:
            word_list = re.sub(r'[^\w\s]', '', sentc.lower()).split()
            check = all(item in dict_list for item in word_list)
            if check == True:
                temp_list.append(sentc)

        self.sentc_list = temp_list


    # #Use spellchecker
    # def remv_badspelling(self):
    #     print("checking for spelling errors...")
    #     from spellchecker import SpellChecker
    #     spellchecker = SpellChecker(distance=1)
    #     temp_list = []
    #     temp_list = temp_list + self.sentc_list
    #     for sentc in self.sentc_list:
    #         word_list = re.sub(r'[^\w\s]', '', sentc).split()
    #         for wrd in word_list:
    #             print(wrd)
                

    #         print("word list: " + str(word_list))
    #         misspelled = spellchecker.unknown(word_list)
    #         print("misspelled: " + str(misspelled))
    #         if len(misspelled) > 0:
    #             print("misspelled tag: " + str(misspelled))
    #             temp_list.remove(sentc)
            
    #     self.sentc_list = temp_list


    ## Use Language-Tool
    # #Fix spelling and grammar errors in sentence list
    # def fix_language(self):
    #     import language_tool_python
    #     print("fixing spelling and grammar errors...")
    #     lang_tool = language_tool_python.LanguageTool('en-US')
    #     temp_list = []
    #     for sentc in self.sentc_list:
    #         errors = lang_tool.check(sentc)
    #         if len(errors) > 0:
    #                 sentc = lang_tool.correct(sentc)
                    
    #         temp_list.append(sentc)

    #     self.sentc_list = temp_list

    # #Remove sentences with spelling and grammar errors from sentence list
    # def remv_badlanguage(self):
    #     import language_tool_python
    #     print("removing spelling and grammar errors...")
    #     lang_tool = language_tool_python.LanguageTool('en-US')
    #     temp_list = []
    #     for sentc in self.sentc_list:
    #         print(sentc)
    #         errors = lang_tool.check(sentc)
    #         print("errors: " + str(errors))
    #         if len(errors) == 0:
    #             temp_list.append(sentc)

    #     self.sentc_list = temp_list
