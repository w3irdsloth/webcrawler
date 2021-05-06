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

class Felow(object):
    def download_files(self, query, engine, headers, waittime, startpage, endpage, filetypes, scrape):
        print("downloader selected...")
        applicator = Applicator()
        downloader = Downloader()

        #Set search engine
        downloader.set_searchengine(engine)
        downloader.set_waittime(waittime)
        
        
        page = startpage
        link_list = []
        scraped_html = ""

        #Scrape HTML from pages
        while page <= endpage: 
            
            #build url from search engine and query
            url = downloader.build_url(query, page)

            #retreive html
            html = downloader.scrape_html(url, headers)
            scraped_html = scraped_html + html.text

            #increment page by 10 for google/scholar
            page += 1
            # time.sleep(wait_time)

        #Get links from collected html
        link_list = downloader.scrape_links(scraped_html)
        print(link_list)

        #Filter links by filetype
        filter_list = downloader.filter_links(link_list, filetypes)

        #Download files from filtered links
        downloader.dl_links(filter_list)

        if scrape == True:
            print("collecting scraped html...")
            for lnk in link_list:
                if lnk not in filter_list:
                    try:
                        html = downloader.scrape_html(lnk, headers)
                        scraped_html = scraped_html + html.text

                        html_text = scraped_html
                        #Use Beautiful Soup to scrape raw html for text
                        # html_text = downloader.scrape_text(scraped_html)

                        applicator.set_text(html_text)
                        applicator.apply_text("scraped.txt")

                        # time.sleep(wait_time)

                    except:
                        print("scrape failed")

    def extract_text(self, path, filename, sentmin, sentmax, style, keywords, keyphraselen, maxkeywords):
        print("extractor selected...")
        applicator = Applicator()
        cleaner = Cleaner()
        formatter = Formatter()
        extractor = Extractor()

        dictionary = "/home/lux/dev/felow/words"
        sent_min = sentmin
        sent_max = sentmax
        phrase_len = keyphraselen
        max_keywords = maxkeywords

        text = ""
        ref_list = []

        #If path is directory
        if os.path.isdir(path):
            for doc in os.listdir(path):
                extractor.extract_text(os.path.join(path, doc))
                text = text + extractor.get_text()

                temp_refs = extractor.extract_references(os.path.join(path, doc))
                ref_list.append(temp_refs)
 
        #If path is file
        elif os.path.isfile(path):
            doc = os.path.split(path)[1]
            extractor.extract_text(doc)
            text = extractor.get_text()

            temp_refs = extractor.extract_references(os.path.join(path, doc))
            ref_list.append(temp_refs)

        else:
            print("invalid path")
            raise SystemExit

        #Clean collected text
        cleaner.set_text(text)
        cleaner.sort_sentcs() 
        cleaner.remv_newlines()
        cleaner.remv_duplicates()
        
        #Remove parenthetical text before filtering characters
        cleaner.remv_pars()
        cleaner.remv_noalpha()
        
        #Remove unwanted sentences
        cleaner.remv_nodeclare()
        cleaner.remv_firstperson()
        cleaner.remv_secondperson()

        #Specific items to remove
        cleaner.remv_excaps()
        cleaner.remv_exletters()
        cleaner.remv_badpgs()

        #Fix punctuation spacing resulting from removed characters
        cleaner.remv_punspace()
        cleaner.remv_badcoms()

        #Trim the length and check spelling
        cleaner.trim_sentlist(sent_min, sent_max)

        # cleaner.check_sentlen(40)

        cleaner.check_misspelled(dictionary)

        sent_list = cleaner.get_sentlist()

        #Format sentences as text list
        formatter.set_sentlist(sent_list)
        formatter.frmt_textlist()
        text = formatter.get_text()

        #apply text to .txt doc
        applicator.set_text(text)
        applicator.apply_text(filename)

        if len(style) > 0:
            #Add extracted references to text file
            formatted_refs = formatter.frmt_references(ref_list, style)
            
            for refrnc in formatted_refs:
                applicator.set_text(refrnc)
                applicator.apply_text("references.txt")

        #Create keyword list
        if keywords == True:
            print("keyword extraction selected...")
            print("creating keywords.txt...")
            # phrase_len = 2
            # max_keywords = 50
            extractor.set_text(text)
            keyword_list = extractor.extract_keywords(phrase_len, max_keywords)
            kwd_text = ""
            for kwd in keyword_list:
                kwd_text = kwd_text + kwd
                kwd_text = kwd_text + "\n"

            applicator.set_text(kwd_text)    
            applicator.apply_text("keywords.txt")

    def build_weight(self, epochs, source, weightname, numepochs):
        print("builder selected...")
        builder = Builder()
        builder.build_weight(source, epochs, numepochs, weightname)

    def generate_document(self, filename, numwords, sentmin, sentmax, title, weightname, lines, temp, clean):
        print("generator selected...")
        applicator = Applicator()
        cleaner = Cleaner()
        extractor = Extractor()
        formatter = Formatter()
        generator = Generator()
        
        dictionary = "/home/lux/dev/felow/words"
        keywords = False
        par_len = 175

        sent_list = []
        len_check = 0

        #Set selected weight
        generator.set_weight(weightname)

        #Check for keyword text and build list
        if os.path.exists("keywords.txt"):
            print("keywords.txt found...")
            extractor.extract_text("keywords.txt")
            keyword_text = extractor.get_text()
            temp_text = ""
            keyword_list = []
            keywords = True
            for char in keyword_text:
                if char == "\n":
                    keyword_list.append(temp_text)
                    temp_text = ""
                
                else:
                    temp_text = temp_text + char

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

            print("generated text: " + str(gen_list))

            #Clean generated text
            if clean == True:
                cleaner.set_sentlist(gen_list)
                
                cleaner.remv_noalpha()
                cleaner.remv_nodeclare()
                cleaner.remv_excaps()
                cleaner.remv_exletters()
                cleaner.remv_firstperson()
                cleaner.remv_secondperson()
                cleaner.remv_dupwords()

                cleaner.trim_sentlist(sentmin, sentmax)
                cleaner.check_misspelled(dictionary)

                #Check for keywords
                if keywords == True:
                    cleaner.check_keywords(keyword_list)

                gen_list = cleaner.get_sentlist()

                print("cleaned text: " + str(gen_list))

            #Add generated text to collected text and check for duplicate sentences
            temp_list = sent_list + gen_list
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
        formatter.set_sentlist(sent_list)
        formatter.frmt_textblock(par_len)
        text = formatter.get_text()

        #Apply selected title to document
        title_tag = "<title>"
        applicator.set_text(title)
        applicator.set_tag(title_tag)
        applicator.apply_text(filename)
        
        #Apply formatted text to document
        content_tag = "<content>"
        applicator.set_text(text)
        applicator.set_tag(content_tag)
        applicator.apply_text(filename)

        #Apply references to document
        reference_tag = "<references>"
        extractor.extract_text("references.txt")
        references = extractor.get_text()
        applicator.set_tag(reference_tag)
        applicator.set_text(references)
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

#dnl subparsers
download = subparsers.add_parser(name="dnl")
download.add_argument("-qry", "--query", action="store", dest="query", required=True)
download.add_argument("-eng", "--engine", action="store", dest="engine", default="g_scholar")
download.add_argument("-hdr", "--headers", action="store", dest="headers", default={'user-agent': "Mozilla/5.0 (Linux x86_64; rv:83.0) Gecko/20100101 Firefox/83.0"})
download.add_argument("-wtm", "--waittime", action="store", dest="waittime", type=int, default=5)
download.add_argument("-spg", "--startpage", action="store", dest="startpage", type=int, default=1)
download.add_argument("-epg", "--endpage", action="store", dest="endpage", type=int, default=3)
download.add_argument("-fts", "--filetypes", action = "store", dest="filetypes", default=["pdf", "doc"])
download.add_argument("-scp", "--scrape", action="store_true", dest="scrape")

#ext subparsers
extract = subparsers.add_parser(name="ext")
extract.add_argument("-p", "--path", action="store", dest="path", required=True)
extract.add_argument("-f", "--filename", action="store", dest="filename", default="extract.txt")
extract.add_argument("-min", "--sentmin", action="store", dest="sentmin", type=int, default=4)
extract.add_argument("-max", "--sentmax", action="store", dest="sentmax", type=int, default=12)
extract.add_argument("-stl", "--style", action="store", dest="style", default="")
extract.add_argument("-kwd", "--keywords", action="store_true", dest="keywords")
extract.add_argument("-kpl", "--keyphraselength", action="store", dest="keyphraselength", type=int, default=2)
extract.add_argument("-mkw", "--maxkeywords", action="store", dest="maxkeywords", type=int, default=50)

#bld subparsers
build = subparsers.add_parser(name="bld")
build.add_argument("-epo", "--epochs", action="store", dest="epochs", type=int, default=50)
build.add_argument("-src", "--source", action="store", dest="source", default="extract.txt")
build.add_argument("-wgt", "--weightname", action="store", dest="weightname", default="weight.hdf5")
build.add_argument("-num", "--numepochs", action="store", type=int, dest="numepochs", default=False)

#gen subparsers
generate = subparsers.add_parser(name="gen")
generate.add_argument("-f", "--filename", action="store", dest="filename", required=True)
generate.add_argument("-num", "--numwords", action="store", dest="numwords", type=int, required=True)
generate.add_argument("-min", "--sentmin", action="store", dest="sentmin", type=int, default=4)
generate.add_argument("-max", "--sentmax", action="store", dest="sentmax", type=int, default=12)
generate.add_argument("-ttl", "--title", action="store", dest="title", default="Title")
generate.add_argument("-wgt", "--weightname", action="store", dest="weightname", default="weight.hdf5")
generate.add_argument("-lns", "--lines", action="store", dest="lines", type=int, default=1)
generate.add_argument("-tmp", "--temp", action="store", dest="temp", type=float, default=0.5)
generate.add_argument("-ncl", "--noclean", action="store_false", dest="noclean")

#tst subparsers
test = subparsers.add_parser(name="tst")

#set arguments
args = parser.parse_args()

#download documents from the internet
if args.command == "dnl":
    query = args.query
    engine = args.engine
    headers = args.headers
    waittime = args.waittime
    startpage = args.startpage
    endpage = args.endpage
    filetypes = args.filetypes
    scrape = args.scrape
    felow.download_files(query, engine, headers, waittime, startpage, endpage, filetypes, scrape)

#extract text from document(s) to .txt file
elif args.command == "ext":
    path = args.path
    filename = args.filename
    sentmin = args.sentmin
    sentmax = args.sentmax
    style = args.style
    keywords = args.keywords
    keyphraselen = args.keyphraselength
    maxkeywords = args.maxkeywords
    felow.extract_text(path, filename, sentmin, sentmax, style, keywords, keyphraselen, maxkeywords)

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
    filename = args.filename
    numwords = args.numwords
    sentmin = args.sentmin
    sentmax = args.sentmax
    title = args.title
    weightname = args.weightname
    lines = args.lines
    temp = args.temp
    noclean = args.noclean
    felow.generate_document(filename, numwords, sentmin, sentmax, title, weightname, lines, temp, noclean)

elif args.command == "tst":
    #Add test function here
    # print("for testing...")
    applicator = Applicator()
    applicator.set_tag("Hi")
    applicator.apply_text("Bye", "newdoc.docx")

else:
    print("command not found")
    print("use -h or --help for available commands")
