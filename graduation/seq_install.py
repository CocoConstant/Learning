# Complete code

import pandas as pd
from bs4 import BeautifulSoup

data = pd.read_table('taxid10239.nbr', comment='#', header=None, names=["Representative","Neighbor","Host","Selected lineage","Taxonomy name","Segment name"]) # get information
accession = list(data['Neighbor']) # extract 'Neighbor' information

# Becauce the RetMax is 20, I slices their length with 20 and the last length is 13
for i in range(1,13051):
    segment = accession[(i-1)*20:i*20]
    
    # Using requests function get the id of term
    term_url = 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=nucleotide&api_key=f7aed0f55f83d46ff0249e3e1830661bef08&term=' + ",".join(segment)
    term_info = requests.get(term_url).text
    soup = BeautifulSoup(term_info, 'html.parser')

    accession_id = [k.text for k in soup.find_all('id')] # get id

    # get sequencing information from id
    fasta_url = 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nucleotide&rettype=fasta&id={}&api_key=f7aed0f55f83d46ff0249e3e1830661bef08'.format(','.join(accession_id))
    fasta_info = requests.get(fasta_url).text

    # get fasta file
    with open("/home/bio_kang/Learning/Python/requests/data/sequence_{}.fasta".format(i), 'w') as f:
        f.write(fasta_info)