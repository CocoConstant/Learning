# Complete code

import pandas as pd
from bs4 import BeautifulSoup
import requests
import re


# the function is designed to get fasta format information
def get_url_info(segment):

    # Using requests function get the id from term
    term_url = 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=nucleotide&api_key=f7aed0f55f83d46ff0249e3e1830661bef08&term=' + ",".join(segment)
    term_info = requests.get(term_url).text
    soup = BeautifulSoup(term_info, 'html.parser')

    # get id
    accession_id = [k.text for k in soup.find_all('id')]

    # get sequencing information from id
    fasta_url = 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nucleotide&rettype=fasta&id={}&api_key=f7aed0f55f83d46ff0249e3e1830661bef08'.format(','.join(accession_id))
    fasta_info = requests.get(fasta_url).text
    return fasta_info


# this function is designed to write files
def write_file(fasta_info,name_num):
    with open("/home/bio_kang/Learning/Python/requests/data/sequence_{}.fasta".format(name_num), 'w') as f:
        f.write(fasta_info)


# read information from taxid10239.nbr file
data = pd.read_table('taxid10239.nbr', comment='#', header=None, names=["Representative","Neighbor","Host","Selected lineage","Taxonomy name","Segment name"])

# extract 'Neighbor' information
accession = list(data['Neighbor']) 

undownloaded_term = [] # record file unsuccessfulely downloaded

# using try-except structure to avoid program stop
for i in range(1,13051):
    segment = accession[(i-1)*20:i*20]
    try:
        fasta_info = get_url_info(segment)
        write_file(fasta_info, i)
    except:
        pattern = re.compile(r'[A-Z]{1,2}\d{5,6}')
        undownloaded_term = undownloaded_term + re.findall(pattern, fasta_info)
