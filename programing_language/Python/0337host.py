import pandas as pd
import sys

inputfile_1 = sys.argv[1] # raw virion csv
inputfile_2 = sys.argv[2] # representational sequence data
inputfile_3 = sys.argv[3] # length data

# raw data
data_procession = []
with open(inputfile_1,'r', encoding='ISO-8859-1') as f:
    for line in f.read().splitlines():
        data = line.split('\t')
        if len(data) < 34:
            continue
        else:
            if data[2] == '' or data[3] == '' or data[7] == '' or data[33] == '': # delete non host genus, host id, virus id and NCBIAccession data
                continue
            else:
                data_procession.append(data)

data = pd.DataFrame(data_procession[1:-1],columns=data_procession[0])

coro = data[data['VirusFamily'] == 'coronaviridae']

host_info = coro[['HostTaxID', 'HostGenus', 'HostFamily', 'HostOrder', 'HostClass']]
host_info = host_info.drop_duplicates(['HostTaxID'])

# representational data
seq_data = pd.read_csv(inputfile_2)

# length data
seq_length = pd.read_table(inputfile_3, sep='\t')
seq_length.columns = ['Representation', 'Length']

# merge
df_1 = pd.merge(seq_data, seq_length, how='inner', on='Representation')
df_2 = pd.merge(df_1, host_info, how='inner', on='HostTaxID')

df_2.to_csv('host_taxon_info.csv', index=None)