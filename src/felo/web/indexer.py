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
    def gen_db(self, db_content, db_name):
        if os.path.isfile(db_name):
            print("db file exists")
            return None

        else:
            try:
                with open(db_name, 'w') as f:
                    json.dump(db_content, f)
                    return db_content

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
            print("read failed: file doesn't exist")
            return None

    #Merge two databases
    def merge_data(self, db1, db2):
        try:
            merged_db = {**db1, **db2}
            
        except:
            return None

        return merged_db

    #Sort database by data_type
    def sort_data(self, db_contents, data_type, sort_reverse=False):
        sorted_contents = dict(sorted(db_contents.items(), key=lambda item: item[1][data_type] if data_type in item[1] else "", reverse=sort_reverse))
        return sorted_contents

    #List links/content info in database
    def list_content(self, db_contents):
        text = ""
        # for lnk in db_contents:
        for lnk in [lnk for lnk in (db_contents or [])]:
            data = db_contents[lnk]
            text += "Link: " + str(lnk) + "\n"
            for cnt in self.content_list:
                contents = data[cnt]
                text += cnt + ": " + str(contents) + "\n"
            text += "\n"

        return text
