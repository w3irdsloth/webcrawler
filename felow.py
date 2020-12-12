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
from documenter import Documenter
from extractor import Extractor
from finder import Finder
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
     #############abcdefg############    ########### Writer. #######
      ############ ###### ########### ####         ########### 
        ###########      ###########
                ############        
                 ##########
------------------------------------------------------------
Apply | Build | Clean | Document | Extract | Find | Generate
------------------------------------------------------------ 
         '''))

subparsers = parser.add_subparsers(title="commands", dest="command")

#batch subparsers
batch = subparsers.add_parser(name="btc")
batch.add_argument("-p", "--path", action="store", dest="path", required=True)
batch.add_argument("-f", "--filename", action="store", dest="filename", default="extract.txt")

#set build subparsers
build = subparsers.add_parser(name="bld")
build.add_argument("-f", "--filename", action="store", dest="filename", required=True)
build.add_argument("-epo", "--epochs", action="store", type=int, dest="epochs", required=True) 
build.add_argument("-num", "--numepochs", action="store", type=int, dest="numepochs", default=False)
build.add_argument("-wgt", "--weightname", action="store", dest="weightname", default="weight.hdf5")

#set generate subparsers
generate = subparsers.add_parser(name="gen")
generate.add_argument("-num", "--numwords", action="store", dest="numwords", type=int, required=True)
generate.add_argument("-lns", "--lines", action="store", dest="lines", type=int, default=1)
generate.add_argument("-tmp", "--temp", action="store", dest="temp", type=float, default= 0.5)
generate.add_argument("-wgt", "--weight", action="store", dest="weight", required=True)
generate.add_argument("-tag", "--tag", action="store", dest="tag", default="<content>")
generate.add_argument("-f", "--filename", action="store", dest="filename", required=True)
generate.add_argument("-t", "--title", action="store", dest="title", default="Title")

#set download subparsers
download = subparsers.add_parser(name="dln")
download.add_argument("-qry", "--query", action="store", dest="query", required=True)
download.add_argument("-hdr", "--headers", action="store", dest="headers", default={'user-agent': "Mozilla/5.0 (Linux x86_64; rv:83.0) Gecko/20100101 Firefox/83.0"})
download.add_argument("-eng", "--engine", action="store", dest="engine", default="g_scholar")
download.add_argument("-spg", "--startpage", action="store", dest="startpage", default=0)
download.add_argument("-epg", "--endpage", action="store", dest="endpage", default=50)
download.add_argument("-prs", "--parseword", action="store", dest="parseword", default=".pdf")

#Get arguments
args = parser.parse_args()

#Batch text from documents to .txt file
if args.command == "btc":
    path = args.path
    filename = args.filename
    if os.path.isdir(path):
        applicator = Applicator()
        cleaner = Cleaner()
        documenter = Documenter()
        extractor = Extractor()

        sent_list = []
        print("batching text...")
        for doc in os.listdir(path):
            #extract text from document
            extractor.split_ext(doc)
            extractor.extract_text(os.path.join(path, doc))
            text = extractor.get_text()
            
            #Add extracted text to cleaner
            cleaner.set_text(text)

            #clean cover
            string_list = ["Name", "Academic Institution", "Author Note", "Class", "Professor", "Date"]
            cleaner.remv_strings(string_list)
            
            #clean pars
            char1 = "("
            char2 = ")"
            cleaner.remv_slices(char1, char2)
        
            #clean quotes
            char1 = "\""
            char2 = "\""
            cleaner.remv_slices(char1, char2)

            #clean refs
            page_list = ["References", "Works Cited", "Bibliography"]
            cleaner.remv_pages(page_list)

            #Convert cleaned text into list
            cleaner.build_sentlist()
            temp_list = cleaner.get_sentlist()

            #Collect cleaned cleaned sentences
            for sentc in temp_list:
                sent_list.append(sentc)
            
    else:
        print("not a path")
        raise SystemExit

    #Clean collected sentence list
    cleaner.set_sentlist(sent_list)
    cleaner.remv_nodeclare()
    cleaner.remv_nums()
    cleaner.remv_wtspc()
    cleaner.remv_noalead()
    cleaner.trim_sentlist(28, 140)
    cleaner.remv_excap()
    #cleaner.fix_language() 
    cleaner.remv_language()
    sent_list = cleaner.get_sentlist()

    #Format sentences as text list
    documenter.set_sentlist(sent_list)
    documenter.frmt_textlist()
    text = documenter.get_text()

    #apply text to .txt doc
    applicator.set_text(text)
    applicator.split_ext(filename)
    applicator.apply_text(filename)

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

    cleaner = Cleaner()
    documenter = Documenter()
    generator = Generator()
    generator.set_weight(weight)
    
    sent_list = []
    len_check = 0 
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
        cleaner.remv_noalead()
        cleaner.trim_sentlist(28, 140)
        cleaner.fix_language()
        cleaner.remv_excap()
        cleaner.remv_language()
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
    documenter = Documenter()
    documenter.set_sentlist(sent_list)
    documenter.frmt_textblock(par_len)
    text = documenter.get_text()

    #Apply title to document
    applicator = Applicator()
    applicator.set_text(title)
    applicator.set_tag("Title")
    applicator.split_ext(filename)
    applicator.apply_text(filename)
    
    #Apply generated text to document
    applicator.set_text(text)
    applicator.set_tag(tag)
    applicator.split_ext(filename)
    applicator.apply_text(filename)

elif args.command == "dln":
    query = args.query
    headers = args.headers
    engine = args.engine
    startpage = args.startpage
    endpage = args.endpage
    parseword = args.parseword
    
    finder = Finder()

    #Set search engine
    finder.set_searchengine(engine)

    #Retreive HTML
    link_list = []
    wait_time = 5
    page = startpage
    print("checking page " + str(int(page / 10)) + "...")
    while page <= endpage: 
        #Build url from search engine and query
        finder.build_url(query, page)
        print("scraping " + finder.get_url + "...")

        #retreive html
        html = finder.find_html(headers)
        print(html)

        #parse links from html
        links = finder.find_links(html)

        for lnk in links:
            link_list.append(lnk)

        #Increment page by 10 for google/scholar
        page += 10
        time.sleep(wait_time)
        print("checking page " + str(int(page/10)) + "...")

    #Parse by filetype
    my_links = finder.filter_links(link_list, parseword)
    print(my_links)

    #Download links
    finder.dl_links(my_links)

else:
    print("command not found")
    print("use -h or --help for available commands")