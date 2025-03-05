import pandas as pd
import sys
from pathlib import Path


input_file = sys.argv[1]

data = pd.read_excel(input_file)
data = data[(data['状态'] != '终止') & (data['状态'].notna())]

output_df = pd.DataFrame(columns=['EntityID', 'SN', 'FASTQ1', 'FASTQ2', 'MASK', 'ImageTar', 'ImagePreDir', 'IPR', 'SplitNum', 'Tissue', 'CIDStart', 'CIDLength', 'MIDStart', 'MIDLength', 'rRNARemove', 'LargeChip', 'Reference',
                                  'CellSpecies', 'CellSample'])

for index, row in data.iterrows():
    dir_path = Path(row['二级路径'])
    barcode_list = row['Barcode号'].split('&')
    lane = row['Lane']
    seq_chip = row['芯片号']
    sample_id = row['样品名称']
    SN = row['SN号']

    if len(barcode_list) == 1:
        min_num = int(barcode_list[0].split('~')[0])
        max_num = int(barcode_list[0].split('~')[-1])
        for num in range(min_num, max_num+1):
            fq1_path = dir_path / f'{seq_chip}_{lane}_{num}_1.fq.gz'
            fq2_path = dir_path / f'{seq_chip}_{lane}_{num}_2.fq.gz'

            result_list = [sample_id, SN, fq1_path, fq2_path, f'/Files/RawData/{SN}.barcodeToPos.h5', None, None, None, 16, 'cell', 0, 25, 25, 10, 'FALSE', 'FALSE', 'human', 'human', 'pbmc']
            output_df.loc[len(output_df)] = result_list
    else:
        for num_list in barcode_list:
            min_num = int(num_list.split('~')[0])
            max_num = int(num_list.split('~')[-1])
            for num in range(min_num, max_num+1):
                fq1_path = dir_path / f'{seq_chip}_{lane}_{num}_1.fq.gz'
                fq2_path = dir_path / f'{seq_chip}_{lane}_{num}_2.fq.gz'
                result_list = [sample_id, SN, fq1_path, fq2_path, f'/Files/RawData/{SN}.barcodeToPos.h5', None, None, None, 16, 'cell', 0, 25, 25, 10, 'FALSE', 'FALSE', 'human', 'human', 'pbmc']
                output_df.loc[len(output_df)] = result_list

output_df.to_csv('output.csv', index=None)