
import re

class Scraper(object):

    # Scrape http links from html
    def scrape_links(self, html):
        print("parsing links...")
        links = []
        link_list = []
        try: 
            links = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', html)
            for lnk in links:
                if lnk not in link_list:
                    link_list.append(lnk)

            return link_list
        
        except:
            print("something went wrong")
            return None

    # Scrape text from html
    def scrape_text(self, html):
        html_text = ""
        # elmnt_list = re.findall(r'<[^<>]+>', html) 
        elmnt_list = self.parse_elmnts(html)
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
    

    # Return content from between html tags
    def scrape_content(self, html, tag1, tag2):
        content = ""
        elmnt_list = self.parse_elmnts(html)
        text_start = 0
        list_start = 0  
        for e in elmnt_list:
            if tag1 in e:
                list_index = elmnt_list.index(e, list_start)
                sub1 = e
                sub2 = tag2
                text_index1 = html.find(sub1, text_start)
                text_index2 = html.find(sub2, text_index1 + len(sub1))

                result = html[text_index1 + len(sub1): text_index2]
                content += result + "\n"

                list_start = list_index + 1
                text_start = text_index2 + len(sub2) - len(result)

        return content


    # Remove content from between html tags
    def remove_content(self, html, tag1, tag2):
        clean_text = html
        elmnt_list = self.parse_elmnts(html)
        text_start = 0
        list_start = 0  
        for e in elmnt_list:
            if tag1 in e:
                list_index = elmnt_list.index(e, list_start)
                sub1 = e
                sub2 = tag2
                text_index1 = clean_text.find(sub1, text_start)
                text_index2 = clean_text.find(sub2, text_index1 + len(sub1))
                result = clean_text[text_index1 + len(sub1): text_index2]
                clean_text = clean_text.replace(result, '')
                list_start = list_index + 1
                text_start = text_index2 + len(sub2) - len(result)

        return clean_text
    
    # def scrape_tags(self, elmnt_list, tag=""):
    #     new_list = []
    #     for elmnt in elmnt_list:
    #         if tag in elmnt:
    #             new_list.append(elmnt)

    #         else:
    #             pass

    #     return new_list

    # remove html elements that contain a tag
    # def remove_tags(self, elmnt_list, tag=""):
    #     new_list = []
    #     for elmnt in elmnt_list:
    #         if tag in elmnt:
    #             pass
            
    #         else:
    #             new_list.append(elmnt)

    #     return new_list
    
    # parse elements from html
    def parse_elmnts(self, html):
        try:
            elmnt_list = re.findall(r'<[^<>]+>', html)    
            return elmnt_list
        
        except:
            print("something went wrong")


    # return list of html elements that contain a tag
    def filter_elements(self, elmnt_list, tag=""):
        new_list = []
        for elmnt in elmnt_list:
            if tag in elmnt:
                try:
                    new_list.append(elmnt)

                except:
                    pass

        return new_list



    # Generate array of html elements based on tag type
    def gen_elmnt_matrix(self, elmnt_list):
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
    
    #Return links from element matrix based on tag
    def gen_link_matrix(self, elmnt_matrix):
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