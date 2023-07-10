'''
you need to input the data file with csv format and its title
exsample: python temporary_intermediate_file.py file_path output_dir
'''
import sys
import pandas as pd
import os

file_path = sys.argv[1]
output_dir = sys.argv[2]
initial_data = pd.read_csv(file_path)
extract_info = pd.DataFrame(columns=['ProjectID', 'SubProjectID', 'SampleID','LibraryID', 'Datapath', 'Mark', 'InsertSize', 'SubSampleID'])
for index, row in initial_data.iterrows():
    extract_info.loc[index] = [row.项目编号, row.项目编号, row.样品名称, row.文库号, row.二级路径, 1, 500, row.文库类型]

extract_info['SampleID'] = [i.rsplit('-', 1)[0] for i in extract_info['SampleID']]
extract_info['SubSampleID'] = [i.rsplit('_', 1)[1] for i in extract_info['SubSampleID']]
extract_info['SubSampleID'] = [i.capitalize() if 'o' in i else i for i in extract_info['SubSampleID']]

final_info = pd.DataFrame(columns=['ProjectID', 'SubProjectID', 'SampleID','LibraryID', 'FQ1', 'FQ2', 'Mark', 'InsertSize', 'SubSampleID'])
initial_num = 0 # set the number for account
for index, row in extract_info.iterrows():
    data_file = sorted([i for i in os.listdir(row.Datapath) if '.fq.gz' in i])
    if len(data_file)/2 > 1:
        for i in range(int(len(data_file))/2):
            final_info.loc[initial_num] = [row.ProjectID, row.SubProjectID, row.SampleID, row.LibraryID, row.Datapath + '/'+ data_file[i*2], row.Datapath + '/'+ data_file[i*2+1], row.Mark, row.InsertSize, row.SubSampleID]
            initial_num += 1
    else:
        final_info.loc[initial_num] = [row.ProjectID, row.SubProjectID, row.SampleID, row.LibraryID, row.Datapath + '/'+ data_file[0], row.Datapath + '/'+ data_file[1], row.Mark, row.InsertSize, row.SubSampleID]
        initial_num += 1

final_info.to_csv(output_dir + '/' + 'batch_submit.tsv', sep='\t', index=None)
