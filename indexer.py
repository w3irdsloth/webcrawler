 ###########
## Indexer ##
 ###########

import json
import os


class Indexer(object):
    """ Creates an object for indexing web links """    

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

    def save_db(self, db_content, db_name):
        try:
            with open(db_name, 'w') as f:
                    json.dump(db_content, f)
        except:
            print("something went wrong")
            

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

        else:
            print("file doesn't exist")

    #List available links in database
    def list_content(self, db_contents):
        text = ""
        for lnk in db_contents:
            data = db_contents[lnk]
            try:
                text += "Link: " + str(lnk) + "\n"
            except:
                pass
            
            try:
                server = data['Server']
                text += "Server: " + str(server) + "\n"
            except:
                pass
            
            try:
                date = data['Date']
                text += "Date: " + str(date) + "\n"
            except:
                pass
            
            try:
                content_type = data['Content-Type']
                text += "Content Type: " + str(content_type) + "\n"
            except:
                pass
                
            text += "\n"
        
        return text
    
    #Sort database by data_type
    def sort_data(self, db_contents, data_type, sort_reverse=False):
        sorted_contents = dict(sorted(db_contents.items(), key=lambda item: item[1][data_type] if data_type in item[1] else "", reverse=sort_reverse))
        return sorted_contents
