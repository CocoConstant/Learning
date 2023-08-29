import pandas as pd
from pathlib import Path
import argparse

# user helper
parser = argparse.ArgumentParser()
parser.add_argument("diractory", help = "providing diractory")
args = parser.parse_args()

# input diractory path
dir_path = Path(args.diractory)

# construct input file
output = []

for chip_name in dir_path.iterdir():
    for segment in chip_name.iterdir():
        
        ipr_file = list(segment.glob("*.ipr"))
        tar_gz_file = list(segment.glob("*.tar.gz"))
        out_dir = segment / 'output'

        output.append([segment.absolute(), out_dir.absolute(), ipr_file[0], tar_gz_file[0], ipr_file[0].stem])

pd.DataFrame(output, columns=['Input_dir', 'Output_dir', 'Ipr_file', 'Tar.gz_file', 'Prefix']).to_csv(dir_path.parent / 'input.csv', index=None)