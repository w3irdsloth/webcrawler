 ########           
## FELO ##
#########

import argparse
import textwrap
import os

from felo.settings import ( 
    crawl_seed_url, 
    max_crawl_links, 
    max_crawl_runtime, 
    max_crawl_sleep, 
    requests_timeout,
    headers_user_agent, 
    headers_accept, 
    headers_accept_language, 
    headers_accept_encoding,
    headers_referer,
    user_agent_list,
    referer_list,
    downloadable_content,
    default_dl_directory,
    default_db_name,
    default_link_db,
    filetype_handlers,
    filter_style_tags,
    filter_script_tags,
    clean_html_tags,
    scrape_elmnts_only,
    scrape_text_only,
    edit_cycle_config,
    default_txt_name,
    default_content_tag1,
    default_content_tag2,
    edit_sent_min,
    edit_sent_max,
    
)

from felo.functions import ( 
    get_response,
    check_response,
    crawl_web, 
    gen_headers, 
    # gen_array, 
    gen_db, 
    read_db,
    merge_data,
    search_db,
    gen_dl_db,
    dl_file,
    dl_files,
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
    read_file,
    write_text,
    edit_text,
    print_items,
    # list_items,
    
)

class Felo(object):
    """Constructs an object for editing files, evaluating data, and other logical operations"""

    def run(self):
        """Top level function that reads arguments and runs commands"""

        args = self.parse_arguments()
        if args.command == "get-status":
            """Get response status from url"""
            url = args.url
            headers = gen_headers(headers_user_agent, headers_accept, headers_accept_language, headers_accept_encoding, headers_referer)
            response = get_response(url, headers)
            if response is not None:
                print(response.status_code)

            else: 
                print("bad response")


        if args.command == "crawl-web":
            """Crawl web for links and index data"""
            seed_url = args.seed_url
            max_links = args.max_links
            max_runtime = args.max_runtime
            db_name = args.db_name
            headers = gen_headers(headers_user_agent, headers_accept, headers_accept_language, headers_accept_encoding, headers_referer)
            crawled_links = crawl_web(seed_url, requests_timeout, max_links, max_runtime, max_crawl_sleep, headers, user_agent_list, referer_list, db_name)
            print("crawled: " + str(crawled_links))


        if args.command == "print-links":
            """Print links in database"""
            db_name = args.db_name
            db = read_db(db_name)
            print_items(db)


        if args.command == "merge-data":
            """Merge two database files"""
            db1 = args.db1
            db2 = args.db2
            db_name = args.db_name
            merged_data = merge_data(db1, db2)
            gen_db(merged_data, db_name)

        if args.command == "dl-db":
            """Index downloadable links from database and create new database"""
            db_name = args.db_name
            new_db = args.new_db
            gen_dl_db(db_name, new_db, downloadable_content)

        if args.command == "dl-file":
            """Download file from link"""
            url = args.url
            redirects = args.redirects
            dl_directory = args.dl_directory
            headers = gen_headers(headers_user_agent, headers_accept, headers_accept_language, headers_accept_encoding, headers_referer)
            dl_file(url, headers, dl_directory, redirects)

        if args.command == "dl-files":
            """Download files from database"""
            link_db = args.link_db
            dl_directory = args.dl_directory
            redirects = args.redirects
            link_array = read_db(link_db)
            link_list = []

            for lnk in link_array:
                link_list.append(lnk)

            headers = gen_headers(headers_user_agent, headers_accept, headers_accept_language, headers_accept_encoding, headers_referer)
            dl_files(link_list, headers, dl_directory, redirects)
            

        if args.command == "print-html":
            """Make request and print html to console or file"""
            url = args.url
            doc_name = args.doc_name
            headers = gen_headers(headers_user_agent, headers_accept, headers_accept_language, headers_accept_encoding)
            response = get_response(url, headers)

            if check_response(response):
                html = response.text

            else:
                print("No response")
                exit(code=0)

            # Order is important here! Script tags should be filtered before style!
            if filter_script_tags == True:
                print("removing content between script elements")
                html = remove_content(html, '<script', '</script>')

            if filter_style_tags == True:
                print("removing content between style elements")
                html = remove_content(html, '<style', '</style>')

            if scrape_elmnts_only == True:
                html = scrape_elmnts(html)
        
            if scrape_text_only == True:
                html = scrape_text(html)                 

            if len(doc_name) > 1:
                write_text(doc_name, html)
            
            else:
                print(html)

        if args.command == "read-text":
            """Read content of .txt file"""
            doc_name = args.doc_name
            text = read_text(doc_name)
            print(text)

        if args.command == "read-file":
            """Read contents supported document"""
            doc_name = args.doc_name
            new_doc = args.new_doc
            text = read_file(doc_name, filetype_handlers)

            if len(new_doc) > 0:
                write_text(new_doc, text)

            else:
                print(text)


        if args.command == "read-html":
            """Read html from doc, create matrix, and print elements based on tag"""
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


        if args.command == "read-content":
            """Read html from doc and print content between tags"""
            doc_name = args.doc_name
            tag1 = args.tag1
            tag2 = args.tag2
            html = read_text(doc_name)
            content = scrape_content(html, tag1, tag2)
            print(content)


        if args.command == "edit-text":
            """Edit text based on configuration settings"""
            doc_name = args.doc_name
            edited_doc = args.edited_doc
            text = read_text(doc_name)
            edited_text = edit_text(text, edit_cycle_config, edit_sent_min, edit_sent_max)
            if len(edited_doc) > 0:
                write_text(edited_doc, edited_text)

            else:
                print(edited_text)


        #### Search through index file based on kw and return results ####
        if args.command == "search-db":
            db1 = args.db1
            db2 = args.db2
            query = args.query
            new_db = search_db(db1, db2, query)
            print(new_db)



    def parse_arguments(self):
        """Parse arguments based on user input"""

        parser = argparse.ArgumentParser( prog='FELO',
              formatter_class=argparse.RawDescriptionHelpFormatter,
              description=textwrap.dedent('''\
                                          
                          #       ###       #                      ######### 
                         ##   ###########   ##                   ###       ###     
                      ###########################              ###  Hello!  ###
                    ####  ###################  ####          ###              ###
                   #################################       ###     I'm FELO:    ###
                  #############  FE^LO  #############     ###   File Evaluator   ###       
                   #################################   #####         and         ###
                    ############ ###### ########### ####   ###  Logical Operator  ### 
                      ###########      ###########           ###                ####
                              ############                     ##   ############
                               ##########                        ####    
         
                 '''), epilog='''
        
                                        ''')

        subparsers = parser.add_subparsers(title="commands", dest="command")
        
        command = subparsers.add_parser(
            name="get-status", 
            help='Get response status from url',
            )
        
        command.add_argument(
            '-url', 
            '--url', 
            action='store', 
            dest='url', 
            default=crawl_seed_url, 
            help='url for request',
            )

        command = subparsers.add_parser(
            name="crawl-web", 
            help='Crawl web for links and index data',
            )
        
        command.add_argument(
            '-url', 
            '--url', 
            action='store', 
            dest='seed_url', 
            default=crawl_seed_url, 
            help='Initial seed url'
            )
        
        command.add_argument(
            '-lnks', 
            '--links', 
            action='store', 
            type=int, 
            dest='max_links', 
            default=max_crawl_links, 
            help='Max number of links to crawl',
            )
        
        command.add_argument(
            '-rtm', 
            '--runtime', 
            action='store', 
            type=int, 
            dest='max_runtime', 
            default=max_crawl_runtime, 
            help='Max time the crawl loop will run',
            )
        
        command.add_argument(
            '-slp', 
            '--sleep', 
            action='store', 
            type=int, 
            dest='max_sleep', 
            default=max_crawl_sleep, 
            help = 'Max amount of time to sleep between requests'
            )
        
        command.add_argument(
            '-db', 
            '--database', 
            action='store', 
            dest='db_name', 
            default=default_db_name, 
            help='Default name for database file',
            )
        
        command = subparsers.add_parser(
            name='merge-data', 
            help='Merge two database files',
            )
        
        command.add_argument(
            '-db1', 
            '--database1', 
            action='store', 
            dest='db1', 
            required=True,
            help='The name of the first database file to merge',
            )
        
        command.add_argument(
            '-db2', 
            '--database2', 
            action='store', 
            dest='db2', 
            required=True,
            help='The name of the second database file to merge',
            )
        
        command.add_argument(
            '-db', 
            '--database', 
            action='store', 
            dest='db_name', 
            default=default_db_name,
            help='The name of the merged database file',
            )

        command = subparsers.add_parser(
            name='print-links', 
            help='Print links from database file',
            )
        
        command.add_argument(
            '-db', 
            '--database', 
            action='store', 
            dest='db_name', 
            default=default_db_name,
            help='Database file to print links from'
            )

        command = subparsers.add_parser(
            name='print-html', 
            help='Make request to url and print html to console or file'
            )
        
        command.add_argument(
            '-url', 
            '--url', 
            action='store', 
            dest='url', 
            default=crawl_seed_url,
            help='url for request'
            )
        
        command.add_argument(
            '-doc', 
            '--docname', 
            action='store', 
            dest='doc_name', 
            default='',
            help='Name of document to print to'
            )

        command = subparsers.add_parser(
            name='read-text',
            help='Read content of .txt file',
            )
        
        command.add_argument(
            '-doc', 
            '--docname', 
            action='store', 
            dest='doc_name', 
            required=True,
            help='Text file to read',
            )

        command = subparsers.add_parser(
            name='read-file',
            help='Read a file if the filetype is supported',
            )
        
        command.add_argument(
            '-doc', 
            '--docname', 
            action='store', 
            dest='doc_name', 
            required=True,
            help='Name of document to read from',
            )
        
        command.add_argument(
            '-new', 
            '--newdoc', 
            action='store', 
            dest='new_doc', 
            default='',
            help='Name of document to save text into',
            )

        command = subparsers.add_parser(
            name='read-html',
            help='Read html from doc, create matrix, and print elements based on tag',
            )
        
        command.add_argument(
            '-doc', 
            '--docname', 
            action='store', 
            dest='doc_name', 
            default=default_txt_name,
            help='Document to read html from',
            )
        
        command.add_argument(
            '-tag', 
            '--tagname', 
            action='store', 
            dest='tag_name', 
            default='',
            help='Name of element tag to return',
            )
        
        command.add_argument(
            '-lnks', 
            '--getlinks', 
            action='store_true', 
            dest='get_links',
            help='Whether to download links from html',
            )
        
        command.add_argument(
            '-qry', 
            '--query', 
            action='store', 
            dest='query', 
            default='',
            help='Search query for filtering elements',
            )

        command = subparsers.add_parser(
            name='read-content', 
            help='Read content between two html elements based on tags',
            )
        
        command.add_argument(
            '-doc', 
            '--docname', 
            action='store', 
            dest='doc_name', 
            default=default_txt_name,
            help='Name of document to read',
            )
        
        command.add_argument(
            '-tag1', 
            '--tag1', 
            action='store', 
            dest='tag1', 
            default=default_content_tag1,
            help='First tag to index',
            )
        
        command.add_argument(
            '-tag2', 
            '--tag2', 
            action='store', 
            dest='tag2', 
            default=default_content_tag2,
            help='Second tag to index',
            )

        command = subparsers.add_parser(
            name='edit-text', 
            help='Edit text based on configuration settings'
            )
        
        command.add_argument(
            '-doc', 
            '--docname', 
            action='store', 
            dest='doc_name', 
            default=default_txt_name,
            help='Name of document to read',
            )
        
        command.add_argument(
            '-edt', 
            '--edits', 
            action='store', 
            dest='edited_doc', 
            default='',
            help='Name of document to save edited text',
            )
        
        command = subparsers.add_parser(
            name='dl-db', 
            help='Index downloadable links from database and create new database',
            )
        
        command.add_argument(
            '-db', 
            '--database', 
            action='store', 
            dest='db_name', 
            default=default_db_name,
            help='Name of database to read'
            )
        
        command.add_argument(
            '-new', 
            '--newdb', 
            action='store', 
            dest='new_db', 
            default=default_link_db,
            help='Name of new database',
            )

        command = subparsers.add_parser(
            name='dl-file', 
            help='Download single file from url',
            )
                                        
        command.add_argument(
            '-url', 
            '--url', 
            action='store', 
            dest='url', 
            default=crawl_seed_url,
            help='url to download from',
            )
        
        command.add_argument(
            '-dir', 
            '--directory', 
            action='store', 
            dest='dl_directory', 
            default=default_dl_directory,
            help='Directory to download files to',
            )
        
        command.add_argument(
            '-rds', 
            '--redirects', 
            action='store_true', 
            dest='redirects', 
            default=True,
            help='Whether requests should allow redirects',
            )

        command = subparsers.add_parser(name='dl-files',
                                        help='Download files from links in a database',
                                        )


        command.add_argument(
            '-db', 
            '--database', 
            action='store', 
            dest='link_db', 
            default=default_link_db,
            help='Database file to query for links',
            )
        
        command.add_argument(
            '-dir', 
            '--directory', 
            action='store', 
            dest='dl_directory', 
            default=default_dl_directory,
            help='Directory to download files to',
            )
        
        command.add_argument(
            '-rds', 
            '--redirects', 
            action='store_true', 
            dest='redirects', 
            default=True,
            help='Whether requests should allow redirects',
            )

        command = subparsers.add_parser(name='search-db',
                                        help='Search database file and return results',
                                        )
        
        command.add_argument(
            '-db1', 
            '--database1', 
            action='store', 
            dest='db1', 
            required=True,
            help='The name of the database file to search',
            )
        
        command.add_argument(
            '-db2', 
            '--database2', 
            action='store', 
            dest='db2', 
            required=True,
            help='The name of the new database file',
            )

        command.add_argument(
            '-qry', 
            '--query', 
            action='store', 
            dest='query', 
            default='',
            help='Search query for filtering content',
            )

        
        args = parser.parse_args()
        return args