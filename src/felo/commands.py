from felo.web.crawler import Crawler
from felo.web.scraper import Scraper
from felo.web.indexer import Indexer

# from editor.applicator import Applicator

import time
import random


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



   ##########
#### office ####
   ##########





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

def rand_user_agent(user_agent_list):
    crawler = Crawler()
    crawler.set_random_user_agent(user_agent_list)
    new_headers = crawler.get_headers()
    return new_headers

def crawl_url(url, headers):
    crawler = Crawler()
    crawler.set_headers(headers)
    response = crawler.get_response(url)
    return response

def crawl_head(url, headers):
    crawler = Crawler()
    crawler.set_headers(headers)
    response = crawler.get_head(url)
    return response

def scrape_links(html):
    scraper = Scraper()
    scraped_links = scraper.parse_links(html)
    return scraped_links

def check_validity(response):
    try:
        status_code = response.status_code
        if status_code != 200:
            return False

        else:
            return True
    except:
        return None

def crawl_web(start_url, max_links, max_timeout, max_sleep, headers, user_agent_list):
    print("crawling web for links...")
    print("max links: " + str(max_links))
    print("max seconds: " + str(max_timeout))

    crawled_links = []
    start_time = time.time()
    run_time = 0

    response = crawl_url(start_url, headers)
    if check_validity(response):
        html = response.text
        queued_links = scrape_links(html)
        queued_links = remv_duplicates(queued_links)

    else:
        print("start url returned no response")
        exit(0)

    for lnk in queued_links:
        headers = rand_user_agent(user_agent_list)
        response = crawl_url(lnk, headers)

        if check_validity(response):
            html = response.text
            temp_links = scrape_links(html)
            queued_links = queued_links + temp_links
            queued_links = remv_duplicates(queued_links)
            current_time = time.time()
            run_time = current_time - start_time
        
            print("run time: " + str(run_time))
            print("num links: " + str(len(crawled_links)))
            print("time remaining: " + str(max_timeout - run_time))
        
            crawled_links.append(lnk)

        queued_links.remove(lnk)

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

## Parse response from link list and create array as: link[meta] ##
def gen_array(link_list, max_sleep, headers, user_agent_list):
    db_content = {}
    for lnk in link_list:
        if lnk not in db_content:
            response = crawl_head(lnk, headers)
            if check_validity(response):
                db_headers = dict(response.headers)
                db_content[lnk] = db_headers

            else:
                print("response invalid")

        else:
            print("link exists")
        
        headers = rand_user_agent(user_agent_list)
        rand_sleep(max_sleep)

    return db_content

def gen_db(db_content, db_name):
    indexer = Indexer()
    indexer.create_db(db_content, db_name)


def read_db(db_name):
    indexer = Indexer()
    db = indexer.read_db(db_name)
    return db

