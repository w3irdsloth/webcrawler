 ###########
## Indexer ##
 ###########

import json
import os

content_list = ['Server', 'Date', 'Content-Type']

class Indexer(object):
    """ Creates an object for indexing web links """

    def __init__(self):
        self.content_list = content_list

    #Convert array to JSON database
    def create_db(self, db_content, db_name):
        if os.path.isfile(db_name):
            print("file exists")
        else:
            try:
                with open(db_name, 'w') as f:
                    json.dump(db_content, f)
            except:
                print("something went wrong")
                return None

    def save_db(self, db_content, db_name):
        try:
            with open(db_name, 'w') as f:
                    json.dump(db_content, f)
        except:
            print("something went wrong")
            return None
            

    #Convert JSON database to array
    def read_db(self, db_name):
        if os.path.isfile(db_name):
            try:
                with open(db_name) as f:
                    file_contents = f.read()
                    db = json.loads(file_contents)
                    return db

            except:
                    print("something went wrong")
                    return None

        else:
            print("file doesn't exist")
            return None

    #Merge two databases
    def merge_data(self, db1, db2):
        merged_db = {**db1, **db2}
        return merged_db

    #Sort database by data_type
    def sort_data(self, db_contents, data_type, sort_reverse=False):
        sorted_contents = dict(sorted(db_contents.items(), key=lambda item: item[1][data_type] if data_type in item[1] else "", reverse=sort_reverse))
        return sorted_contents

    #List links/content info in database
    def list_content(self, db_contents):
        text = ""
        for lnk in db_contents:
            data = db_contents[lnk]
            try:
                text += "Link: " + str(lnk) + "\n"
            except:
                pass

            for cnt in self.content_list:
                try:
                    contents = data[cnt]
                    text += cnt + ": " + str(contents) + "\n"
                
                except:
                    pass
                
            text += "\n"
        
        return text
