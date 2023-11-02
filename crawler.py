 ###########
## Crawler ##
 ###########

import requests
import random
import re

# import time
# import os
# from bs4 import BeautifulSoup


##-- Move to config file --##
sleep_time = 5
timeout = 5

# Header configuration
headers_user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
headers_accept = 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
headers_accept_language = 'en-US,en;q=0.9'
# headers_accept_encoding = 'gzip, deflate, br'
headers_accept_encoding = 'default'

user_agent_list = ['Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
                    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
                    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
                    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
                    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
                    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15',
                    'Mozilla/5.0 (Macintosh; Intel Mac OS X 13_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15']

##-- End --##

class Crawler(object):
    """ Creates an object for crawling html for web links """

    def __init__(self):
        self.sleep_time = sleep_time
        self.timeout = timeout
        self.headers_user_agent = headers_user_agent
        self.headers_accept = headers_accept
        self.headers_accept_language = headers_accept_language
        self.headers_accept_encoding = headers_accept_encoding
        self.headers = {'User-Agent': self.headers_user_agent,
            'Accept': self.headers_accept,
            'Accept-Language': self.headers_accept_language,
            'Accept-Encoding': self.headers_accept_encoding}

        # self.url = url        
        # self.html = ""
        # self.link_list = []

    def set_sleep(self, sleep_time):
        self.sleep_time = sleep_time
    
    def set_random_sleep(self):
        self.sleep_time = random.randrange(1,5)
    
    def get_sleep(self):
        return self.sleep_time

    def set_timeout(self, time_out):
        self.timeout = time_out

    def get_timeout(self):
        return self.timeout

    def set_url(self, url):
        self.url = url

    def get_url(self):
        return self.url
    
    def set_user_agent(self, user_agent):
        self.headers_user_agent = user_agent
        self.headers['User-Agent'] = self.headers_user_agent
    
    def set_random_user_agent(self):
        # max_range = len(user_agent_list) + 1
        # for i in range(1, max_range):
        self.headers_user_agent = random.choice(user_agent_list)
        self.headers['User-Agent'] = self.headers_user_agent
    
    def get_user_agent(self):
        return self.headers_user_agent

    def get_headers_accept(self):
        return self.headers_accept

    def get_headers_accept_language(self):
        return self.headers_accept_language
    
    def get_headers_accept_encoding(self):
        return self.headers_accept_encoding

    # def set_headers(self, headers):
    #     self.headers=headers

    # def gen_headers(self):
    #     self.headers = {'User-Agent': self.headers_user_agent,
    #         'Accept': self.headers_accept,
    #         'Accept-Language': self.headers_accept_language,
    #         'Accept-Encoding': self.headers_accept_encoding}

    def get_headers(self):
        return self.headers
    
    def get_html(self):
        return self.html
    
    def get_link_list(self):
        return self.link_list

    #Scrape HTML from URL
    def scrape_html(self, url):
        print("scraping " + url + "...")
        html = ""
        try:
            html = requests.get(url, headers=self.headers, timeout=self.timeout)
            return html

        except requests.exceptions.Timeout:
            print("timeout")

        except requests.exceptions.TooManyRedirects:
            print("too many redirects")

        except requests.exceptions.HTTPError:
            print("HTTP error")

        except requests.exceptions.RequestException as e:
            print("request error: " + str(e))

        except:
            print("something went wrong")
    
    #Scrape metadata from URL
    def parse_response(self, url):
        print("parsing metadata...")
        meta = ""
        try:
            meta = requests.head(url)
            return meta

        except requests.exceptions.Timeout:
            print("timeout")

        except requests.exceptions.TooManyRedirects:
            print("too many redirects")

        except requests.exceptions.HTTPError:
            print("HTTP error")

        except requests.exceptions.RequestException as e:
            print("request error: " + str(e))
        
        except:
            print("something went wrong")

    # Parse links from html
    def parse_links(self, html):
        print("parsing links...")
        # #To use BeautifulSoup
        # soup = BeautifulSoup(html, 'html.parser')
        # links = []
        # for lnk in soup.find_all('a',  attrs={'href': re.compile("^http")}):
        #     link = lnk.get('href')
        #     if link not in links:
        #         links.append(link)
   
        # #To use regular expressions instead of beautiful soup
        links = []
        link_list = []
        try: 
            links = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', html.text)
            for lnk in links:
                if lnk not in link_list:
                    link_list.append(lnk)

            return link_list
        
        except:
            print("something went wrong")

    
 