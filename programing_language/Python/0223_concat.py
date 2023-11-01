import pandas as pd
import sys

print('#'*20 + 'start processing' + '#'*20)
# file name
file_1 = sys.argv[1]
file_2 = sys.argv[2]
file_3 = sys.argv[5]
trans_file = sys.argv[3]
trans_type = sys.argv[4]

hv_acce = pd.read_csv(file_1)
hv_acce.columns = ['VirusTaxID', 'HostTaxID', trans_type]

trans = pd.read_table(trans_file, sep='\t')
trans.columns = [trans_type, 'Accession']

rep_acce = pd.read_table(file_2, sep='\t')
rep_acce.columns = ['Representation', 'Accession']

tem_1 = pd.merge(hv_acce, trans, how='inner', on=trans_type)

tem = pd.merge(tem_1, rep_acce, how='inner', on='Accession')

print('#'*20 + 'start deleting duplications' + '#'*20)

tem.drop_duplicates(subset=['VirusTaxID', 'HostTaxID', 'Accession'], inplace=True)
tem.to_csv(file_3, index=None)

print('#'*20 + 'Congratulations!!!' + '#'*20)