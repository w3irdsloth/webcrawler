 ########           
## FELO ##
#########


from felo.commands import ( 
    crawl_url, 
    crawl_web, 
    gen_headers, 
    gen_array, 
    gen_db, 
    read_db, 
    print_items
)

from felo.settings import ( 
    seed_url, 
    max_crawl_links, 
    max_crawl_timeout, 
    max_crawl_sleep, 
    default_db_name, 
    requests_timeout, 
    headers_user_agent, 
    headers_accept, 
    headers_accept_language, 
    headers_accept_encoding, 
    user_agent_list,
)

import argparse
import textwrap
import os


class Felo(object):
    def __init__(self):
        self.seed_url = seed_url 
        self.max_crawl_links = max_crawl_links
        self.max_crawl_timeout = max_crawl_timeout 
        self.max_crawl_sleep = max_crawl_sleep
        self.default_db_name = default_db_name
        self.headers_user_agent = headers_user_agent
        self.headers_accept = headers_accept
        self.headers_accept_language = headers_accept_language
        self.headers_accept_encoding = headers_accept_encoding
        self.user_agent_list = user_agent_list

    def run(self):
        #Construct parsers
        parser = argparse.ArgumentParser( prog='FELO',
              formatter_class=argparse.RawDescriptionHelpFormatter,
              description=textwrap.dedent('''\
                          #       ###       #                      ######### 
                         ##   ###########   ##                   ###       ###     
                      ###########################              ###  Hello!  ###
                    ####  ###################  ####          ###  I'm FELO.   ###
                   #################################       ###      Your       ###
                  #############  FE^LO  #############     ###  Fellow Editor    ###       
                   #################################   #####         And         ###
                    ############ ###### ########### ####   ###  Logical Operator ### 
                      ###########      ###########           ###                ####
                              ############                     ##   ############
                               ##########                        ####    
        --------------------------------------------------------------
        *Commands go here:
        -------------------------------------------------------------- 
                 '''), epilog='''
        --------------------------------------------------------------
                                        ''')

        subparsers = parser.add_subparsers(title="commands", dest="command")

        crawl = subparsers.add_parser(name="get-status")
        crawl.add_argument("-url", "--url", action="store", dest="url", default=self.seed_url)

        crawl = subparsers.add_parser(name="crawl-web")
        crawl.add_argument("-url", "--url", action="store", dest="seed_url", default=self.seed_url)
        crawl.add_argument("-lnks", "--links", action="store", type=int, dest="max_links", default=self.max_crawl_links)
        crawl.add_argument("-tmt", "--timeout", action="store", type=int, dest="max_timeout", default=self.max_crawl_timeout)
        crawl.add_argument("-slp", "--sleep", action="store", type=int, dest="max_sleep", default=self.max_crawl_sleep)
        crawl.add_argument("-db", "--database", action="store", dest="db_name", default=self.default_db_name)

        printdb = subparsers.add_parser(name="print-db")
        printdb.add_argument("-db", "--database", action="store", dest="db_name", default=self.default_db_name)


        #set arguments
        args = parser.parse_args()

         #######
        ## web ##
         #######

        ## Crawl URL and return response
        if args.command == "get-status":
            url = args.url
            response = crawl_url(url)
            print(response.status_code)

        ## Crawl web for links and generate index db
        if args.command == "crawl-web":
            seed_url = args.seed_url
            max_links = args.max_links
            max_timeout = args.max_timeout
            db_name = args.db_name

            headers_user_agent = self.headers_user_agent
            headers_accept = self.headers_accept
            headers_accept_language = self.headers_accept_language
            headers_accept_encoding = self.headers_accept_encoding
            headers = gen_headers(headers_user_agent, headers_accept, headers_accept_language, headers_accept_encoding)
            user_agent_list = self.user_agent_list
            link_list = crawl_web(seed_url, max_links, max_timeout, max_crawl_sleep, headers, user_agent_list)

            headers = gen_headers(headers_user_agent, headers_accept, headers_accept_language, headers_accept_encoding)
            link_array = gen_array(link_list, max_crawl_sleep, headers, user_agent_list)
            gen_db(link_array, db_name)

        ## Print links in database file
        if args.command == "print-db":
            db_name = args.db_name
            db = read_db(db_name)
            print_items(db)

        
        ## Sort database links and output based on query
