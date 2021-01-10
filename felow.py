#########           
##FELOW##
#########

from applicator import Applicator
from builder import Builder
from cleaner import Cleaner
from downloader import Downloader
from extractor import Extractor
from formatter import Formatter
from generator import Generator

import argparse
import textwrap
import os
import time

class Felow(object):
    def download_files(self, query, engine, headers, startpage, endpage, filetypes):
        print("downloading files...", flush=True)

        downloader = Downloader()

        #Set search engine
        downloader.set_searchengine(engine)

        #Retreive HTML
        link_list = []
        scraped_html = ""
        wait_time = 5
        page = startpage

        #Scrape HTML from pages
        while page <= endpage: 
            
            #build url from search engine and query
            url = downloader.build_url(query, page)

            #retreive html
            html = downloader.scrape_html(url, headers)
            scraped_html = scraped_html + html.text

            #increment page by 10 for google/scholar
            page += 10
            time.sleep(wait_time)

        #Get links from collected html
        link_list = downloader.scrape_links(scraped_html)

        #Parse by filetypes
        if len(filetypes) >= 1:
            temp_list = []
            for fltype in filetypes:
                filter_list = downloader.filter_links(link_list, fltype)
                temp_list = temp_list + filter_list

            link_list = temp_list

        #Download files from collected links
        downloader.dl_links(link_list)

    def extract_text(self, path, filename):
        print("extracting text...")

        applicator = Applicator()
        cleaner = Cleaner()
        formatter = Formatter()
        extractor = Extractor()

        text = ""
        sent_min = 12
        sent_max = 72

        #If path is directory
        if os.path.isdir(path):
            for doc in os.listdir(path):
                extractor.extract_text(os.path.join(path, doc))
                extractor.strip_pars()
                extractor.strip_quotes()
                extractor.strip_newlines()
                text = text + extractor.get_text()

        #If path is file
        elif os.path.isfile(path):
            doc = os.path.split(path)[1]
            extractor.extract_text(path)
            extractor.strip_pars()
            extractor.strip_quotes()
            extractor.strip_newlines()
            text = extractor.get_text()

        else:
            print("invalid path")

            raise SystemExit

        #Clean collected text
        cleaner.set_text(text)
        cleaner.build_sentlist()
        
        cleaner.remv_dblspaces()
        cleaner.remv_nodeclare()
        cleaner.remv_nums()
        cleaner.remv_wtspc()
        cleaner.remv_noleadcap()
        cleaner.remv_excap()
        cleaner.trim_sentlist(sent_min, sent_max)
        cleaner.check_spelling()
        sent_list = cleaner.get_sentlist()

        #Format sentences as text list
        formatter.set_sentlist(sent_list)
        formatter.frmt_textlist()
        text = formatter.get_text()

        #apply text to .txt doc
        applicator.set_text(text)
        applicator.apply_text(filename)

    def build_weight(self, epochs, source, weightname, numepochs):
        print("building weight...")

        builder = Builder()
        builder.build_weight(source, epochs, numepochs, weightname)

    def generate_document(self, numwords, weightname, filename, title, tag, lines, temp):
        print("generating document...")

        applicator = Applicator()
        cleaner = Cleaner()
        formatter = Formatter()
        generator = Generator()
        
        sent_list = []
        len_check = 0 
        word_min = 14
        word_max = 28

        #Set selected weight
        generator.set_weight(weightname)

        #Generate text in loop
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

            #Collect generated text and clean
            cleaner.set_sentlist(gen_list)

            #Clean text in sentence list
            cleaner.remv_nodeclare()
            cleaner.remv_nums()
            cleaner.remv_wtspc()
            cleaner.remv_noleadcap()
            cleaner.remv_excap()
            cleaner.remv_dupwrds()
            cleaner.remv_duplicates()
            cleaner.remv_firstperson()
            cleaner.remv_secondperson()
            cleaner.check_spelling()
            cleaner.trim_sentlist(word_min, word_max)

            #Add cleaned text to collected text and check for duplicate sentences
            cleaned_list = cleaner.get_sentlist()
            temp_list = sent_list + cleaned_list
            cleaner.set_sentlist(temp_list)
            cleaner.remv_duplicates()
            sent_list = cleaner.get_sentlist()

            #Get length of collected text
            i = 0
            for sentc in sent_list:
                i += len(sentc.split())

            len_check = i

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

        #Apply selected title to document
        if len (title) >= 1:
            title_tag = "Title"
            applicator.set_text(title)
            applicator.set_tag(title_tag)
            applicator.apply_text(filename)
        
        #Apply formatted text to document
        applicator.set_text(text)
        applicator.set_tag(tag)
        applicator.apply_text(filename)

#Construct felow object
felow = Felow()

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

#download subparsers
download = subparsers.add_parser(name="dnl")
download.add_argument("-qry", "--query", action="store", dest="query", required=True)
download.add_argument("-eng", "--engine", action="store", dest="engine", default="g_scholar")
download.add_argument("-hdr", "--headers", action="store", dest="headers", default={'user-agent': "Mozilla/5.0 (Linux x86_64; rv:83.0) Gecko/20100101 Firefox/83.0"})
download.add_argument("-spg", "--startpage", action="store", dest="startpage", type=int, default=0)
download.add_argument("-epg", "--endpage", action="store", dest="endpage", type=int, default=40)
download.add_argument("-fts", "--filetypes", action = "store", dest="filetypes", default=[".pdf", ".doc"])

#extract subparsers
extract = subparsers.add_parser(name="ext")
extract.add_argument("-p", "--path", action="store", dest="path", required=True)
extract.add_argument("-f", "--filename", action="store", dest="filename", default="extract.txt")

#build subparsers
build = subparsers.add_parser(name="bld")
build.add_argument("-epo", "--epochs", action="store", type=int, dest="epochs", required=True)
build.add_argument("-src", "--source", action="store", dest="source", default="extract.txt")
build.add_argument("-wgt", "--weightname", action="store", dest="weightname", default="weight.hdf5")
build.add_argument("-num", "--numepochs", action="store", type=int, dest="numepochs", default=False)

#generate subparsers
generate = subparsers.add_parser(name="gen")
generate.add_argument("-num", "--numwords", action="store", dest="numwords", type=int, required=True)
generate.add_argument("-wgt", "--weightname", action="store", dest="weightname", required=True)
generate.add_argument("-f", "--filename", action="store", dest="filename", required=True)
generate.add_argument("-ttl", "--title", action="store", dest="title", default="")
generate.add_argument("-tag", "--tag", action="store", dest="tag", default="<content>")
generate.add_argument("-lns", "--lines", action="store", dest="lines", type=int, default=1)
generate.add_argument("-tmp", "--temp", action="store", dest="temp", type=float, default= 0.5)

#test subparsers
test = subparsers.add_parser(name="tst")

#Get arguments
args = parser.parse_args()

#download documents from the internet
if args.command == "dnl":
    query = args.query
    engine = args.engine
    headers = args.headers
    startpage = args.startpage
    endpage = args.endpage
    filetypes = args.filetypes
    felow.download_files(query, engine, headers, startpage, endpage, filetypes)

#extract text from document(s) to .txt file
elif args.command == "ext":
    path = args.path
    filename = args.filename
    felow.extract_text(path, filename)

#Build weight from .txt file
elif args.command == "bld":
    print("building...")
    epochs = args.epochs
    source = args.source
    weightname = args.weightname
    numepochs = args.numepochs
    felow.build_weight(epochs, source, weightname, numepochs)

#Generate document from weight
elif args.command == "gen":
    numwords = args.numwords
    weightname = args.weightname
    filename = args.filename
    title = args.title
    tag = args.tag
    lines = args.lines
    temp = args.temp
    felow.generate_document(numwords, weightname, filename, title, tag, lines, temp)

# elif args.command == "tst":
#     #Add test function here
#     #print("for testing...")

else:
    print("command not found")
    print("use -h or --help for available commands")