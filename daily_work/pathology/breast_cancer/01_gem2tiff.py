"""
======================================================
@File   : 01_gem2tiff.py
@Author : ouyangkang
@Date   : 2025.03.03
@Email  : ouyangkang@genomics.cn
@Desc   : generate tiff file based on gem file in bin 1 level
@mirror : spateo_scanpy
@Version: v1
@Update : 2025.03.03
======================================================

update record：
- 2025.03.03：todense() is changed to toarray() to avoid memory overflow during large-scale data conversion.
"""


import numpy as np
from PIL import Image
import spateo as st
import matplotlib.pyplot as plt
import sys

def convert_gem2tiff(input_file, chip_id):
    """
    converting gem file to bin1 tif image for downstream registering HE image and bin1 image
    
    Parameters:
        input_file (str): raw gem file
        chip_id (str): the chip id
        
    Return:
        None: the function without return, but it will save the following file:
            - {chip_id}_bin1_beforePS.tiff : the tif image of bin1
    """
    adata = st.io.read_bgi_agg(input_file)
    img = adata.X.toarray()
    img[img > 10] = 10
    img = img / 10 * 255 # Convert to grayscale image
    
    plot_data = Image.fromarray(adata.X.toarray().T)

    if img.shape == adata.shape:
        img = Image.fromarray(img.T)
        img = img.convert("L")
        img.save(f'./{chip_id}_bin1_beforePS.tiff')
    else:
        raise ValueError(f"Shape mismatch: img.shape is {img.shape}, but adata.shape is {adata.shape}.\nPlease check your input data")
        
    return plot_data
        
def plot_chip(plot_data, chip_id):
    """
    plotting bin1 image
    
    Parameters:
        plot_data (np.array): image numpy array data
        chip_id (str): the chip id
        
    Return:
        None: the function without return, but it will save the following file:
            - {chip_id}_bin1_beforePS.png : th png image of  bin1
    """
    plt.figure(figsize=(6, 8))
    plt.imshow(plot_data, cmap='viridis', vmax='1')
    plt.axis('off')
    plt.savefig(f'./{chip_id}_bin1_beforePS.png', format='png')
    
    
if __name__ == "__main__":
    # parameter infomation
    input_file = sys.argv[1] # for example: '/data/input/Files/ResultData/Workflow/T202412180002227/04.tissuecut/Y00724H9.gem.gz'
    chip_id = sys.argv[2] # Y00724H9
    plot_data = convert_gem2tiff(input_file, chip_id)
    plot_chip(plot_data, chip_id)