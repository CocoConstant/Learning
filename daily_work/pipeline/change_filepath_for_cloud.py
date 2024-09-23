import pandas as pd
from pathlib import Path
import sys

# read data
file_path = sys.argv[1]
data = pd.read_csv(file_path)

# these parts will be change for DCS platform scRNA workflow
modified_list = ["cDNA1", "cDNA2", "Oligo1", "Oligo2"]

# create a loop to finish change pathway
for part in modified_list:
    new_path = []
    for path in data[part]:
        path = Path(path)
        path = path.name
        path = "/File/RawData/OYK/" + path
        new_path += [path]
    data[part] = new_path

data.to_csv(file_path, index=None)