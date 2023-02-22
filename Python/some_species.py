import pandas as pd

data_procession = []
with open('/home/ouconstand/data/Virus_Host/Virion.csv','r', encoding='ISO-8859-1') as f:
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

# sapecies list
species_list = ['homo sapiens', 'sus scrofa', 'canis lupus', 'felis silvestris', 'gallus gallus', 'bos taurus', 'ovis aries', 'capra hircus']

# empty dataframe
final_dataframe = pd.DataFrame(columns=['Host', 'HostTaxID', 'Virus', 'VirusTaxID', 'VirusFamily', 'Count', 'Trans_Infect_Count'])

# construct a circle to finish this work
for species in species_list:
    species_data = data[data['Host'] == species]
    # the first step to statistic the count of virus
    virus_count = pd.DataFrame(species_data[['HostTaxID', 'VirusTaxID']].value_counts())
    # remove duplication
    species_data = species_data[['Host', 'HostTaxID', 'Virus', 'VirusTaxID', 'VirusFamily']].drop_duplicates(subset=['HostTaxID', 'VirusTaxID']) # basic information
    
    # the second step to statistic the count of virus
    virus_count = virus_count.reset_index()
    virus_count.columns = ['HostTaxID', 'VirusTaxID', 'Count']
    virus_count = virus_count[['VirusTaxID', 'Count']]

    # to statistic the count of trans-family virus
    virus_list = list(species_data['VirusTaxID'])
    trans_family = data[data['VirusTaxID'].isin(virus_list)] # from raw data to statistic the trans-family information
    trans_family = trans_family[['VirusTaxID', 'HostFamily']].drop_duplicates(subset=['VirusTaxID', 'HostFamily'])
    trans_count = pd.DataFrame(trans_family['VirusTaxID'].value_counts())
    trans_count = trans_count.reset_index()
    trans_count.columns = ['VirusTaxID', 'Trans_Infect_Count']

    # merge different dataframe
    tem_dataframe_1 = pd.merge(species_data, virus_count, how='inner', on='VirusTaxID')
    tem_dataframe_2 = pd.merge(tem_dataframe_1, trans_count, how='inner', on='VirusTaxID')
    final_dataframe = pd.concat([final_dataframe, tem_dataframe_2], ignore_index=True)

final_dataframe.to_csv('name', index=None)