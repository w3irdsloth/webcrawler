 ##############
## Downloader ##
 ##############

import requests
import re
import time
import os

# from bs4 import BeautifulSoup

class Downloader(object):
    """ Creates an object for downloading files from the internet """

    def _init_(self):
        self.engine = ""

    def set_searchengine(self, search_engine):
        self.engine = search_engine

    def set_waittime(self, wait_time):
        self.wait_time = wait_time

    #Bulid url from query and page number
    def build_url(self, query, page):
        url = ""
        if self.engine == "ggl":
            print("building url for page " + str(page) + "...")
            i = page
            i = (i - 1) * 10
            qry_string = query.replace(" ", "+")
            url = "https://google.com/search?start=" + str(page) + "&q=" + qry_string
            return url
        
        elif self.engine == "g_scholar":
            print("building url for page " + str(page) + "...")
            i = page
            i = (i - 1) * 10
            qry_string = query.replace(" ", "+")
            url = "https://scholar.google.com/scholar?start=" + str(i) + "&q=" + qry_string
            return url

        else:
            print("engine not found")

    #Scrape HTML from url
    def scrape_html(self, url, headers):
        print("scraping " + url + "...")
        html = ""
        try:
            html = requests.get(url, headers=headers, timeout=5)
            time.sleep(self.wait_time)
            return html

        except requests.exceptions.Timeout:
            print("timeout")

        except requests.exceptions.TooManyRedirects:
            print("too many redirects")

        except requests.exceptions.HTTPError:
            print("HTTP error")

        except requests.exceptions.RequestException as e:
            print("request error: " + str(e))
            pass

    # #Scrape text from html
    # def scrape_text(self, html):
    #     print("scraping text...")
    #     soup = BeautifulSoup(html, 'html.parser')
    #     text = soup.text
    #     return text

    #Scrape html for links
    def scrape_links(self, html):
        print("scraping links...")
        # #To use BeautifulSoup
        # soup = BeautifulSoup(html, 'html.parser')
        # links = []
        # for lnk in soup.find_all('a',  attrs={'href': re.compile("^http")}):
        #     link = lnk.get('href')
        #     if link not in links:
        #         links.append(link)
   
        # #To use regular expressions instead of beautiful soup
        link_list = []      
        links = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', html)
        for lnk in links:
            if lnk not in link_list:
                link_list.append(lnk)
        
        return link_list

    #Filter links for files
    def filter_links(self, links, filetypes):
        link_list = []
        for lnk in links:
            print("querying " + lnk + "...")
            try:
                r = requests.head(lnk)
                headers = r.headers
                content_type = headers.get('Content-Type')
                time.sleep(self.wait_time)
                print("content type:")
                print(content_type)
                
                for fltp in filetypes:
                    if content_type != None and fltp in content_type:
                        link_list.append(lnk)
                        print("file added to queue...")
                        break

            except requests.exceptions.Timeout:
                print("timeout")

            except requests.exceptions.TooManyRedirects:
                print("too many redirects")

            except requests.exceptions.HTTPError:
                print("HTTP error")

            except requests.exceptions.RequestException as e:
                print("request error: " + str(e))
                pass

        return link_list

    #Download files from links
    def dl_links(self, links):
        for lnk in links:
            filename = os.path.split(lnk)[1]
            print("downloading " + filename + "...")
            try:
                r = requests.get(lnk, allow_redirects=True, timeout=5)
                open(filename, "wb").write(r.content)
                time.sleep(self.wait_time)
                print("done")

            except requests.exceptions.Timeout:
                print("timeout")

            except requests.exceptions.TooManyRedirects:
                print("too many redirects")

            except requests.exceptions.HTTPError:
                print("HTTP error")

            except requests.exceptions.RequestException as e:
                print("requst error: " + str(e))
                pass



