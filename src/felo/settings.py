#### FELO SETTINGS ####
"""Default settings for Felo object commands."""

# Maximum number of links to crawl before stopping
max_crawl_links = 1000

# Maximum seconds crawler should operate before timing out 
max_crawl_runtime = 3600 * 3

# Maximum wait between crawl requests
max_crawl_sleep = 3

# Default path/name for db
default_db_name = "newtest.json"

# Default link db name
default_link_db = "linkdb.json"

# Default path/name for creating/reading .txt files
default_txt_name = "test.txt"


# Default download directory
default_dl_directory = "/home/n0xs1/projects/felo/tests/downloads/"

# Timeout for making requests in seconds
requests_timeout = 5

# Initial URL for crawler
# seed_url = 'https://www.duckduckgo.com'
# seed_url = 'https://www.yahoo.com'
# seed_url = 'https://www.google.com'
# seed_url = 'https://www.yandex.com'
crawl_seed_url = "https://stackoverflow.com/questions/65173291/git-push-error-src-refspec-main-does-not-match-any-on-linux"
# seed_url = "https://www.geeksforgeeks.org/python-merging-two-dictionaries/"
# seed_url = "https://www.w3schools.com/html/html_comments.asp"
# seed_url = "https://blablabla.com"

# Default header configuration
headers_user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
headers_accept = 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
headers_accept_language = 'en-US,en;q=0.9'
headers_accept_encoding = 'default'
headers_referer = 'https://www.duckduckgo.com'

# A list of user agents to pass into the headers
user_agent_list = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 13_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15'
    ]

referer_list = [
    'https://www.duckduckgo.com',
    'https://www.yahoo.com',
    'https://www.google.com',
    'https://www.yandex.com',
    'https://www.bing.com',
    'https://www.startpage.com/',
    'https://www.baidu.com/',

]

## Elements to remove from crawled text ##
# Leave these all False to return only html #

# text_only will return javascript functions, style elements, etc if these are set to False)
# Filtering out style tags before script tags may cause issues!
filter_script_tags = True
filter_style_tags = True


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


# List of content-types to download
downloadable_content = [
    # Images
    'image/gif',
    'image/jpeg',
    'image/png',
    'image/tiff',
    'image/vnd.microsoft.icon',
    'image/x-icon',
    'image/vnd.djvu',
    'image/svg+xml',  

    # Audio
    'audio/mpeg',
    'audio/x-ms-wma',
    'audio/vnd.rn-realaudio',
    'audio/x-wav',

    # Video
    'video/mpeg',
    'video/mp4',
    'video/quicktime',
    'video/x-ms-wmv',
    'video/x-msvideo',
    'video/x-flv',
    'video/webm',

    # Applications
    'application/ogg',
    'application/pdf',
    'application/json',
    'application/ld+json',
    'application/xml',
    'application/zip',
    
    ]

# Default filetype handlers
filetype_handlers = {
    ".doc":"docx",
    ".pdf":"pdftotext",
    # ".pdf":"pymupdf",

}


## Editor ##

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
    "checkspelling": False,
}

# Min and max sentence length for 'trimsentlist' cycle
edit_sent_min = 1
edit_sent_max = 50 