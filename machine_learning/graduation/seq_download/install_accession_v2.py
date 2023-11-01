#!/home/bio_kang/software/anaconda3/bin/python

# import essential library
import re
import requests
import sys

# open file and get data
with open('/home/bio_kang/Learning/bioinformatics/virion_coronaviridae_accession.csv', 'r') as f:
    lines = f.readlines()
    f.close()

# this is a empty list to collect accession number
accession = []

pattern_acce = re.compile(r'[A-Z]{1,2}\d+')
for line in lines:
    accession += re.findall(pattern_acce, line)

# remove duplication accession
accession = list(set(accession))

# get id information and fasta imformation and write info to file
def get_url_info_id(segment,num):

    # Using requests function get the id from term
    term_url = 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=nucleotide&api_key=6e2f58038b074d964bb8b87f43623af7b508&term=' + ",".join(segment)
    term_info = requests.get(term_url, timeout=(5,5)).text
 
    id_pattern = re.compile(r'<Id>(\d+)</Id>')
    accession_id = re.findall(id_pattern, term_info)

    # get sequencing information from id
    fasta_url = 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nucleotide&rettype=fasta&id={}&api_key=59cbd6ff6b3ce5d506f0eeb69e4e09362409 '.format(','.join(accession_id))
    with open('/home/bio_kang/Learning/bioinformatics/sequence_{}.fasta'.format(num),'wb') as f, requests.get(fasta_url,stream=True) as info:
        for chunk in info.iter_content(chunk_size=256*1024):
            if not chunk:
                break
            f.write(chunk)


for i in range(int(sys.argv[1]),(int(sys.argv[1])+200)):
    id_list = accession[i*20:(i+1)*20]
    get_url_info_id(id_list, i)
