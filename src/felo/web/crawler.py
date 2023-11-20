 ###########
## Crawler ##
 ###########

import requests
import random
# import time
import os

class Crawler(object):
    """ Creates an object for crawling html for web links """

    def __init__(self):
        self.headers = {}
        self.user_agent_list = []
        self.timeout = 5

    def set_timeout(self, time_out):
        self.timeout = time_out

    def get_timeout(self):
        return self.timeout
    
    def set_user_agent(self, user_agent):
        # self.headers_user_agent = user_agent
        self.headers['User-Agent'] = user_agent

    def set_random_user_agent(self, user_agent_list):
        random_user_agent = random.choice(user_agent_list)
        self.headers['User-Agent'] = random_user_agent
    
    def set_agent_list(self, user_agent_list):
        self.user_agent_list = user_agent_list
    
    def get_user_agent(self):
        return self.headers_user_agent
    
    def set_headers_accept(self, headers_accept):
        # self.headers_accept = headers_accept
        self.headers['Accept'] = headers_accept

    def get_headers_accept(self):
        return self.headers_accept
    
    def set_headers_language(self, accept_language):
        self.headers['Accept-Language'] = accept_language

    def get_headers_language(self):
        return self.headers_accept_language
    
    def set_headers_encoding(self, accept_encoding):
        self.headers['Accept-Encoding'] = accept_encoding
    
    def get_headers_encoding(self):
        return self.headers_accept_encoding

    def set_headers(self, headers):
        self.headers = headers

    def get_headers(self):
        return self.headers


    def check_validity(self, response):
        try:
            status_code = response.status_code
            if status_code != 200:
                return False

            else:
                return True
        except:
            return None

    # Get response from URL
    def get_response(self, url):
        print("scraping " + url + "...")
        try:
            response = requests.get(url, headers=self.headers, timeout=self.timeout)
            return response

        except requests.exceptions.Timeout:
            print("timeout")
            return None

        except requests.exceptions.TooManyRedirects:
            print("too many redirects")
            return None

        except requests.exceptions.HTTPError:
            print("HTTP error")
            return None

        except requests.exceptions.RequestException as e:
            print("request error: " + str(e))
            return None

        except:
            print("something went wrong")
            return None
        

    def get_head(self, url):
        print("scraping " + url + "...")
        try:
            response = requests.head(url, headers=self.headers, timeout=self.timeout)
            return response

        except requests.exceptions.Timeout:
            print("timeout")
            return None

        except requests.exceptions.TooManyRedirects:
            print("too many redirects")
            return None

        except requests.exceptions.HTTPError:
            print("HTTP error")
            return None

        except requests.exceptions.RequestException as e:
            print("request error: " + str(e))
            return None

        except:
            print("something went wrong")
            return None
        

    #Download file from url
    def dl_file(self, url, directory, redirects):
        # for lnk in links:
        filename = os.path.split(url)[1]
        print("downloading " + filename + "...")
        try:
            request = requests.get(url, allow_redirects=redirects, timeout=self.timeout)
            open(directory + filename, "wb").write(request.content)
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