from crawler import Crawler
from scraper import Scraper
from indexer import Indexer

import time
import random
from os.path import splitext, basename, dirname
import re


   ###########
#### Helpers ####
   ###########

def rand_sleep(max_num):
    """Sleeps for random amount of time."""
    sleep_time = random.randrange(0, max_num)
    time.sleep(sleep_time)

def remv_duplicates(old_list):
    """Removes duplicates from list."""
    new_list = list(set(old_list))
    return new_list

def check_lists(list1, list2):
    """Appends items in first list to new list if they aren't in second list."""
    new_list = []
    for i in list1:
        if i not in list2:
            new_list.append(i)

    return new_list

def print_items(data):
    """Prints out items in data set."""
    for itm in data:
        print(itm)

def list_items(data):
    """Adds items in data set to list."""
    list= []
    for itm in data:
        list.append(itm)

    return list

def query_list(list, query=""):
    """Filters list items for query."""
    new_list = []
    for itm in list:
        if query in itm:
            new_list.append(itm)

        else:
            pass

    return new_list

def filter_list(list, query=""):
    """Filters out list items containing query."""
    new_list = []
    for itm in list:
        if query in itm:
            pass
        
        else:
            new_list.append(itm)

    return new_list

def split_path(file_path):
    """Splits a file path and returns dictionary."""
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


  #######
### Web ###
  #######

def gen_headers(user_agent, headers_accept, accept_language, accept_encoding, referer):
    """Generate headers for html request."""
    headers = {'User-Agent': user_agent,
        'Accept': headers_accept,
        'Accept-Language': accept_language,
        'Accept-Encoding': accept_encoding,
        'Referer': referer
        }
    
    return headers

def get_status(url, headers):
    """Returns html request response from URL."""
    crawler = Crawler()
    crawler.set_headers(headers)
    response = crawler.get_response(url)
    if response is not None:
        response_status = response.status_code

    else:
        response_status = None

    return response_status

def check_response(response):
    """Checks whether html response request was valid."""
    crawler = Crawler()
    valid = crawler.check_validity(response)
    return valid

def get_head(url, headers):
    """Returns head data from html request."""
    crawler = Crawler()
    crawler.set_headers(headers)
    response = crawler.get_head(url)
    return response

def get_snippet(response):
    scraper = Scraper()
    text_snippet = ""
    content_list = [
        'text/css', 
        'text/csv',
        'text/html',
        'text/plain',
        'text/xml',
        'text/javascript',
        'None',
    ] 

    content_type = response.headers.get('Content-Type')
    if content_type == None:
        pass

    elif any(item in content_type for item in content_list):
        pass

    else:
        return text_snippet
    
    print("getting snippet...")
    html = response.text
    ## Order is important here!!! Removing style elements first will cause problems. ##
    scraper.gen_elmnt_list(html)
    html = scraper.remove_content(html, '<script', '</script>')
    scraper.gen_elmnt_list(html)
    html = scraper.remove_content(html, '<style', '</style>')
    scraper.gen_elmnt_list(html)
    html = scraper.scrape_text(html)
    text_snippet = " ".join(html.split())
    if len(text_snippet) > 500:
        text_snippet = text_snippet[:500]
    
    return text_snippet



def crawl_web(seed_url, requests_timeout, max_links, max_runtime, max_sleep, headers, user_agent_list, referer_list, db_name):
    """Crawls web for http links starting from seed url, creates index database out of valid requests, and returns all crawled links."""
    crawler = Crawler()
    scraper = Scraper()
    indexer = Indexer()
    queued_links = []
    crawled_links = []
    db_content = {}
    run_time = 0
    start_time = time.time()
    crawler.set_timeout(requests_timeout)
    crawler.set_headers(headers)
    response = crawler.get_response(seed_url)
    print("crawling web for links...")
    print("max links: " + str(max_links))
    print("max seconds: " + str(max_runtime))
    if crawler.check_validity(response):
        html = response.text
        page_links = scraper.scrape_links(html)
        page_links = remv_duplicates(page_links)
        queued_links = page_links
        crawled_links.append(seed_url)
        db_headers = dict(response.headers)
        db_headers['Page-Links'] = page_links
        text_snippet = get_snippet(response)
        db_headers['Text-Snippet'] = text_snippet
        db_content[seed_url] = db_headers
        indexer.gen_db(db_content, db_name)
        collected_links = 1
        print('content type: ' + str(db_headers.get('Content-Type')))

    else:
        print("start url invalid")
        exit(0)

    while len(queued_links) > 0:
        for lnk in queued_links:
            print("run time: " + str(int(run_time)) + " seconds")
            print("crawled links: " + str(len(crawled_links)))
            print("queued links: " + str(len(queued_links)))
            print("collected links: " + str(collected_links))
            print("time remaining: " + str(int(max_runtime - run_time)) + " seconds")
            db_content = {}
            crawler.set_random_user_agent(user_agent_list)
            crawler.set_random_referer(referer_list)
            response = crawler.get_response(lnk)
            if crawler.check_validity(response):
                html = response.text
                page_links = scraper.scrape_links(html)
                new_links = check_lists(page_links, crawled_links)
                queued_links = queued_links + new_links
                queued_links = remv_duplicates(queued_links)  
                db_headers = dict(response.headers)
                db_headers['Page-Links'] = page_links
                text_snippet = get_snippet(response)
                db_headers['Text-Snippet'] = text_snippet
                db_content[lnk] = db_headers
                existing_db = indexer.read_db(db_name)
                merged_db = indexer.merge_data(existing_db, db_content)
                indexer.save_db(merged_db, db_name)
                collected_links += 1
                print('content type: ' + str(db_headers.get('Content-Type')))
                print("Snippet: " + str(db_headers['Text-Snippet']))

            else:
                print("response invalid")

            current_time = time.time()
            run_time = current_time - start_time
            crawled_links.append(lnk)
            queued_links.remove(lnk)
            if len(crawled_links) >= max_links:
                print("max links crawled")
                return crawled_links
        
            elif run_time >= max_runtime:
                print("timeout")
                return crawled_links

            else:
                rand_sleep(max_sleep)
                pass

    return crawled_links


def dl_file(url, headers, dl_directory, redirects):
    """Downloads file from url."""
    crawler = Crawler()
    crawler.set_headers(headers)
    crawler.dl_file(url, dl_directory, redirects)

def dl_files(link_list, headers, dl_directory, redirects):
    """Downloads files from list of urls."""
    crawler = Crawler()
    crawler.set_headers(headers)
    for lnk in link_list:
        crawler.dl_file(lnk, dl_directory, redirects)

def gen_array(link_list, max_sleep, headers, user_agent_list, referer_list):
    """Parses response from link list and create array as: link[meta]."""
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
        crawler.set_random_referer(referer_list)
        rand_sleep(max_sleep)

    return db_content

def gen_db(db_content, db_name):
    """Generates a .json database from array."""
    indexer = Indexer()
    db = indexer.gen_db(db_content, db_name)
    return db


def read_db(db_name):
    """Reads .json database and returns array."""
    indexer = Indexer()
    db = indexer.read_db(db_name)
    return db

## Merge 2 databases ##
def merge_data(db1, db2):
    """Merges two .json databases together."""
    indexer = Indexer()
    db1_content = indexer.read_db(db1)
    db2_content = indexer.read_db(db2)
    merged_db = indexer.merge_data(db1_content, db2_content)
    return merged_db


def search_db(db1, db2, query):
    """Searches database and creates new one based on query."""
    indexer = Indexer()
    search_array = indexer.read_db(db1)
    
    if search_array == None:
        return None
    
    temp_array = {}
    for lnk in search_array:
        if query in lnk or query in search_array[lnk]:
            temp_array[lnk] = search_array[lnk]

        else:
            pass
    
    new_db = indexer.gen_db(temp_array, db2)

    return new_db

def gen_dl_db(db1, db2, downloadable_content):
    """Generates database containing downloadable links"""
    indexer = Indexer()
    search_array = indexer.read_db(db1)
    temp_array = {}
    for lnk in search_array:
        head = search_array[lnk]
        if head.get('Content-Type') in downloadable_content:
            temp_array[lnk] = search_array[lnk]

        else:
            pass

    new_db = indexer.gen_db(temp_array, db2)
    return new_db


def weigh_db(db1, db2):
    """Weights links in index database against one another."""
    indexer = Indexer()
    db_array = indexer.read_db(db1)
    for i1 in db_array:
        index_wgt = 0
        for i2 in db_array: 
            if i2 is not i1 and db_array[i2].get('Page-Links') is not None:
                for lnk in db_array[i2].get('Page-Links'):
                    if lnk == i1:
                        index_wgt += 1

        else:
            pass

        db_array[i1]['Index-Weight'] = index_wgt

    new_db = indexer.gen_db(db_array, db2)
    return new_db

                   
def get_html(url, headers):
    """Retrieves html from url."""
    crawler = Crawler()
    crawler.set_headers(headers)
    response = crawler. get_response(url)

    if check_response(response):
        html = response.text
        return html

    else:
        return None

def scrape_content(html, tag1, tag2):
    """Returns content between html elements."""
    scraper = Scraper()
    content = scraper.scrape_content(html, tag1, tag2)
    return content

def remove_content(html, tag1, tag2):
    """Removes content between html elements."""
    scraper = Scraper()
    html = scraper.remove_content(html, tag1, tag2)
    return html

def parse_elmnts(html):
    """Creates list of html elements from scraped text."""
    scraper = Scraper()
    elmnt_list = scraper.parse_elmnts(html)
    return elmnt_list

def scrape_elmnts(html):
    """Parses elements from html and return as text."""
    scraped_text = ""
    elmnt_list = parse_elmnts(html)
    for elmnt in elmnt_list:
        scraped_text += elmnt + "\n"

    return scraped_text

# Order is important here! Script tags should be filtered before style!
def filter_html(html, filter_html_scripts, filter_html_styles, scrape_html_elmnts, scrape_html_text, doc_name):
    scraper = Scraper()
    # remv_image_tags = False
    scraper.gen_elmnt_list(html)

    if html is None:
        return None
    
    if filter_html_scripts == True:
        print("removing content between script elements")
        html = scraper.remove_content(html, '<script', '</script>')
        scraper.gen_elmnt_list(html)

    if filter_html_styles == True:
        print("removing content between style elements")
        html = scraper.remove_content(html, '<style', '</style>')
        scraper.gen_elmnt_list(html)

    if scrape_html_elmnts == True:
        html = scrape_elmnts(html)
        
    if scrape_html_text == True:
        html = scraper.scrape_text(html)

    # if remv_image_tags == True:
    #     print("removing image tags")
    #     html = scraper.remove_tag(html, '<img')

    if len(doc_name) > 1:
        write_text(doc_name, html)
            
    return html

def gen_elmnt_matrix(elmnt_list):
    """Generates a matrix of html elements that can be searched based on <tag>."""
    scraper = Scraper()
    elmnt_matrix = scraper.gen_elmnt_matrix(elmnt_list)
    return elmnt_matrix
    
def gen_link_matrix(elmnt_matrix):
    """Creates new matrix out of links from element matrix."""
    scraper = Scraper()
    link_matrix = scraper.gen_link_matrix(elmnt_matrix)
    return link_matrix

def filter_tags(html, query):
    """Return html elements that contain a query"""
    scraper = Scraper()
    filtered_text = ""
    elmnt_list = scraper.parse_elmnts(html)
    elmnt_list = query_list(elmnt_list, query)
    for elmnt in elmnt_list:
        filtered_text += elmnt + "\n"

    return filtered_text

def remove_tags(html, query):
    """Remove html elements that contain a query."""
    scraper = Scraper()
    scraped_text = ""
    elmnt_list = scraper.parse_elmnts(html)
    elmnt_list = filter_list(elmnt_list, query)
    for elmnt in elmnt_list:
        scraped_text += elmnt

    return scraped_text


def search_tags(html, query, tag_name, clean_html_tags, get_tag_links):
    if clean_html_tags == True:
        html = remove_tags(html, '</')
        html = remove_tags(html, '![endif]')
        html = remove_tags(html, '<br')

    if len(query) > 0:
        html = filter_tags(html, query)
    elmnt_list = parse_elmnts(html)
    elmnt_matrix = gen_elmnt_matrix(elmnt_list)

    if get_tag_links == True:
        print("getting links!")
        link_matrix = gen_link_matrix(elmnt_matrix)
        matrix = link_matrix

    else:
        matrix = elmnt_matrix

    if tag_name in matrix:
        print(tag_name + " elements:")
        print_items(matrix[tag_name])

    elif len(tag_name) == 0:
        print("no tag given")
        print("available tags: ")
        print_items(matrix)

    else:
        print("tag not found")
        print("available tags: ")
        print_items(matrix)


def scrape_text(html):
    """Parses text from raw html."""
    scraper = Scraper()
    scraped_text = scraper.scrape_text(html)
    return scraped_text


def edit_text(text, cycle_config, sentmin, sentmax):
    """Edits text based on configuration settings."""
    editor = Editor()
    editor.create_sentc_list(text)
    if cycle_config['noalpha']:
        editor.remv_noalpha()

    if cycle_config['nodeclare']:
        editor.remv_nodeclare()

    if cycle_config['excaps']:
        editor.remv_excaps()

    if cycle_config['exletters']:
        editor.remv_exletters()

    if cycle_config['firstperson']:
        editor.remv_firstperson()

    if cycle_config['secondperson']:
        editor.remv_secondperson()

    if cycle_config['dupwords']:
        editor.remv_dupwords()

    if cycle_config['duplicates']:
        editor.remv_duplicates()

    if cycle_config['trimsentlist']:
        editor.trim_sentlist(sentmin, sentmax)

    if cycle_config['whitespace']:
        editor.remv_wtspace()

    # elif cycle == "checkspelling":
    #     editor.check_misspelled(dictionary)

    sentc_list = editor.get_sentc_list()    
    clean_text = ""
    for sentc in sentc_list:
        clean_text += sentc + " "
        
    return clean_text
