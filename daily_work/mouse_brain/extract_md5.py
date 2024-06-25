import pandas as pd
from pathlib import Path

info = pd.read_csv("/find_md5.csv")

name = 'md5.txt'
first_md5 = []
first_file = []
second_md5 = []
second_file = []
for path in info.File_path:
    file_path = Path(path).parent
    combined_path = file_path / name
    with combined_path.open("r", encoding="utf-8") as f:
        content = f.read()
    first_md5 += content.split("\n")[0].split("  ")[0]
    first_file += content.split("\n")[0].split("  ")[1]
    second_md5 += content.split("\n")[1].split("  ")[0]
    second_file += content.split("\n")[1].split("  ")[1]
    
info["File_1"] = first_file
info["File_1_md5"] = first_md5
info["File_2"] = second_file
info["File_2_md5"] = second_md5

info.to_csv("final_result.csv", index=None)