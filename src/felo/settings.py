#### FELO SETTINGS ####
## Path to project ##
# project_path = "/home/n0xs1/projects/felo"

## Argparse Defaults ##
# Maximum number of links to crawl before stopping
max_crawl_links = 5

# Maximum seconds crawler should operate before timing out 
max_crawl_timeout = 360

# Maximum wait between crawl requests
max_crawl_sleep = 3

# Default path/name for index database
default_db_name = "/home/n0xs1/projects/felo/tests/db.json"

# Default path/name for creating/reading .txt files
default_txt_name = "/home/n0xs1/projects/felo/tests/test.txt"


## Crawler Defaults ##
# Timeout for making requests in seconds
requests_timeout = 5

# Initial URL for crawler
# seed_url = 'https://www.duckduckgo.com'
# seed_url = 'https://www.yahoo.com'
# seed_url = 'https://www.google.com'
# seed_url = 'https://www.yandex.com'
seed_url = "https://stackoverflow.com/questions/65173291/git-push-error-src-refspec-main-does-not-match-any-on-linux"
# seed_url = "https://www.geeksforgeeks.org/python-merging-two-dictionaries/"
# seed_url = "https://www.w3schools.com/html/html_comments.asp"
# seed_url = "https://blablabla.com"

# Default header configuration
headers_user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
headers_accept = 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
headers_accept_language = 'en-US,en;q=0.9'
headers_accept_encoding = 'default'

# A list of user agents to pass into the headers
user_agent_list = ['Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
                    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
                    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
                    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
                    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
                    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15',
                    'Mozilla/5.0 (Macintosh; Intel Mac OS X 13_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15']



## Elements to remove from crawled text ##
# Leave these all False to return only html #

# text_only will return javascript functions, style elements, etc if these are set to False)
filter_style_tags = True
filter_script_tags = True


# Setting both of these True will result in no text returned
scrape_elmnts_only = False
scrape_text_only = True



## Elements to remove from indexed text ##

# Removes ['</', '![endif]', '<br')] tags
clean_html_tags = True


## Return content between tags ##

# Not super useful. Maybe for pulling out javascript
default_content_tag1 = "<script"
default_content_tag2 = "</script>"

# Edit cycle list

edit_cycle_config = {
    "noalpha": True, 
    "nodeclare": True, 
    "excaps": True, 
    "exletters": True, 
    "firstperson": True, 
    "secondperson": True, 
    "dupwords": True, 
    "duplicates": True, 
    "trimsentlist": True, 
    "checkspelling": True,
}
