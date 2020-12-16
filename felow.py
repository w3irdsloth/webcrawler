#########           
##FELOW##
#########

import argparse
import textwrap
import os
import time

from applicator import Applicator
from builder import Builder
from cleaner import Cleaner
from downloader import Downloader
from extractor import Extractor
from formatter import Formatter
from generator import Generator

#Construct parsers
parser = argparse.ArgumentParser( prog='FELOW',
      formatter_class=argparse.RawDescriptionHelpFormatter,
      description=textwrap.dedent('''\

                 ##   ###########   ##                   ##########     
              ###########################              ### Hello! ###
            ####  ###################  ####         #### I'm FELOW. #######
           #################################       ### Your Fellow Editor ##
          #############  FELOW  #############     ### And Logical Office ##       
           #############abcdefg#############   ############ Writer. #######
            ############ ###### ########### ####         ########### 
              ###########      ###########
                      ############        
                       ##########
--------------------------------------------------------------
Apply | Build | Clean | Download | Extract | Format | Generate
-------------------------------------------------------------- 
         '''), epilog='''
--------------------------------------------------------------
                                ''')

subparsers = parser.add_subparsers(title="commands", dest="command")

#set download subparsers
download = subparsers.add_parser(name="dnl")
download.add_argument("-qry", "--query", action="store", dest="query", required=True)
download.add_argument("-hdr", "--headers", action="store", dest="headers", default={'user-agent': "Mozilla/5.0 (Linux x86_64; rv:83.0) Gecko/20100101 Firefox/83.0"})
download.add_argument("-eng", "--engine", action="store", dest="engine", default="g_scholar")
download.add_argument("-spg", "--startpage", action="store", dest="startpage", default=0)
download.add_argument("-epg", "--endpage", action="store", dest="endpage", default=40)
download.add_argument("-prs", "--parseword", action="store", dest="parseword", default=".pdf")

#extract subparsers
extract = subparsers.add_parser(name="ext")
extract.add_argument("-p", "--path", action="store", dest="path", required=True)
extract.add_argument("-f", "--filename", action="store", dest="filename", default="extract.txt")
extract.add_argument("-kwd", "--keyword", action="store", dest="keyword", type=bool, default=False)

#set build subparsers
build = subparsers.add_parser(name="bld")
build.add_argument("-f", "--filename", action="store", dest="filename", required=True)
build.add_argument("-epo", "--epochs", action="store", type=int, dest="epochs", required=True) 
build.add_argument("-num", "--numepochs", action="store", type=int, dest="numepochs", default=False)
build.add_argument("-wgt", "--weightname", action="store", dest="weightname", default="weight.hdf5")

#set generate subparsers
generate = subparsers.add_parser(name="gen")
generate.add_argument("-num", "--numwords", action="store", dest="numwords", type=int, required=True)
generate.add_argument("-wgt", "--weight", action="store", dest="weight", required=True)
generate.add_argument("-f", "--filename", action="store", dest="filename", required=True)
generate.add_argument("-lns", "--lines", action="store", dest="lines", type=int, default=1)
generate.add_argument("-tmp", "--temp", action="store", dest="temp", type=float, default= 0.5)
generate.add_argument("-tag", "--tag", action="store", dest="tag", default="<content>")
generate.add_argument("-ttl", "--title", action="store", dest="title", default="")

test = subparsers.add_parser(name="tst")

#Get arguments
args = parser.parse_args()

#download documents from the internet
if args.command == "dnl":
    query = args.query
    headers = args.headers
    engine = args.engine
    startpage = args.startpage
    endpage = args.endpage
    parseword = args.parseword
    
    # finder = Finder()
    downloader = Downloader()

    #Set search engine
    downloader.set_searchengine(engine)

    #Retreive HTML
    link_list = []
    scraped_html = ""
    wait_time = 5
    page = startpage
    print("checking page " + str(int(page / 10)) + "...")
    while page <= endpage: 
        #Build url from search engine and query
        downloader.build_url(query, page)
        print("scraping " + downloader.get_url() + "...")

        #retreive html
        html = downloader.scrape_html(headers)

        scraped_html = scraped_html + html

        # #parse links from html
        # links = downloader.find_links(html)

        # for lnk in links:
        #     link_list.append(lnk)

        #Increment page by 10 for google/scholar
        page += 10
        time.sleep(wait_time)
        print("checking page " + str(int(page/10)) + "...")

    #Get links from collected html
    link_list = downloader.find_links(scraped_html)

    #Parse by filetype
    my_links = downloader.filter_links(link_list, parseword)

    #Download links
    downloader.dl_links(my_links)

#extract text from document(s) to .txt file
elif args.command == "ext":
    path = args.path
    filename = args.filename
    keyword = args.keyword

    applicator = Applicator()
    cleaner = Cleaner()
    formatter = Formatter()
    extractor = Extractor()

    sent_list = []
    text = ""
    sent_min = 5
    sent_max = 25
    #If path is folder
    if os.path.isdir(path):
        for doc in os.listdir(path):
            print("extracting from " + doc + "...")
            extractor.split_ext(doc)
            extractor.extract_text(os.path.join(path, doc))
            text = text + extractor.get_text()

    #If path is file
    elif os.path.isfile(path):
        print("extracting from " + doc + "...")
        extractor.split_ext(doc)
        extractor.extract_text(doc)
        text = extractor.get_text()

    else:
        print("not a path")
        raise SystemExit

    #Clean collected text
    cleaner.set_text(text)
    cleaner.build_sentlist()
    cleaner.remv_newlines()
    cleaner.remv_nodeclare()
    cleaner.remv_nums()
    cleaner.remv_wtspc()
    cleaner.remv_noleadcap()
    cleaner.trim_sentlist(sent_min, sent_max)
    cleaner.remv_excap()
    cleaner.fix_language() 
    cleaner.remv_badlanguage()
    sent_list = cleaner.get_sentlist()

    #Format sentences as text list
    formatter.set_sentlist(sent_list)
    formatter.frmt_textlist()
    text = formatter.get_text()

    #apply text to .txt doc
    applicator.set_text(text)
    applicator.split_ext(filename)
    applicator.apply_text(filename)

    #Generate keyword list if necessary
    if keyword == True:
        from rake_nltk import Rake
        r = Rake(max_length=1)
        r.extract_keywords_from_text(text)
        keyword_list = r.get_ranked_phrases()

        #Apply keyword list to text
        formatter.set_sentlist(keyword_list)
        formatter.frmt_textlist()
        keyword_text = formatter.get_text()
        applicator.set_text(keyword_text)
        applicator.set_ext(".txt")
        applicator.apply_text("keywords.txt")

#Build weight from .txt file
elif args.command == "bld":
    
    filename = args.filename
    epochs = args.epochs
    numepochs = args.numepochs
    weightname = args.weightname
    builder = Builder()
    print("building weight...")
    builder.build_weight(filename, epochs, numepochs, weightname)

#Generate document from weight
elif args.command == "gen":
    numwords = args.numwords
    lines = args.lines
    temp = args.temp
    weight = args.weight
    tag = args.tag
    filename = args.filename
    title = args.title

    applicator = Applicator()
    cleaner = Cleaner()
    formatter = Formatter()
    generator = Generator()
    
    sent_list = []
    len_check = 0 
    word_min = 5
    word_max = 35
    
    #Check for keyword text file and build list
    if os.path.exists("keywords.txt"):
        print("keyword .txt found")
        print("building keyword list...")
        kywrd_text = open("keywords.txt", "r")
        kywrd_list =[]
        for line in kywrd_text:
            line = line.rstrip("\n")
            kywrd_list.append(line)

    #Generate weight in loop
    generator.set_weight(weight)
    print("generating document...")
    while True:
        #Check number of words to generate
        gen_num = numwords - len_check
        
        #Generate text based on remaining word count
        generator.gen_text(gen_num, lines, temp)
        gen_list = generator.get_text_list()
        
        #Get length of generated text plus stored text
        gen_len = generator.get_textlength()
        old_len = len_check + gen_len
        print(str(old_len) + " words collected...")

        #Collect generated text and build sentence list
        cleaner.set_sentlist(gen_list)

        #Clean text in sentence list
        cleaner.remv_nodeclare()
        cleaner.remv_nums()
        cleaner.remv_wtspc()
        cleaner.remv_noleadcap()
        cleaner.trim_sentlist(word_min, word_max)
        cleaner.fix_language()
        cleaner.remv_excap()
        cleaner.remv_badlanguage()
        
        #Check for keywords
        try:
            cleaner.check_kywrds(kywrd_list)

        except:
            pass

        #Get cleaned text from cleaner
        cleaned_list = cleaner.get_sentlist()

        #Collect cleaned sentences and get length
        i = 0
        for sentc in cleaned_list:
            sent_list.append(sentc)
            i += len(sentc.split())

        len_check += i

        #Print length of discarded text
        disc_len = old_len - len_check
        print("old length: " + str(old_len))
        print("new length: " + str(len_check))
        print(str(disc_len) + " words discarded...")
            
        #Break loop when word count reached
        if len_check >= numwords:
            break
    
    #Format generated sentences as paragraph
    par_len = 175
    formatter.set_sentlist(sent_list)
    formatter.frmt_textblock(par_len)
    text = formatter.get_text()

    #Apply title to document
    if len (title) >= 1:
        title_tag = "Title"
        applicator.set_text(title)
        applicator.set_tag(title_tag)
        applicator.split_ext(filename)
        applicator.apply_text(filename)
    
    #Apply formatted text to document
    applicator.set_text(text)
    applicator.set_tag(tag)
    applicator.split_ext(filename)
    applicator.apply_text(filename)

elif args.command == "tst":
    cleaner = Cleaner()
    downloader = Downloader()
    downloader.set_url("https://www.google.com/books/edition/An_Enquiry_Concerning_the_Principles_of/xGFE53T5yd8C?hl=en&gbpv=1")
    html = downloader.scrape_html({'user-agent': "Mozilla/5.0 (Linux x86_64; rv:83.0) Gecko/20100101 Firefox/83.0"})
    print(html)

    cleaner.set_text(html)
    cleaner.build_sentlist()
    cleaner.remv_newlines()
    cleaner.remv_nodeclare()
    cleaner.remv_nums()
    cleaner.remv_wtspc()
    cleaner.remv_noleadcap()
    cleaner.trim_sentlist(12, 32)
    cleaner.remv_excap()
    cleaner.fix_language() 
    cleaner.remv_badlanguage()

    print(cleaner.get_sentlist())

else:
    print("command not found")
    print("use -h or --help for available commands")