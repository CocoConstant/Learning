'''
you need input the data file with csv format and its title
exsample: python temporary_intermediate_file.py file_path
'''
import sys
import pandas as pd

file_path = sys.argv[1]
initial_data = pd.read_csv(file_path)
extract_info = pd.DataFrame(columns=['Project_ID', 'Library_ID', 'Data_path'])

for index, row in initial_data.iterrows():
    extract_info.loc[index] = [row.项目编号, row.文库号, row.二级路径]

extract_info.to_csv('/mnt/c/Users/ouyangkang/Desktop/extract_info.txt', sep='\t', index=None)
