from felo.web.crawler import Crawler
from felo.web.scraper import Scraper
from felo.web.indexer import Indexer

from felo.office.reader import Reader
from felo.office.writer import Writer
from felo.office.editor import Editor

import time
import random
from os.path import splitext, basename, dirname


   ###########
#### Helpers ####
   ###########

def rand_sleep(max_num):
    sleep_time = random.randrange(0, max_num)
    time.sleep(sleep_time)

def remv_duplicates(list):
    new_list = []
    for itm in list:
        if itm not in new_list:
            new_list.append(itm)

    return new_list

def print_items(data):
    for itm in data:
        print(itm)

# Add items in data to list
def list_items(data):
    list= []
    for itm in data:
        list.append(itm)

    return list

# Return list of elements containing query
def query_list(list, query=""):
    new_list = []
    for itm in list:
        if query in itm:
            new_list.append(itm)

        else:
            pass

    return new_list

# Filter list items containing query
def filter_list(list, query=""):
    new_list = []
    for itm in list:
        if query in itm:
            pass
        
        else:
            new_list.append(itm)

    return new_list


def split_path(file_path):
    file = basename(file_path)
    file_tuple = splitext(file)
    file_name = file_tuple[0]
    ext_name = file_tuple[1]
    dir_name = dirname(file_path)
    path_data = {
        "file": file,
        "filename": file_name,
        "extension": ext_name,
        "directory": dir_name

    }

    return path_data

  ##########
#### office ####
   ##########

def write_text(doc_name, txt_content):
    writer = Writer()
    writer.write_txt(doc_name, txt_content)

def read_text(doc_name):
    reader = Reader()
    text = reader.read_text(doc_name)
    return text

def read_file(doc_name, handlers):
    reader = Reader()
    reader.set_handlers(handlers)

    path_data = split_path(doc_name)
    file_ext = path_data['extension']
    if file_ext == '.doc' or ".docm" or ".docx" or ".dot" or ".dotx":
        doc_text = reader.read_doc(doc_name)

    elif file_ext == '.pdf':
        doc_text = reader.read_pdf(doc_name)

    else:
        print("unsupported filetype")
        doc_text = None

    return doc_text


   #######
#### web ####
   #######

## Get response from URL

def gen_headers(user_agent, headers_accept, accept_language, accept_encoding):
    headers = {'User-Agent': user_agent,
        'Accept': headers_accept,
        'Accept-Language': accept_language,
        'Accept-Encoding': accept_encoding}
    
    return headers

def get_response(url, headers):
    crawler = Crawler()
    crawler.set_headers(headers)
    response = crawler.get_response(url)
    return response

def check_response(response):
    crawler = Crawler()
    valid = crawler.check_validity(response)
    return valid

def get_head(url, headers):
    crawler = Crawler()
    crawler.set_headers(headers)
    response = crawler.get_head(url)
    return response

def crawl_web(seed_url, max_links, max_timeout, max_sleep, headers, user_agent_list):
    crawler = Crawler()
    scraper = Scraper()
    crawled_links = []
    start_time = time.time()
    run_time = 0
    crawler.set_headers(headers)
    response = crawler.get_response(seed_url)

    print("crawling web for links...")
    print("max links: " + str(max_links))
    print("max seconds: " + str(max_timeout))
    
    if crawler.check_validity(response):
        html = response.text
        queued_links = scraper.scrape_links(html)
        queued_links = remv_duplicates(queued_links)

    else:
        print("start url returned no response")
        exit(0)

    for lnk in queued_links:
        crawler.set_random_user_agent(user_agent_list)
        response = crawler.get_response(lnk)

        if crawler.check_validity(response):
            html = response.text
            temp_links = scraper.scrape_links(html)
            queued_links = queued_links + temp_links
            queued_links = remv_duplicates(queued_links)
            crawled_links.append(lnk)
            current_time = time.time()
            run_time = current_time - start_time

        else:
            print("response invalid")

        queued_links.remove(lnk)
        print("run time: " + str(run_time))
        print("num links: " + str(len(crawled_links)))
        print("time remaining: " + str(max_timeout - run_time))

        if len(crawled_links) >= max_links:
            print("max links collected")
            break
        
        elif run_time >= max_timeout:
            print("timeout")
            break

        else:
            rand_sleep(max_sleep)
            pass

    return crawled_links

# Download file from url
def dl_file(url, dl_directory, redirects):
    # redirects = True
    crawler = Crawler()
    crawler.dl_file(url, dl_directory, redirects)

# Download list of links
def dl_files(link_list, dl_directory, redirects):
    # directory = "/home/n0xs1/projects/felo/tests/downloads"
    # redirects = True
    crawler = Crawler()
    for lnk in link_list:
        crawler.dl_file(lnk, dl_directory, redirects)

## Parse response from link list and create array as: link[meta] ##
def gen_array(link_list, max_sleep, headers, user_agent_list):
    crawler = Crawler()
    db_content = {}
    crawler.set_headers(headers)
    for lnk in link_list:
        if lnk not in db_content:
            response = crawler.get_head(lnk)
            if crawler.check_validity(response):
                db_headers = dict(response.headers)
                db_content[lnk] = db_headers

            else:
                print("response invalid")

        else:
            print("link exists")
        
        crawler.set_random_user_agent(user_agent_list)
        rand_sleep(max_sleep)

    return db_content

def gen_db(db_content, db_name):
    indexer = Indexer()
    db = indexer.gen_db(db_content, db_name)
    return db


def read_db(db_name):
    indexer = Indexer()
    db = indexer.read_db(db_name)
    return db

## Merge 2 databases ##
def merge_data(db1, db2):
    indexer = Indexer()
    db1_content = indexer.read_db(db1)
    db2_content = indexer.read_db(db2)
    merged_db = indexer.merge_data(db1_content, db2_content)
    return merged_db


# Generate index file based on query
def search_db(db1, db2, query):
    indexer = Indexer()
    search_array = indexer.read_db(db1)
    temp_array = {}
    for lnk in search_array:
        if query in lnk or query in search_array[lnk]:
            temp_array[lnk] = search_array[lnk]

        else:
            pass
    
    new_db = indexer.gen_db(temp_array, db2)

    return new_db

# Generate index file containing downloadable links
def gen_link_db(db1, db2):
    indexer = Indexer()
    search_array = indexer.read_db(db1)
    temp_array = {}
    content_list = ['image/png']
    for lnk in search_array:
        head = search_array[lnk]
        if head['Content-Type'] and head['Content-Type'] in content_list:
            temp_array[lnk] = search_array[lnk]

        else:
            pass

    print(temp_array)
    new_db = indexer.gen_db(temp_array, db2)

    return new_db
                                    
## Return content between html elements
def scrape_content(html, tag1, tag2):
    scraper = Scraper()
    content = scraper.scrape_content(html, tag1, tag2)
    return content

## Remove content between html elements
def remove_content(html, tag1, tag2):
    scraper = Scraper()
    html = scraper.remove_content(html, tag1, tag2)
    return html

# Create list of html elements from scraped text
def parse_elmnts(html):
    scraper = Scraper()
    elmnt_list = scraper.parse_elmnts(html)
    return elmnt_list

# Parse elements from html and return as text
def scrape_elmnts(html):
    scraped_text = ""
    elmnt_list = parse_elmnts(html)
    for elmnt in elmnt_list:
        scraped_text += elmnt + "\n"

    return scraped_text

def gen_elmnt_matrix(elmnt_list):
    scraper = Scraper()
    elmnt_matrix = scraper.gen_elmnt_matrix(elmnt_list)
    return elmnt_matrix
    
def gen_link_matrix(elmnt_matrix):
    scraper = Scraper()
    link_matrix = scraper.gen_link_matrix(elmnt_matrix)
    return link_matrix

def filter_tags(html, query):
    scraper = Scraper()
    filtered_text = ""
    elmnt_list = scraper.parse_elmnts(html)
    elmnt_list = query_list(elmnt_list, query)
    for elmnt in elmnt_list:
        filtered_text += elmnt + "\n"

    return filtered_text

def remove_tags(html, tag):
    scraper = Scraper()
    scraped_text = ""
    elmnt_list = scraper.parse_elmnts(html)
    elmnt_list = filter_list(elmnt_list, tag)
    for elmnt in elmnt_list:
        scraped_text += elmnt

    return scraped_text

## Parse text from HTML ##
def scrape_text(html):
    scraper = Scraper()
    scraped_text = scraper.scrape_text(html)
    return scraped_text


## Editing ##
def edit_text(text, cycle_config, sentmin, sentmax):
        editor = Editor()
        editor.create_sentc_list(text)

        if cycle_config["noalpha"]:
            editor.remv_noalpha()

        if cycle_config["nodeclare"]:
            editor.remv_nodeclare()

        if cycle_config["excaps"]:
            editor.remv_excaps()

        if cycle_config["exletters"]:
            editor.remv_exletters()

        if cycle_config["firstperson"]:
            editor.remv_firstperson()

        if cycle_config["secondperson"]:
            editor.remv_secondperson()

        if cycle_config["dupwords"]:
            editor.remv_dupwords()

        if cycle_config["duplicates"]:
            editor.remv_duplicates()

        if cycle_config["trimsentlist"]:
            editor.trim_sentlist(sentmin, sentmax)

        # elif cycle == "checkspelling":
        #     editor.check_misspelled(dictionary)

        sentc_list = editor.get_sentc_list()    
        clean_text = ""
        for sentc in sentc_list:
            clean_text += sentc + " "

        return clean_text


