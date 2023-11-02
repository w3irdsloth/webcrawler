from crawler import Crawler

from indexer import Indexer

import json
import time

# from applicator import Applicator

## Build Applicator
# applicator = Applicator()

## Build Crawler
crawler = Crawler()

## Build Indexer
indexer = Indexer()

## Set initial URL
# url = 'https://www.duckduckgo.com'
# url = 'https://www.yahoo.com'
# url = 'https://www.google.com'
url = 'https://www.yandex.com'


## Scrape HTML ##
# crawler.set_random_sleep()
# sleep_time = crawler.get_sleep()
# print("sleep time: " + str(sleep_time))

# crawler.set_random_user_agent()
# user_agent = crawler.get_user_agent()
# print("user agent: " + user_agent)

# html = crawler.scrape_html(url)
# print("response: " + str(html))

# time.sleep(sleep_time)

# print(html.text)
# print("head: " + str(html.headers))



## Parse links from HTML ##
# link_list = crawler.parse_links(html)
# print("links: " + str(link_list))
# print ("# of links: " + str(len(link_list)))



## Parse  metadata from single URL ##
# crawler.set_random_sleep()
# sleep = crawler.get_sleep()
# print("sleep time: " + str(sleep))

# crawler.set_random_user_agent()
# user_agent = crawler.get_user_agent()
# print("user agent: " + user_agent)

# meta = crawler.parse_meta(url)
# print(meta.headers)



## Parse metadata from list and create database ##
# db_array = {}
# int = 5
# for lnk in link_list:
#     crawler.set_random_sleep()
#     sleep_time = crawler.get_sleep()
#     print("sleep time: " + str(sleep_time))

#     crawler.set_random_user_agent()
#     user_agent = crawler.get_user_agent()
#     print("user agent: " + user_agent)

#     metadata = crawler.parse_response(lnk)
#     if lnk not in db_array:
#         db_headers = dict(metadata.headers)
#         db_array[lnk] = db_headers

#     time.sleep(sleep_time)
    
#     int = int - 1
#     if int == 0:
#         break

# print("database: " + str(db_array))

# db_name = 'db.json'
# indexer.create_db(db_array, db_name)


## Read database ##
# db_name = 'db.json'
# db_name = 'db.json'
db_name = 'test.json'
db_content = indexer.read_db(db_name)

## Index metadata ##
# print("before: ")
# text = indexer.list_content(db_content)
# print(text)

data_type = 'Date'
sort_reverse = True
sorted_content = indexer.sort_data(db_content, data_type, sort_reverse=sort_reverse)

# print("after: ")
# text = indexer.list_content(sorted_content)
# print(text)


# result_one =  db_contents['https://duckduckgo.com/?smartbanner=1']
# print (result_one['Server'])
# print(result_one['Date'])

    # content_type = indexer.get_content_type(metadata)
    # print("Content Type: " + str(content_type))

    # content_length = indexer.get_content_length(metadata)
    # print("Content Length: " + str(content_length))

    # content_encoding = indexer.get_content_encoding(metadata)
    # print("Content Encoding: " + str(content_encoding))

    # last_modified = indexer.get_last_modified(metadata)
    # print("Last Modified: " + str(last_modified))

    # connection = indexer.get_connection(metadata)
    # print("Connection: " + str(connection))

    # print("headers: ")
    # print(metadata.headers)
    # print("\n")


## Save database ##
db_name = 'test.json'
db_content = sorted_content
indexer.save_db(db_content, db_name)
