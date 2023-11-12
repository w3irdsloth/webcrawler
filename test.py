from crawler import Crawler
from indexer import Indexer
from scraper import Scraper

import json
import time

import re

# from applicator import Applicator

## Build Applicator
# applicator = Applicator()

## Build Crawler
crawler = Crawler()

## Build Scraper ##
scraper = Scraper()

## Build Indexer
indexer = Indexer()


## Set initial URL
# url = 'https://www.duckduckgo.com'
# url = 'https://www.yahoo.com'
# url = 'https://www.google.com'
# url = 'https://www.yandex.com'
url = "https://www.geeksforgeeks.org/python-merging-two-dictionaries/"



## Scrape HTML ##
crawler.set_random_user_agent()
user_agent = crawler.get_user_agent()
# print("user agent: " + user_agent)

response = crawler.get_response(url)
# print("response: " + str(response))

# print("html: " + str(response.text))




## Parse links from HTML ##
link_list = scraper.parse_links(response)
print("links: " + str(link_list))
print ("# of links: " + str(len(link_list)))




## Parse metadata from single URL ##
# crawler.set_random_sleep()
# sleep = crawler.get_sleep()
# print("sleep time: " + str(sleep))

# crawler.set_random_user_agent()
# user_agent = crawler.get_user_agent()
# print("user agent: " + user_agent)

# response = crawler.get_response(url)
# print(response.headers)


## Parse response from link list and create array as: link[meta] ##
# db_content = {}
# int = 5
# for lnk in link_list:
#     crawler.set_random_sleep()
#     sleep_time = crawler.get_sleep()
#     print("sleep time: " + str(sleep_time))

#     crawler.set_random_user_agent()
#     user_agent = crawler.get_user_agent()
#     print("user agent: " + user_agent)

#     valid = False
#     if lnk not in db_content:

#         # response = crawler.parse_response(lnk)
#         response = crawler.get_response(lnk)
        
#         valid = crawler.check_validity(response)

#     if valid == True:
#         db_headers = dict(response.headers)
#         db_content[lnk] = db_headers

#     time.sleep(sleep_time)
    
#     int = int - 1
#     if int == 0:
#         break

# print("database: " + str(db_content))
# print("Database length: " + str(len(db_content)))



## Create new database from array ##
# db_name = 'db.json'
# indexer.create_db(db_content, db_name)




## Read array from database file ##
# db_name = 'db.json'
# db_content = indexer.read_db(db_name)


## List content from array ##
# print("before: ")
# text = indexer.list_content(db_content)
# print(text)

# data_type = 'Date'
# sort_reverse = True
# sorted_content = indexer.sort_data(db_content, data_type, sort_reverse=sort_reverse)

# print("after: ")
# text = indexer.list_content(sorted_content)
# print(text)




## Save database to file ##
# db_name = 'test.json'
# db_content = sorted_content
# indexer.save_db(db_content, db_name)


## Merge 2 databases ##
# db1 = "db1.json"
# db2 = "db2.json"

# db1_content = indexer.read_db(db1)
# db2_content = indexer.read_db(db2)

# text1 = indexer.list_content(db1_content)
# text2 = indexer.list_content(db2_content)

# print("db1:")
# print(text1)

# print("db2:")
# print(text2)

# merged_data = indexer.merge_data(db1_content, db2_content)

# text3 = indexer.list_content(merged_data)
# print("merged:")
# print(text3)






## Create list of html elements from response ##

# div_list = re.findall(r'(?:class=")([^"]*)', response.text)
# div_list = re.findall(r'(?:style=")([^"]*)', response.text)
# div_list = re.findall(r'(?<=<div>).*?(?=<\/div>)', response.text)

#The best one
# div_list = re.findall(r'<[^<>]+>', response.text)

tag_list = scraper.parse_elements(response)
# div_list = crawler.parse_elements(response)


# query = "style"
# query = "display: none"
query = "<script>"

div_list = scraper.filter_elements(tag_list, query)

# print("div list: " + str(div_list))
# print("\n")

for div in div_list:
    print(div)


## Find elements between substrings ##

# test_str = response.text

# # sub1 = "<title>"
# # sub2 = "</title>"

# # sub1 = "<!DOCTYPE"
# # sub2 = ">"

# # sub1 = "<head>"
# # sub2 = "</head>"

# # sub1 = ";lakjdsflkajsfd"
# # sub2 = ">"

# # sub1 = "display:"
# # sub2 = ";"

# sub1 = "style"
# sub2 = ";"

# # sub1 = "Compression"
# # sub2 = ">"

# # sub1 = "hidden"
# # sub2 = ";"

# # getting index of substrings
# idx1 = test_str.find(sub1)
# print(idx1)
# idx2 = test_str.find(sub2, idx1)
# print(idx2)

# # result = test_str[idx1 + len(sub1): idx2]
# result = test_str[idx1 - 1: idx2 - len(sub2)]
 
# # printing result
# print("\n")
# print("The extracted string : " + result)

# for e in div_list:
#     if sub1 in e and sub2 in e and "none" in e:
#         print(e)








## Print content between one div element and the next ##
# print(response.text)

text_start = 0
list_start = 0

num = 0
max = 20
for e in div_list:

    list_index = div_list.index(e, list_start)
    # print("start index #: " + str(list_index))
    
    sub1 = e
    print("string 1: " + sub1)

    sub2 = div_list[list_index + 1]
    print("string 2: " + sub2)


    text_index1 = response.text.find(sub1, text_start)
    # print(text_index1)

    text_index2 = response.text.find(sub2, text_index1 + len(sub1))
    # print(text_index2)    

    result = response.text[text_index1 + len(sub1): text_index2]
    print("in between: " + result)
    
    list_start = list_index + 1
    text_start = text_index1 + len(sub1)

    num += 1
    if num >= max:
        break


