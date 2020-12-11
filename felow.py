           
##FELOW##

import argparse
import textwrap
import os
import time

from applicator import Applicator
from builder import Builder
from cleaner import Cleaner
#from documenter import Documenter
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
        extractor = Extractor()
        cleaner = Cleaner()
        print("batching text...")
        for doc in os.listdir(path):
            #extract text from document
            ##The splitter function sets the ext internally##
            extractor.split_ext(doc)
           
            ##Is this necessary?##
            # ext = extractor.get_ext()
            # extractor.set_ext(ext)
           
            extractor.extract_text(os.path.join(path, doc))
            text = extractor.get_text()
            
            #Add text to cleaner
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

            text = text + cleaner.get_text()
            
    else:
        print("not a path")
        raise SystemExit

    #Add collected text to cleaner
    cleaner.set_text(text)
    cleaner.build_sentlist()
    cleaner.remv_nodeclare()
    cleaner.remv_nums()
    cleaner.remv_wtspc()
    cleaner.remv_noalead()
    cleaner.trim_sentlist(28, 140)
    cleaner.remv_excap()
    #cleaner.fix_language() 
    cleaner.remv_language()

    #Format text as list
    cleaner.frmt_textlist()
    text = cleaner.get_text()

    #apply text to .txt doc
    applicator = Applicator()
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
    
    #Generate text based on word count
    text = ""
    len_check = 0 
    cleaner = Cleaner()
    generator = Generator()
    generator.set_weight(weight)
    print("generating document...")
    while True:
        #Get remaining word count
        text_len = len(text.split())
        gen_num = numwords - text_len
        
        #Generate text based on remaining word count
        generator.gen_text(gen_num, lines, temp)
        text_list = generator.get_text_list()
        
        #Get length of generated text plus stored text
        gen_len = generator.get_textlength()
        len_check = text_len + gen_len
        print(str(len_check) + " words collected...")

        #Store text length before cleaning generated text
        old_len = len_check

        #Collect text and build sentence list
        cleaner.set_sentlist(text_list)
        cleaner.frmt_textstring()
        cleaner.build_sentlist()

        #Clean text in sentence list
        cleaner.remv_nodeclare()
        cleaner.remv_nums()
        cleaner.remv_wtspc()
        cleaner.remv_noalead()
        cleaner.trim_sentlist(28, 140)
        cleaner.fix_language()
        cleaner.remv_excap()
        cleaner.remv_language()
        
        #Format cleaned sentence list as string
        cleaner.frmt_textstring()
        cleaned_text = cleaner.get_text()
        
        #Collect cleaned text
        text = text + cleaned_text

        #Check length again
        new_len = len(text.split())
        disc_len = old_len - new_len
        print("old length: " + str(old_len))
        print("new length: " + str(new_len))
        len_check = new_len
        
        ####This wil be negative if no words are discarded###
        print(str(disc_len) + " words discarded...")
            
        #Break loop when word count reached
        if len_check >= numwords:
            break

    #Format generated text
    par_len = 175
    cleaner.set_text(text)
    cleaner.build_sentlist()
    cleaner.remv_wtspc()
    cleaner.frmt_textblock(par_len)
    text = cleaner.get_text()

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
    
    #Build finder
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

        #Page in increments of 10 for google scholar
        page += 10
        time.sleep(wait_time)
        print("checking page " + str(int(page/10)) + "...")

    #Set a file type to parse
    my_links = finder.filter_links(link_list, parseword)
    print(my_links)

    #Download links
    finder.dl_links(my_links)

elif args.command == "--help":
    print("hello")

else:
    print("command not found")
    print("use -h or --help for available commands")