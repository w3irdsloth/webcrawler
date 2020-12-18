 ##############
## Downloader ##
 ##############

import requests
import re
import time
import os

from bs4 import BeautifulSoup

class Downloader(object):
    """ Creates an object for downloading files from the internet """
    def _init_(self):
        self.engine = ""

    def set_searchengine(self, search_engine):
        self.engine = search_engine

    #Bulid url from query and page number
    def build_url(self, query, page):
        url = ""
        if self.engine == "ggl":
            qryreplc = query.replace(" ", "+")
            url = "https://google.com/search?start=" + str(page) + "&q=" + qryreplc
            return url
        
        elif self.engine == "g_scholar":
            qryreplc = query.replace(" ", "+")
            url = "https://scholar.google.com/scholar?start=" + str(page) + "&q=" + qryreplc
            return url

        else:
            print("engine not found")

    #Scrape HTML from url
    def scrape_html(self, url, headers):
        html = requests.get(url, headers=headers)
        return html.text

    #Scrape html for text
    def scrape_text(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        text = soup.text
        return text

    #Scrape HTML for links
    def scrape_links(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        links = []
        for link in soup.find_all('a'):
            link = link.get('href')
            if "http" in link:
                links.append(link)
   
        # #To use regular expressions instead of beautiful soup      
        # links = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', html)
        return links

    #Parse links for  keyword
    def filter_links(self, links, parse_word):
        link_list = []
        for lnk in links:
            if parse_word in lnk:
                link_list.append(lnk)

        return link_list

    #Download files from links
    def dl_links(self, links):
        wait_time = 2
        for lnk in links:
            try:
                print("attempting download from " + lnk + "...")
                r = requests.get(lnk)
                flname = os.path.split(lnk)[1]
                with open(flname, "wb") as f:
                    f.write(r.content)
                
                print("done")
                time.sleep(wait_time)

            except:
                print("file not found...")
                time.sleep(wait_time)



