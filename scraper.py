
import re


class Scraper(object):

    def parse_links(self, response):
        print("parsing links...")
        # #To use BeautifulSoup
        # soup = BeautifulSoup(response, 'html.parser')
        # links = []
        # for lnk in soup.find_all('a',  attrs={'href': re.compile("^http")}):
        #     link = lnk.get('href')
        #     if link not in links:
        #         links.append(link)
   
        # #To use regular expressions instead of beautiful soup
        links = []
        link_list = []
        try: 
            # links = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', response.text)
            links = re.findall(r'<[^<>]+>', response.text)
            for lnk in links:
                if lnk not in link_list:
                    link_list.append(lnk)

            return link_list
        
        except:
            print("something went wrong")


    # parse html tags from response
    def parse_elements(self, response):
        try:
            tag_list = re.findall(r'<[^<>]+>', response.text)    
            return tag_list
        
        except:
            print("something went wrong")

    # return html elements that contain a keyword
    def filter_elements(self, tag_list, query=""):
        new_list = []
        for tag in tag_list:
            if query in tag:
                try:
                    new_list.append(tag)

                except:
                    pass

        return new_list