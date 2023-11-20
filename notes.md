#### Startup ####

#Install pip build packages 
sudo dnf install gcc-c++ pkgconfig poppler-cpp-devel python3-devel

#Create virtual environment
python3 -m venv .venv

#Acvivate virtual environment
source .venv/bin/activate

#Install PIP packages
Required [
    requests,
  ]

Supported [
    texttopdf,
    pymupdf,
    docx,
  ]



##################
## FELO Commands ##
###################
get-status - Return response status from url
[url]

crawl-web - Crawl web from seed url and generate index of links
[url, lnks, tmt, db]

print-links - Print links from database file 
[db]

merge-data - Merge 2 database files 
[db1, db2, db]

print-html - Print html from url to console or file
[url, doc]

read-text - Read text from .txt file to console
[doc]

read-html - Read html from doc and print to console based on tags; Can return only links.
[doc, tag, lnks]




