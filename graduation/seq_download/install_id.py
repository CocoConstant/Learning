#!/home/bio_kang/software/anaconda3/bin/python


# import essential library
import re
import requests

# open file and get information
with open('/home/bio_kang/Learning/bioinformatics/virion_coronaviridae_accession.csv', 'r') as f:
    lines = f.readlines()
    f.close()

id = []

pattern_id = re.compile(r'^\d+')
for line in lines:
    id += re.findall(pattern_id, line)


# install sequence data function
def get_fasta_info(id):
    # get sequencing information from id
    fasta_url = 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nucleotide&rettype=fasta&id={}&api_key=6e2f58038b074d964bb8b87f43623af7b508'.format(','.join(id))
    fasta_info = requests.get(fasta_url).text
    return fasta_info

# write file function
def write_file(fasta_info,name_num):
    with open("/home/bio_kang/Learning/bioinformatics/sequence_{}.fasta".format(name_num), 'w') as f:
        f.write(fasta_info)

# accomplish work
for i in range(70):
	id_list = id[i*20:(i+1)*20]
	fasta_info = get_fasta_info(id_list)
	write_file(fasta_info,i)
