 ###########
## Crawler ##
 ###########

import requests
import random
import os

class Crawler(object):
    """Constructs an object for crawling html for web links.
    
    Attributes
    ----------
    headers: dict
        headers data to pass into requests
    timeout: int
        timeout for requests in seconds

    """

    def __init__(self):
        """Constructs the necessary attributes for the Crawler object."""
        self.timeout = 5
        self.headers = {
            'User-Agent': '',
            'Accept': '',
            'Accept-Language': '',
            'Accept-Encoding': '',
            'Referer': '',
        }

    def set_timeout(self, time_out):
        """Sets the timeout for requests in seconds."""
        self.timeout = time_out

    def get_timeout(self):
        """Returns the timeout for requests."""
        return self.timeout
    
    def set_user_agent(self, user_agent):
        """Sets 'User-Agent' for requests headers."""
        self.headers['User-Agent'] = user_agent

    def set_random_user_agent(self, user_agent_list):
        """Sets random 'User-Agent' for requests headers.

        Parameters
        ----------
        user_agent_list: list
            list of user agents

        """
        random_user_agent = random.choice(user_agent_list)
        self.headers['User-Agent'] = random_user_agent
    
    def get_user_agent(self):
        """Returns 'User-Agent' for requests headers."""
        return self.headers['User-Agent']
    
    def set_headers_accept(self, headers_accept):
        """Sets 'Accept' for requests headers."""
        self.headers['Accept'] = headers_accept

    def get_headers_accept(self):
        """Returns 'Accept' for requests headers."""
        return self.headers['Accept']
    
    def set_headers_language(self, accept_language):
        """Sets 'Accept-Language' for requests headers."""
        self.headers['Accept-Language'] = accept_language

    def get_headers_language(self):
        """Returns 'Accept-Language' for requests headers."""
        return self.headers['Accept-Language']
    
    def set_headers_encoding(self, accept_encoding):
        """Sets 'Accept-Encoding' for requests headers."""
        self.headers['Accept-Encoding'] = accept_encoding
    
    def get_headers_encoding(self):
        """Returns 'Accept-Encoding' for requests headers"""
        return self.headers['Accept-Encoding']
    
    def set_headers_referer(self, referer):
        """Sets 'Referer' for requests headers."""
        self.headers['Referer'] = referer


    def set_random_referer(self, referer_list):
        """Sets random 'referer' for requests headers.

        Parameters
        ----------
        referer_list: list
            list of referers

        """
        random_referer = random.choice(referer_list)
        self.headers['Referer'] = random_referer

    def get_referer(self):
        return self.headers['Referer']

    def set_headers(self, headers):
        """Sets requests headers.
        
        Parameters
        ----------
        headers: dict
            dictionary of headers values
        
        """
        self.headers = headers

    def get_headers(self):
        """Returns requests headers"""
        return self.headers


    def check_validity(self, response):
        """Checks the validity of an http request.
        
        Parameters
        ----------
        response: http response
            response value from http request
        
        """
        try:
            status_code = response.status_code
            if status_code != 200:
                return False

            else:
                return True
        except:
            return None

    def get_response(self, url):
        """Requests response from a url."""
        print("requesting response from " + url + "...")
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
        """Requests head from a url"""
        print("requesting head data from " + url + "...")
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
        
    def dl_file(self, url, directory, redirects):
        """Downloads a file from a url."""
        filename = os.path.split(url)[1]
        print("downloading " + filename + "...")
        try:
            request = requests.get(url, headers=self.headers, allow_redirects=redirects, timeout=self.timeout)
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