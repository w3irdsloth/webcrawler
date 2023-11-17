 ###########
## Crawler ##
 ###########

import requests
import random

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

    def set_agent_list(self, user_agent_list):
        self.user_agent_list = user_agent_list
    
    def set_random_user_agent(self, user_agent_list):
        random_user_agent = random.choice(user_agent_list)
        self.headers['User-Agent'] = random_user_agent
    
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

    # def gen_headers(self):
    #     headers = {'User-Agent': self.user_agent,
    #             'Accept': self.headers_accept,
    #             'Accept-Language': self.accept_language,
    #             'Accept-Encoding': self.accept_encoding}

    #     self.headers = headers

    def set_headers(self, headers):
        self.headers = headers

    def get_headers(self):
        return self.headers


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





