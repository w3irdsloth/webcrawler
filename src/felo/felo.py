 ########           
## FELO ##
#########

import argparse
import textwrap
import os

## Import Functions ##
from felo.functions import ( 
    get_response,
    check_response,
    crawl_web, 
    gen_headers, 
    gen_array, 
    gen_db, 
    read_db,
    merge_data,
    remove_content,
    remove_tags,
    scrape_content,
    parse_elmnts,
    scrape_elmnts,
    gen_elmnt_matrix,
    gen_link_matrix,
    filter_tags,
    scrape_text,
    read_text,
    write_text,
    edit_text,

    print_items,
    list_items,
)

## Import Settings ##
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
    filter_style_tags,
    filter_script_tags,
    clean_html_tags,
    scrape_elmnts_only,
    scrape_text_only,
    edit_cycle_config,
    default_txt_name,
    default_content_tag1,
    default_content_tag2,
    # default_search_tag,
    
)
## Build FELO ##
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
        self.edit_cycle_config = edit_cycle_config

    ## Run argument parser ##
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


        ## Parse Commands ##
        subparsers = parser.add_subparsers(title="commands", dest="command")

        command = subparsers.add_parser(name="get-status")
        command.add_argument("-url", "--url", action="store", dest="url", default=self.seed_url)

        command = subparsers.add_parser(name="crawl-web")
        command.add_argument("-url", "--url", action="store", dest="seed_url", default=self.seed_url)
        command.add_argument("-lnks", "--links", action="store", type=int, dest="max_links", default=self.max_crawl_links)
        command.add_argument("-tmt", "--timeout", action="store", type=int, dest="max_timeout", default=self.max_crawl_timeout)
        command.add_argument("-slp", "--sleep", action="store", type=int, dest="max_sleep", default=self.max_crawl_sleep)
        command.add_argument("-db", "--database", action="store", dest="db_name", default=self.default_db_name)

        command = subparsers.add_parser(name="merge-data")
        command.add_argument("-db1", "--database1", action="store", dest="db1", required=True)
        command.add_argument("-db2", "--database2", action="store", dest="db2", required=True)
        command.add_argument("-db", "--database", action="store", dest="db_name", default=self.default_db_name)

        command = subparsers.add_parser(name="print-links")
        command.add_argument("-db", "--database", action="store", dest="db_name", default=self.default_db_name)

        command = subparsers.add_parser(name="print-html")
        command.add_argument("-url", "--url", action="store", dest="url", default=self.seed_url)
        command.add_argument("-doc", "--docname", action="store", dest="doc_name", default="")

        command = subparsers.add_parser(name="read-text")
        command.add_argument("-doc", "--docname", action="store", dest="doc_name", default=default_txt_name)

        command = subparsers.add_parser(name="read-html")
        command.add_argument("-doc", "--docname", action="store", dest="doc_name", default=default_txt_name)
        command.add_argument("-tag", "--tagname", action="store", dest="tag_name", default="")
        command.add_argument("-lnks", "--getlinks", action="store_true", dest="get_links")
        command.add_argument("-qry", "--query", action="store", dest="query", default="")

        command = subparsers.add_parser(name="read-content")
        command.add_argument("-doc", "--docname", action="store", dest="doc_name", default=default_txt_name)
        command.add_argument("-tag1", "--tag1", action="store", dest="tag1", default=default_content_tag1)
        command.add_argument("-tag2", "--tag2", action="store", dest="tag2", default=default_content_tag2)

        command = subparsers.add_parser(name="edit-text")
        command.add_argument("-doc", "--docname", action="store", dest="doc_name", default=default_txt_name)
        command.add_argument("-edt", "--edits", action="store", dest="edited_doc", default="edits.txt")
        # command.add_argument("-edc", "--editcycle", action="store", dest="edit_cycle_config", default=self.edit_cycle_config)


        ## Parse Arguments ##
        args = parser.parse_args()

        # Crawl URL and return response
        if args.command == "get-status":
            url = args.url
            headers = gen_headers(self.headers_user_agent, self.headers_accept, self.headers_accept_language, self.headers_accept_encoding)
            response = get_response(url, headers)
            print(response.status_code)


        # Crawl web for links and generate index db
        if args.command == "crawl-web":
            seed_url = args.seed_url
            max_links = args.max_links
            max_timeout = args.max_timeout
            db_name = args.db_name
            headers = gen_headers(self.headers_user_agent, self.headers_accept, self.headers_accept_language, self.headers_accept_encoding)
            user_agent_list = self.user_agent_list
            link_list = crawl_web(seed_url, max_links, max_timeout, max_crawl_sleep, headers, user_agent_list)
            link_array = gen_array(link_list, max_crawl_sleep, headers, user_agent_list)
            gen_db(link_array, db_name)


        # Print links in database file
        if args.command == "print-links":
            db_name = args.db_name
            db = read_db(db_name)
            print_items(db)


        # Merge two database files
        if args.command == "merge-data":
            db1 = args.db1
            db2 = args.db2
            db_name = args.db_name
            merged_data = merge_data(db1, db2)
            gen_db(merged_data, db_name)


        # Make request and print html to console or file
        if args.command == "print-html":
            url = args.url
            doc_name = args.doc_name
            headers = gen_headers(self.headers_user_agent, self.headers_accept, self.headers_accept_language, self.headers_accept_encoding)
            response = get_response(url, headers)

            if check_response(response):
                html = response.text

            else:
                print("No response")
                exit(code=0)

            if filter_style_tags == True:
                print("removing content between style elements")
                html = remove_content(html, '<style', '</style>')

            if filter_script_tags == True:
                print("removing content between script elements")
                html = remove_content(html, '<script', '</script>')

            if scrape_elmnts_only == True:
                html = scrape_elmnts(html)
        
            if scrape_text_only == True:
                html = scrape_text(html)                 

            if len(doc_name) > 1:
                write_text(doc_name, html)
            
            else:
                print(html)


        # Is this really necessary? I mean there's echo/nano/etc...
        if args.command == "read-text":
            doc_name = args.doc_name
            text = read_text(doc_name)
            print(text)


        # Read html from doc, create matrix, and print elments
        if args.command == "read-html":
            doc_name = args.doc_name
            tag_name = args.tag_name
            get_links = args.get_links
            query = args.query
            html = read_text(doc_name)

            if clean_html_tags == True:
                html = remove_tags(html, '</')
                html = remove_tags(html, '![endif]')
                html = remove_tags(html, '<br')

            if len(query) > 0:
                html = filter_tags(html, query)
    
            elmnt_list = parse_elmnts(html)
            elmnt_matrix = gen_elmnt_matrix(elmnt_list)

            if get_links == True:
                print("getting links!")
                link_matrix = gen_link_matrix(elmnt_matrix)
                matrix = link_matrix

            else:
                matrix = elmnt_matrix

            if tag_name in matrix:
                print(tag_name + " elements:")
                print_items(matrix[tag_name])

            elif len(tag_name) == 0:
                print("no tag given")
                print("available tags: ")
                print_items(matrix)

            else:
                print("tag not found")
                print("available tags: ")
                print_items(matrix)


        # Read html from doc and print content between tags
        if args.command == "read-content":
            doc_name = args.doc_name
            tag1 = args.tag1
            tag2 = args.tag2
            html = read_text(doc_name)
            content = scrape_content(html, tag1, tag2)
            print(content)


        if args.command == "edit-text":
            doc_name = args.doc_name
            edited_doc = args.edited_doc
            # edit_cycle_config = args.edit_cycle_config
            text = read_text(doc_name)
            edited_text = edit_text(text, edit_cycle_config)
            print(edited_text)
            write_text(edited_doc, edited_text)


            


