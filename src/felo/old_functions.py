# from office.writer import Writer

# from commands import gen_array





# from crawler import Crawler
# from indexer import Indexer
# from scraper import Scraper

# import json
# import time

# import re

# from applicator import Applicator

## Build Applicator
# applicator = Applicator()

## Build Crawler
# crawler = Crawler()

## Build Scraper ##
# scraper = Scraper()

## Build Indexer
# indexer = Indexer()


## Set initial URL
# url = 'https://www.duckduckgo.com'
# url = 'https://www.yahoo.com'
# url = 'https://www.google.com'
# url = 'https://www.yandex.com'
# url = "https://www.geeksforgeeks.org/python-merging-two-dictionaries/"
# url = "https://www.w3schools.com/html/html_comments.asp"

 ###############
#### CRAWLER ####
 ###############

## Scrape HTML ##
# crawler.set_random_user_agent()
# user_agent = crawler.get_user_agent()
# print("user agent: " + user_agent)

# response = crawler.get_response(url)
# print("response: " + str(response))
# print("html: " + str(response.text))
# print("headers: " + str(response.headers))
# print("\n")


## Return html from response
# html = response.text


 ###############
#### SCRAPER ####
 ###############

## Remove text between two html elements
# html = scraper.remove_text(html, '<script', '</script>')
# html = scraper.remove_text(html, '<style', '</style>')

## Parse text from HTML ##
# html_text = scraper.parse_text(html)
# print(html_text)

## Parse links from HTML ##
# link_list = scraper.parse_links(html)
# print("links: " + str(link_list))
# print ("# of links: " + str(len(link_list)))






## Create list of html elements from response ##
# elmnt_list = scraper.parse_elements(html)


## Remove unwanted elements from list
# elmnt_list = scraper.clean_elements(elmnt_list, query="/")
# elmnt_list = scraper.clean_elements(elmnt_list, query="![endif]")
# elmnt_list = scraper.clean_elements(elmnt_list, query="<br")

# for elmnt in elmnt_list:
#     print(elmnt)






## Organize html elements from list into matrix ##
# elmnt_matrix = scraper.elmnt_matrix(elmnt_list)

## Print tags in matrix
# tag_list = []
# for k in elmnt_matrix:
#     tag_list.append(k)

# print("html tags: " + str(tag_list))
# print("\n")

## Print values associated with tags in element matrix
# tag = "div"
# tag = "meta"
# tag = "title"
# tag = "a"

# print(elmnt_matrix[tag])


## Create link matrix as tag[links] from element matrix ##
# link_matrix = scraper.link_matrix(elmnt_matrix)
# print(link_matrix)

## Print links associated with tags in link matrix ##
# print(link_matrix[tag])






 ###############
#### INDEXER ####
 ###############

## Parse response from link list and create array as: link[meta] ##
# db_content = {}
# int = 5
# for lnk in link_list:
#     crawler.set_random_sleep()
#     sleep_time = crawler.get_sleep()
#     print("sleep time: " + str(sleep_time))

#     crawler.set_random_user_agent()
#     user_agent = crawler.get_user_agent()
#     print("user agent: " + user_agent)

#     valid = False
#     if lnk not in db_content:

#         # response = crawler.parse_response(lnk)
#         response = crawler.get_response(lnk)
        
#         valid = crawler.check_validity(response)

#     if valid == True:
#         db_headers = dict(response.headers)
#         db_content[lnk] = db_headers

#     time.sleep(sleep_time)
    
#     int = int - 1
#     if int == 0:
#         break

# print("database: " + str(db_content))
# print("Database length: " + str(len(db_content)))


## Create new database from array ##
# db_name = 'db.json'
# indexer.create_db(db_content, db_name)


## Read array from database file ##
# db_name = 'db.json'
# db_content = indexer.read_db(db_name)


## List content from array ##
# print("before: ")
# text = indexer.list_content(db_content)
# print(text)

# data_type = 'Date'
# sort_reverse = True
# sorted_content = indexer.sort_data(db_content, data_type, sort_reverse=sort_reverse)

# print("after: ")
# text = indexer.list_content(sorted_content)
# print(text)


## Save database to file ##
# db_name = 'test.json'
# db_content = sorted_content
# indexer.save_db(db_content, db_name)


## Merge 2 databases ##
# db1 = "db1.json"
# db2 = "db2.json"

# db1_content = indexer.read_db(db1)
# db2_content = indexer.read_db(db2)

# text1 = indexer.list_content(db1_content)
# text2 = indexer.list_content(db2_content)

# print("db1:")
# print(text1)

# print("db2:")
# print(text2)

# merged_data = indexer.merge_data(db1_content, db2_content)

# text3 = indexer.list_content(merged_data)
# print("merged:")
# print(text3)




# ## Print content between one div element and the next ##
# # print(response.text)

# text_start = 0
# list_start = 0

# num = 0
# max = 500
# for e in div_list:

#     list_index = div_list.index(e, list_start)
#     # print("start index #: " + str(list_index))
    
#     sub1 = e
#     # print("string 1: " + sub1)

#     sub2 = div_list[list_index + 1]
#     # print("string 2: " + sub2)


#     text_index1 = response.text.find(sub1, text_start)
#     # print(text_index1)

#     text_index2 = response.text.find(sub2, text_index1 + len(sub1))
#     # print(text_index2)

#     result = response.text[text_index1 + len(sub1): text_index2]
#     print("in between: " + result)
    
#     list_start = list_index + 1
#     text_start = text_index1 + len(sub1)

#     num += 1
#     if num >= max:
#         break




## Check for hidden content and print links ##

# text_start = 0
# list_start = 0

# num = 0
# max = 1000

# tag = "visibility:hidden"
# # tag = "display:hidden"

# test_str = response.text

# for e in div_list:
#     if tag in e:
#         list_index = div_list.index(e, list_start)

#         sub1 = e
#         print("string 1: " + sub1)

#         sub2 = div_list[list_index + 1]
#         print("string 2: " + sub2)

#         text_index1 = response.text.find(sub1, text_start)
#         # print(text_index1)

#         text_index2 = response.text.find(sub2, text_index1 + len(sub1))
#         # print(text_index2) 

#         result = response.text[text_index1 + len(sub1): text_index2]
#         print("in between: " + result)
#         print("\n")

#         list_start = list_index + 1
#         text_start = text_index1 + len(sub1)

    # num += 1
    # if num >= max:
    #     break





#### WRITER ####
# doc_name = "testdoc"
# doc_text = "This is a test!"
# doc_text2 = "This is another test!!!"
# doc_text3 = "This is the final frontier!!!!!!"

# writer = Writer()
# writer.write_txt(doc_name, doc_text)
# writer.append_txt(doc_name, doc_text2)
# writer.save_txt(doc_name, doc_text3)














###### OLD FELO Content ######


# #Apply text to document based on tag
# if args.command == "applicator":
#     text = args.text
#     document = args.document
#     tag = args.tag
#     felow.apply_text(text, document, tag)

# #Build weight from .txt file
# elif args.command == "builder":
#     source = args.source
#     epochs = args.epochs
#     number = args.number
#     isnew = args.isnew

#     weights = args.weights
#     vocab = args.vocab
#     config = args.config
#     felow.build_weights(source, epochs, number, isnew, weights, vocab, config)

# elif args.command == "cleaner":
#     text = args.text
#     document = args.document
#     sentmin = args.sentmin
#     sentmax = args.sentmax
#     dictionary = args.dictionary
#     cycle = args.cycle
#     felow.clean_text(text, document, sentmin, sentmax, dictionary, cycle)

# #download documents from the internet
# elif args.command == "downloader":
#     query = args.query
#     engine = args.engine
#     headers = args.headers
#     waittime = args.waittime
#     startpage = args.startpage
#     endpage = args.endpage
#     filetypes = args.filetypes
#     scrape = args.scrape
#     felow.download_files(query, engine, headers, waittime, startpage, endpage, filetypes, scrape)

# #extract text from document(s) to .txt file
# elif args.command == "extractor":
#     path = args.path
#     filename = args.filename
#     felow.extract_text(path=path, filename=filename)

# elif args.command == "formatter":
#     text = args.text
#     document = args.document
#     formatting = args.formatting
#     felow.format_text(text, document, formatting)

# elif args.command == "generator":
#     weights = args.weights
#     vocab = args.vocab
#     config = args.config
#     num = args.num
#     lines = args.lines
#     temp = args.temp
#     document = args.document
#     felow.generate_text(weights, vocab, config, num, lines, temp, document)

# # elif args.command == "tst":
#     #Add test function here
#     # print("for testing...")

# else:
#     print("command not found")
#     print("use -h or --help for available commands")








# class Felow(object):


# #Applicator subparsers
# applicator = subparsers.add_parser(name="applicator")
# applicator.add_argument("-txt", "--text", action="store", dest="text", required=True)
# applicator.add_argument("-doc", "--document", action="store", dest="document", required=True)
# applicator.add_argument("-tag", "--tag", action="store", dest="tag", default="")

# #Builder subparsers
# builder = subparsers.add_parser(name="builder")
# builder.add_argument("-src", "--source", action="store", dest="source", required=True)
# builder.add_argument("-epo", "--epochs", action="store", dest="epochs", type=int, default=50)
# builder.add_argument("-num", "--number", action="store", type=int, dest="number", default=5)
# builder.add_argument("-new", "--isnew", action="store_true", dest="isnew")

# builder.add_argument("-wts", "--weights", action="store", dest="weights", default=None)
# builder.add_argument("-vcb", "--vocab", action="store", dest="vocab", default=None)
# builder.add_argument("-cfg", "--config", action="store", dest="config", default=None)

# #Cleaner subparsers
# cleaner = subparsers.add_parser(name="cleaner")
# cleaner.add_argument("-txt", "--text", action="store", dest="text", required=True)
# cleaner.add_argument("-doc", "--document", action="store", dest="document", default="clean.txt")
# cleaner.add_argument("-min", "--sentmin", action="store", type=int, dest="sentmin", default=6)
# cleaner.add_argument("-max", "--sentmax", action="store", type=int, dest="sentmax", default=24)
# cleaner.add_argument("-dic", "--dictionary", action="store", dest="dictionary", default="/home/lux/dev/felow/words")
# cleaner.add_argument("-cyl", "--cycle", action="store", dest="cycle", default="full")

# #Downloader subparsers
# downloader = subparsers.add_parser(name="downloader")
# downloader.add_argument("-qry", "--query", action="store", dest="query", required=True)
# downloader.add_argument("-eng", "--engine", action="store", dest="engine", default="g_scholar")
# downloader.add_argument("-hdr", "--headers", action="store", dest="headers", default={'user-agent': "Mozilla/5.0 (Linux x86_64; rv:83.0) Gecko/20100101 Firefox/83.0"})
# downloader.add_argument("-wtm", "--waittime", action="store", dest="waittime", type=int, default=5)
# downloader.add_argument("-spg", "--startpage", action="store", dest="startpage", type=int, default=1)
# downloader.add_argument("-epg", "--endpage", action="store", dest="endpage", type=int, default=3)
# downloader.add_argument("-fts", "--filetypes", action = "store", dest="filetypes", default=["pdf", "doc"])
# downloader.add_argument("-scp", "--scrape", action="store_true", dest="scrape")

# #Extractor subparsers
# extractor = subparsers.add_parser(name="extractor")
# extractor.add_argument("-p", "--path", action="store", dest="path", required=True)
# extractor.add_argument("-f", "--filename", action="store", dest="filename", default="extract.txt")
# extractor.add_argument("-min", "--sentmin", action="store", dest="sentmin", type=int, default=4)
# extractor.add_argument("-max", "--sentmax", action="store", dest="sentmax", type=int, default=12)
# extractor.add_argument("-stl", "--style", action="store", dest="style", default="")
# # extract.add_argument("-kwd", "--keywords", action="store_true", dest="keywords")
# # extract.add_argument("-kpl", "--keyphraselength", action="store", dest="keyphraselength", type=int, default=2)
# # extract.add_argument("-mkw", "--maxkeywords", action="store", dest="maxkeywords", type=int, default=50)

# #Formatter subparsers
# formatter = subparsers.add_parser(name="formatter")
# formatter.add_argument("-txt", "--text", action="store", dest="text", required=True)
# formatter.add_argument("-doc", "--document", action="store", dest="document", default="format.txt")
# formatter.add_argument("-fmt", "--formatting", action="store", dest="formatting", default="string")

# #Generator subparsers
# generator = subparsers.add_parser(name="generator")
# generator.add_argument("-wts", "--weights", action="store", dest="weights", default="weights.hdf5")
# generator.add_argument("-vcb", "--vocab", action="store", dest="vocab", default=None)
# generator.add_argument("-cfg", "--config", action="store", dest="config", default=None)
# generator.add_argument("-num", "--num", action="store", dest="num", type=int, required=True)
# generator.add_argument("-lns", "--lines", action="store", dest="lines", type=int, default=1)
# generator.add_argument("-tmp", "--temp", action="store", dest="temp", type=float, default=0.5)
# generator.add_argument("-doc", "--document", action="store", dest="document", default="gen.txt")

#Test subparsers
# test = subparsers.add_parser(name="tst")
##Add test subparsers here##





#     def get_string(self, text):
#         extractor = Extractor()
#         if os.path.isfile(text):
#             if extractor.extract_text(text):
#                 new_text = extractor.get_text()

#             else:
#                 print("unsupported file type")
#                 raise SystemExit

#         else:
#             new_text = text

#         return new_text


#     def apply_text(self, text, document, tag):
#         print("applicator selected")
#         applicator = Applicator()
#         new_text = self.get_string(text)
#         applicator.set_tag(tag)
#         if applicator.apply_text(text=new_text, document=document):
#             print("application successful")

#         else:
#             print("application failed")

#     def build_weights(self, source, epochs, number, isnew, weights, vocab, config):
#         print("builder selected")
#         builder = Builder()
#         builder.set_weights(weights, vocab, config)
#         if builder.build_weights(source=source, epochs=epochs, gen_epochs=number, is_new=isnew):
#             print("build successful")

#         else:
#             print("build failed")

#     def clean_text(self, text, document, sentmin, sentmax, dictionary, cycle):
#         print("applicator selected")
#         applicator = Applicator()
#         cleaner = Cleaner()
#         formatter = Formatter()
#         new_text = self.get_string(text)

#         cycle_list = ["noalpha", 
#                           "nodeclare", 
#                           "excaps", 
#                           "exletters", 
#                           "firstperson", 
#                           "secondperson", 
#                           "dupwords", 
#                           "duplicates", 
#                           "trimsentlist", 
#                           "checkspelling", 
#                           "help (or h)"]

#         def return_cycles():
#             s = ", "
#             s = s.join(cycle_list)
#             return s
        
#         cleaner.create_sentc_list(new_text)
#         if cycle == "full":
#             cleaner.remv_noalpha()
#             cleaner.remv_nodeclare()
#             cleaner.remv_excaps()
#             cleaner.remv_exletters()
#             cleaner.remv_firstperson()
#             cleaner.remv_secondperson()
#             cleaner.remv_dupwords()
#             cleaner.remv_duplicates()
#             cleaner.trim_sentlist(sentmin, sentmax)
#             cleaner.check_misspelled(dictionary)

#         elif cycle == "noalpha":
#             cleaner.remv_noalpha()

#         elif cycle == "nodeclare":
#             cleaner.remv_nodeclare()

#         elif cycle == "excaps":
#             cleaner.remv_excaps()

#         elif cycle == "exletters":
#             cleaner.remv_exletters()

#         elif cycle == "firstperson":
#             cleaner.remv_firstperson()

#         elif cycle == "secondperson":
#             cleaner.remv_secondperson()

#         elif cycle == "dupwords":
#             cleaner.remv_dupwords()

#         elif cycle == "duplicates":
#             cleaner.remv_duplicates()

#         elif cycle == "trimsentlist":
#             cleaner.trim_sentlist(sentmin, sentmax)

#         elif cycle == "checkspelling":
#             cleaner.check_misspelled(dictionary)

#         else:
#             print("cycle not found")
#             print("available cycles:")
#             print(return_cycles())
#             raise SystemExit

#         sentc_list = cleaner.get_sentc_list()
#         formatter.set_sentlist(sentc_list)
#         formatter.frmt_textlist()
#         clean_text = formatter.get_text()
#         applicator.apply_text(text=clean_text, document=document)

#     def download_files(self, query, engine, headers, waittime, startpage, endpage, filetypes, scrape):
#         # applicator = Applicator()
#         downloader = Downloader()

#         #Set search engine
#         downloader.set_searchengine(engine)
#         downloader.set_waittime(waittime)
        
#         page = startpage
#         link_list = []
#         scraped_html = ""

#         #Scrape HTML from pages
#         while page <= endpage: 
            
#             #build url from search engine and query
#             url = downloader.build_url(query, page)

#             #retreive html
#             html = downloader.scrape_html(url, headers)
#             scraped_html = scraped_html + html.text

#             #increment page by 10 for google/scholar
#             page += 1
#             # time.sleep(wait_time)

#         #Get links from collected html
#         link_list = downloader.scrape_links(scraped_html)

#         #Filter links by filetype
#         filter_list = downloader.filter_links(link_list, filetypes)

#         #Download files from filtered links
#         downloader.dl_links(filter_list)

#         # if scrape == True:
#         #     print("collecting scraped html...")
#         #     for lnk in link_list:
#         #         if lnk not in filter_list:
#         #             try:
#         #                 html = downloader.scrape_html(lnk, headers)
#         #                 scraped_html = scraped_html + html.text

#         #                 html_text = scraped_html
#         #                 #Use Beautiful Soup to scrape raw html for text
#         #                 # html_text = downloader.scrape_text(scraped_html)

#         #                 applicator.set_text(html_text)
#         #                 applicator.apply_text("scraped.txt")

#         #                 # time.sleep(wait_time)

#         #             except:
#         #                 print("scrape failed")

#     def extract_text(self, path, filename):
#         applicator = Applicator()
#         extractor = Extractor()

#         text = ""
#         # ref_list = []

#         #If path is directory
#         if os.path.isdir(path):
#             for doc in os.listdir(path):
#                 if extractor.extract_text(os.path.join(path, doc)):
#                     text = text + extractor.get_text()

#                 else:
#                     print("no text extracted")

#                 # temp_refs = extractor.extract_references(os.path.join(path, doc))
#                 # ref_list.append(temp_refs)
 
#         #If path is file
#         elif os.path.isfile(path):
#             doc = os.path.split(path)[1]
#             if extractor.extract_text(doc):
#                 text = extractor.get_text()

#             else:
#                 print("no text extracted")

#             # temp_refs = extractor.extract_references(os.path.join(path, doc))
#             # ref_list.append(temp_refs)

#         else:
#             print("invalid path")
#             raise SystemExit

#         applicator.apply_text(text=text, document=filename)

#         print("extraction complete")

#         # if len(style) > 0:
#         #     #Add extracted references to text file
#         #     formatted_refs = formatter.frmt_references(ref_list, style)
            
#         #     for refrnc in formatted_refs:
#         #         applicator.set_text(refrnc)
#         #         applicator.apply_text("references.txt")

#         # #Create keyword list
#         # if keywords == True:
#         #     print("keyword extraction selected...")
#         #     print("creating keywords.txt...")
#         #     # phrase_len = 2
#         #     # max_keywords = 50
#         #     extractor.set_text(text)
#         #     keyword_list = extractor.extract_keywords(phrase_len, max_keywords)
#         #     kwd_text = ""
#         #     for kwd in keyword_list:
#         #         kwd_text = kwd_text + kwd
#         #         kwd_text = kwd_text + "\n"

#         #     applicator.set_text(kwd_text)    
#         #     applicator.apply_text("keywords.txt")

#     def format_text(self, text, document, formatting):
#         par_len = 150

#         applicator = Applicator()
#         cleaner = Cleaner()
#         formatter = Formatter()
#         new_text = self.get_string(text)

#         cleaner.create_sentc_list(new_text)
#         sentc_list = cleaner.get_sentc_list()
#         formatter.set_sentlist(sentc_list)

#         if formatting == "list":
#             formatter.frmt_textlist()

#         elif formatting == "block":
#             formatter.frmt_textblock(par_len=par_len)

#         elif formatting == "string":
#             formatter.frmt_textstring()

#         else:
#             print("format not supported")
#             raise SystemExit
        
#         format_text = formatter.get_text()
#         applicator.apply_text(format_text, document=document)

#     def generate_text(self, weights, vocab, config, num, lines, temp, document):
#         applicator = Applicator()
#         formatter = Formatter()
#         generator = Generator()
        
#         generator.set_weights(weights, vocab, config)
#         generator.gen_text(num, lines, temp)
#         gen_list = generator.get_text_list()
        
#         formatter.set_sentlist(gen_list)
#         formatter.frmt_textlist()
#         format_text = formatter.get_text()
#         applicator.apply_text(format_text, document)


# #Construct felow object
# felow = Felow()