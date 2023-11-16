
import re


class Scraper(object):

    # Parse http links from html response
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
            links = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', html)
            # links = re.findall(r'<[^<>]+>', html)
            for lnk in links:
                if lnk not in link_list:
                    link_list.append(lnk)

            return link_list
        
        except:
            print("something went wrong")


    # Remove elements from between 2 html tags
    def remove_text(self, html, tag1, tag2):
        clean_text = html
        elmnt_list = re.findall(r'<[^<>]+>', html)
        text_start = 0
        list_start = 0

        for e in elmnt_list:
            if tag1 in e:
            # try:
                list_index = elmnt_list.index(e, list_start)
                sub1 = e
                sub2 = tag2

                # list_index2 = elmnt_list.index[tag2, list_index]

                text_index1 = clean_text.find(sub1, text_start)
                text_index2 = clean_text.find(sub2, text_index1 + len(sub1))
                result = clean_text[text_index1 + len(sub1): text_index2]
                # print(result)
                clean_text = clean_text.replace(result, '')
                # print(clean_text)
                
                # result_index = html.find(result, text_index1 + len(sub1))                    
                # clean_text = clean_text[:result_index - 1] + clean_text[result_index + len(result):]
                list_start = list_index + 1
                text_start = text_index2 + len(sub2) - len(result)

                # except:
                #     pass

        return clean_text


    # Parse text from html
    def parse_text(self, html):
        html_text = ""
        elmnt_list = re.findall(r'<[^<>]+>', html) 
        text_start = 0
        list_start = 0

        for e in elmnt_list:
            try:
                list_index = elmnt_list.index(e, list_start)
                sub1 = e
                sub2 = elmnt_list[list_index + 1]

                text_index1 = html.find(sub1, text_start)
                text_index2 = html.find(sub2, text_index1 + len(sub1))

                result = html[text_index1 + len(sub1): text_index2]
                html_text = html_text + result

                list_start = list_index + 1
                text_start = text_index1 + len(sub1)

            except:
                pass

        return html_text
    


    # parse html elements from response
    def parse_elements(self, html):
        try:
            elmnt_list = re.findall(r'<[^<>]+>', html)    
            return elmnt_list
        
        except:
            print("something went wrong")


    # return list of html elements that contain a keyword
    def filter_elements(self, elmnt_list, query=""):
        new_list = []
        for elmnt in elmnt_list:
            if query in elmnt:
                try:
                    new_list.append(elmnt)

                except:
                    pass

        return new_list

    # remove html elements that contain a keyword from list
    def clean_elements(self, elmnt_list, query=""):
        new_list = []
        for elmnt in elmnt_list:
            if query in elmnt:
                pass
            
            else:
                new_list.append(elmnt)

        return new_list


    # Generate array of html elements based on tag type
    def elmnt_matrix(self, elmnt_list):
        elmnt_matrix = {}
        for elmnt in elmnt_list:
            split_elmnt = elmnt.split()
            tag = split_elmnt[0]
            clean_tag = re.sub("[^a-zA-Z\s]+", "", tag)

            if clean_tag.isalpha():
                pass

            else:
                clean_tag = "other"      

            if clean_tag in elmnt_matrix:
                elmnt_matrix[clean_tag].append(elmnt)
            
            elif clean_tag not in elmnt_matrix:
                elmnt_matrix[clean_tag] = [elmnt]

        return elmnt_matrix
    

    def link_matrix(self, elmnt_matrix):
        link_matrix = {}
        for t in elmnt_matrix:
            tag_list = elmnt_matrix[t]
            tag_text = ''.join(tag_list)
            tag_links = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', tag_text)
            new_links = []

            for lnk in tag_links:
                if lnk not in new_links:
                    new_links.append(lnk)

                else:
                    pass
                
            link_matrix[t] = new_links

        return link_matrix