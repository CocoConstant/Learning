import re

with open('virion_coronaviridae_accession.csv', 'r') as f:
    lines = f.readlines()
    f.close()

accession = []
id = []

num_id = re.compile('\d')

for line in lines:
    line = line.split(',')
    accession += line
print(len(accession))