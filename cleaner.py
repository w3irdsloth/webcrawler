 ###########
## Cleaner ##
 ###########
 
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

    #Print sentence list to .txt file formatted as a list
    def frmt_textlist(self):
        temp_text = ""
        for sentc in self.sent_list:
            temp_text = temp_text + sentc
            temp_text = temp_text + "\n"
        
        return temp_text

    #Print sentences to .txt file formated as a block
    def frmt_textblock(self):
        temp_text = ""
        for setnc in self.sent_list:
            temp_text = temp_text + setnc
            temp_text = temp_text + " "

        return temp_text