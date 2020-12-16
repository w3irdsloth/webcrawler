 ##############
## Downloader ##
 ##############

import requests
import re
import time
import os

class Downloader(object):
    """ Creates an object for downloading files from the internet """
    def _init_(self):
        self.engine = ""
        self.url = ""

    def get_searchengine(self):
        return self.engine

    def set_searchengine(self, search_engine):
        self.engine = search_engine
    
    def split_filename(self, url):
        flname = os.path.split(url)[1]
        return flname

    def get_url(self):
        return self.url

    def set_url(self, url):
        self.url = url

    #Bulid url from query and page number
    def build_url(self, query, page):
        url = ""
        if self.engine == "ggl":
            qryreplc = query.replace(" ", "+")
            url = "https://google.com/search?start=" + str(page) + "&q=" + qryreplc
            self.url = url
        
        elif self.engine == "g_scholar":
            qryreplc = query.replace(" ", "+")
            url = "https://scholar.google.com/scholar?start=" + str(page) + "&q=" + qryreplc
            self.url = url

        else:
            print("engine not found")

    #Retreive HTML from url
    def scrape_html(self, headers):
        url = self.url
        html = requests.get(url, headers=headers)
        return html.text

    #Scrape HTML for links
    def find_links(self, html):
        links = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', html)
        return links

    #Parse links for  keyword
    def filter_links(self, links, parse_word):
        link_list = []
        for lnk in links:
            print(lnk)
            if parse_word in lnk:
                link_list.append(lnk)
                print(link_list)

        return link_list

    #Download files from parsed links
    def dl_links(self, links):
        wait_time = 2
        for lnk in links:
            try:
                print("attempting download from " + lnk + "...")
                r = requests.get(lnk)
                flname = self.split_filename(lnk)
                with open(flname, "wb") as f:
                    f.write(r.content)
                
                print("done")
                time.sleep(wait_time)

            except:
                print("file not found...")
                time.sleep(wait_time)
