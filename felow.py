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
        print("downloader selected...")
        # applicator = Applicator()
        downloader = Downloader()

        #Set search engine
        downloader.set_searchengine(engine)

        #Retreive HTML
        link_list = []
        scraped_html = ""
        wait_time = 3
        page = startpage

        # scrape = True

        #Scrape HTML from pages
        while page <= endpage: 
            
            #build url from search engine and query
            url = downloader.build_url(query, page)

            #retreive html
            html = downloader.scrape_html(url, headers)
            scraped_html = scraped_html + html.text

            #increment page by 10 for google/scholar
            page += 1
            time.sleep(wait_time)

        #Get links from collected html
        link_list = downloader.scrape_links(scraped_html)

        #Filter links by filetype
        filter_list = downloader.filter_links(link_list, filetypes)

        #Download files from filtered links
        downloader.dl_links(filter_list)

        # if scrape == True:
        #     print("collecting scraped html...")
        #     for lnk in link_list:
        #         if lnk not in filter_list:
        #             try:
        #                 html = downloader.scrape_html(lnk, headers)
        #                 scraped_html = scraped_html + html.text

        #                 #Use Beautiful Soup to scrape raw html for text
        #                 html_text = downloader.scrape_text(scraped_html)

        #                 applicator.set_text(html_text)
        #                 applicator.apply_text("scraped.txt")

        #                 time.sleep(wait_time)

        #             except:
        #                 print("scrape failed")

    def extract_text(self, path, filename, keywords):
        print("extractor selected...")
        applicator = Applicator()
        cleaner = Cleaner()
        formatter = Formatter()
        extractor = Extractor()

        text = ""
        sent_min = 4
        sent_max = 24
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
        # cleaner.remv_firstperson()
        # cleaner.remv_secondperson()

        #Specific items to remove
        cleaner.remv_excaps()
        cleaner.remv_exletters()
        cleaner.remv_badpgs()
        cleaner.remv_badcoms()

        #Fix sentence spacing after removing characters
        # cleaner.remv_wtspace()
        # cleaner.remv_endspace()
        cleaner.remv_punspace()
        
        #Trim the length and check spelling
        cleaner.trim_sentlist(sent_min, sent_max)
        cleaner.check_misspelled("/home/lux/dev/felow/words")

        sent_list = cleaner.get_sentlist()

        #Format sentences as text list
        formatter.set_sentlist(sent_list)
        formatter.frmt_textlist()
        text = formatter.get_text()

        #apply text to .txt doc
        applicator.set_text(text)
        applicator.apply_text(filename)

        #Add extracted references to text file
        formatted_refs = formatter.frmt_references(ref_list, "MLA")
        
        for refrnc in formatted_refs:
            applicator.set_text(refrnc)
            applicator.apply_text("references.txt")

        # #Create keyword list
        # if keywords == True:
        #     print("keyword extraction selected...")
        #     print("creating keywords.txt...")
        #     extractor.set_text(text)
        #     keyword_list = extractor.extract_keywords()
        #     kwd_text = ""
        #     for kwd in keyword_list:
        #         kwd_text = kwd_text + kwd
        #         kwd_text = kwd_text + "\n"

        #     applicator.set_text(kwd_text)    
        #     applicator.apply_text("keywords.txt")

    def build_weight(self, epochs, source, weightname, numepochs):
        print("builder selected...")
        builder = Builder()
        builder.build_weight(source, epochs, numepochs, weightname)

    def generate_document(self, numwords, filename, weightname, title, lines, temp, clean):
        print("generator selected...")
        applicator = Applicator()
        cleaner = Cleaner()
        extractor = Extractor()
        formatter = Formatter()
        generator = Generator()
        
        sent_list = []
        len_check = 0 
        sent_min = 4
        sent_max = 24
        # keywords = False

        #Set selected weight
        generator.set_weight(weightname)

        # #Check for keyword text and build list
        # if os.path.exists("keywords.txt"):
        #     print("keywords.txt found...")
        #     extractor.extract_text("keywords.txt")
        #     keyword_text = extractor.get_text()
        #     temp_text = ""
        #     keyword_list = []
        #     keywords = True
        #     for char in keyword_text:
        #         if char == "\n":
        #             keyword_list.append(temp_text)
        #             temp_text = ""
                
        #         else:
        #             temp_text = temp_text + char

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
                # cleaner.remv_wtspace()
                # cleaner.remv_noalpha()
                # cleaner.remv_nodeclare()
                # cleaner.remv_nums()
                # cleaner.remv_endspc()
                # cleaner.remv_noleadcap()
                # cleaner.remv_excap()
                # cleaner.remv_firstperson()
                # cleaner.remv_secondperson()
                # cleaner.remv_letters()
                # cleaner.remv_dupwords()
                cleaner.trim_sentlist(sent_min, sent_max)
                cleaner.check_misspelled("/home/lux/dev/felow/words")

                # #Check for keywords
                # if keywords == True:
                #     cleaner.check_keywords(keyword_list)

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
        par_len = 175
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
download.add_argument("-spg", "--startpage", action="store", dest="startpage", type=int, default=1)
download.add_argument("-epg", "--endpage", action="store", dest="endpage", type=int, default=3)
download.add_argument("-fts", "--filetypes", action = "store", dest="filetypes", default=["pdf", "doc"])

#ext subparsers
extract = subparsers.add_parser(name="ext")
extract.add_argument("-p", "--path", action="store", dest="path", required=True)
extract.add_argument("-f", "--filename", action="store", dest="filename", default="extract.txt")
extract.add_argument("-kwd", "--keywords", action="store", dest="keywords", default=True)

#bld subparsers
build = subparsers.add_parser(name="bld")
build.add_argument("-epo", "--epochs", action="store", type=int, dest="epochs", required=True)
build.add_argument("-src", "--source", action="store", dest="source", default="extract.txt")
build.add_argument("-wgt", "--weightname", action="store", dest="weightname", default="weight.hdf5")
build.add_argument("-num", "--numepochs", action="store", type=int, dest="numepochs", default=False)

#gen subparsers
generate = subparsers.add_parser(name="gen")
generate.add_argument("-num", "--numwords", action="store", dest="numwords", type=int, required=True)
generate.add_argument("-f", "--filename", action="store", dest="filename", required=True)
generate.add_argument("-wgt", "--weightname", action="store", dest="weightname", default="weight.hdf5")
generate.add_argument("-ttl", "--title", action="store", dest="title", default="Title")
generate.add_argument("-lns", "--lines", action="store", dest="lines", type=int, default=1)
generate.add_argument("-tmp", "--temp", action="store", dest="temp", type=float, default=[0.2, 0.5])
generate.add_argument("-cln", "--clean", action="store", dest="clean", default=True)

#tst subparsers
test = subparsers.add_parser(name="tst")

#set arguments
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
    keywords = args.keywords
    felow.extract_text(path, filename, keywords)

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
    filename = args.filename
    weightname = args.weightname
    title = args.title
    lines = args.lines
    temp = args.temp
    clean = args.clean
    felow.generate_document(numwords, filename, weightname, title, lines, temp, clean)

elif args.command == "tst":
#     #Add test function here
#     print("for testing...")
    extractor = Extractor()
    #Check for keyword text and build list
    if os.path.exists("metadata.txt"):
        print("metadata.txt found...")
        f = open("metadata.txt", "r")
        meta_list = f.readlines()
        print(meta_list)

    new_list = []
    remove_list = ["\n", "{", "}"]
    for meta in meta_list:
        for char in remove_list:  
            meta = meta.strip(char)

        new_list.append(meta)

    meta_list = new_list
    
    new_list = []
    for dct in meta_list:
        # print(dct)
        temp_dict = {}
        field_list = dct.split(",")
        for fld in field_list:
            values = fld.split(":")
            print(values)
            try:
                temp_dict[values[0]] = values[1]
                print(values[0])
                print(values[1])

            except:
                print("value not found")

        new_list.append(temp_dict)

    print(new_list)


else:
    print("command not found")
    print("use -h or --help for available commands")