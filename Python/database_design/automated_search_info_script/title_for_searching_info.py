# import necessary packages
import requests
from bs4 import BeautifulSoup
import re
import sys
import pandas as pd

# basic infomation and related infomation provided by you
API_KEY = "59cbd6ff6b3ce5d506f0eeb69e4e09362409"
query_info = sys.argv[1]

# using e-search for matching UIDs corresponding your query
search_url = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&api_key={API_KEY}&term={query_info}"

# result of searching in pubmed 
search_info = BeautifulSoup(requests.get(search_url).text, 'html.parser')

# uid
uid_info = search_info.find_all('id')[0].text

# a judgement to avoid emerging errros
if uid_info == None:
    # if the script not get UID, it cann't search more info
    print("Sorry, the function cann't provide any related infomation based on title you provided")
else:
    # using e-fetch to obtain detailed info
    fetch_url = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id={uid_info}&api_key={API_KEY}&rettype=medline&retmode=text"
    detailed_info = BeautifulSoup(requests.get(fetch_url).text, 'html.parser')
    # detailed info
    pmid = str(detailed_info).split("\nPMID-")[1].split('\n')[0].strip()
    
    doi_pattern = re.compile(r'LID - (.*) \[doi\]')
    doi = re.findall(doi_pattern, str(detailed_info))[0]

    journal = str(detailed_info).split("\nJT  -")[1].split('\n')[0].strip()
    
    if len(str(detailed_info).split("\nDEP -")) > 1:
        tmp_pub_date = str(detailed_info).split("\nDEP -")[1].split('\n')[0].strip()
        pub_date = tmp_pub_date[:4] + '/' + tmp_pub_date[4:6] + '/' + tmp_pub_date[6:]
    else:
        pub_date = None

    author_pattern = re.compile(r'FAU(.*)')
    authors = ";".join([i.strip(' - ') for i in re.findall(author_pattern, str(detailed_info))])
    try:
        institution = str(detailed_info).split('AD')[1].split('FAU')[0].strip('\n').strip('- .').replace('\n      ', '').rsplit(',', 3)[0]
    except:
        institution = ""
    link = 'https://doi.org/' + doi
    try:
        country = str(detailed_info).split('AD')[1].split('FAU')[0].strip('\n').strip('- .').split(',')[-1].strip()
    except:
        country = ""
    
    df = pd.DataFrame([pmid, doi, journal, pub_date, authors, institution, link, country]).T
    df.columns = ["PMID", "DOI", "Journal", "Publication Date", "Authors", "Institution", "Link", "Country"]
    df.to_csv(sys.argv[2], index=None)