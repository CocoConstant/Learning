"""
======================================================
@File   : 02_based_cellpose_segment_cell.py
@Author : ouyangkang
@Date   : 2025.03.04
@Email  : ouyangkang@genomics.cn
@Desc   : utilizing cellpose model to segment cell
@mirror : cellpose_with_GPU
@Version: v1
@Update : 2025.03.13
======================================================
update record：
- 2025.03.13：adding annotation information and modifying error
"""

from cellpose import models, io
import matplotlib.pyplot as plt
import sys


def cell_segment(registered_file, chip_id, model_path):
    """
    utilizing cellpose model cyto3 to segment cell in HE image
    
    Parameters:
        registered_file (str): the absolute pathway of registered HE image
        chip_id (str): the chip id
        model_path (str): the path of cellpose model
        
    Return:
        None: the function without return, but it will save the following files:
            - {chip_id}_cellpose_cp_masks.png : the png image of cell segment mask
            - {chip_id}_cellpose_cp_masks.tif : th tif image of  cell segment mask
            - {input_file_prefix}_seg.npy : the numpy file of cell segment result, input_file_prefix is registered_file prefix
    """
    
    # read registered file
    img = io.imread(registered_file)
    # load pre-trained model
    model = models.CellposeModel(gpu=True, pretrained_model=model_path)
    # run pre-trained model
    masks, flows, styles = model.eval(img, diameter=None, channels=[0,3])
    
    channels = [0,3]
    filenames = registered_file
    io.masks_flows_to_seg(img, masks, flows, filenames, styles, channels)
    io.save_masks(img, masks, flows, f'./{chip_id}_cellpose.tif', png=True, tif=True, channels=[0,3])
    


if __name__ == "__main__":
    input_file = sys.argv[1] # regesited tiff, for example '/data/work/ascites/aligned_picture/Y00722A9_HE_aligned_OYK.tif'
    model_path = sys.argv[2]
    chip_id = sys.argv[3]
    
    cell_segment(registered_file=input_file, chip_id=chip_id, model_path=model_path)