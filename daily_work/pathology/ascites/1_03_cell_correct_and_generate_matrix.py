"""
======================================================
@File   : 03_cell_correct_and_generate_matrix.py
@Author : ouyangkang
@Date   : 2025.03.04
@Email  : ouyangkang@genomics.cn
@Desc   : generate single cell matrix based on the cell segment result of cellpose modle
@mirror : stereopy-1.4.0
@Version: v1
@Update : 2025.03.18
======================================================
update record：
- 2025.03.18：adding annotation information and modifying error
"""

import stereo as st
from stereo.tools.cell_correct import cell_correct
from stereo.tools.cell_cut import CellCut
import gzip
import sys


def gem_file_check(gem_path, chip_id):
    """
    check if the values of gem file offset X and Y are 0.
    
    Parameters:
        gem_path (str): the absolute pathway of gem file
        chip_id (str): the chip id
        
    Return:
        modified_status (bool): True if gem file is modified. the function will save following file
            - {chip_id}_modified.gem.gz : offset X and Y are changed to 0
    """
    
    # check input data format
    if not isinstance(gem_path, str):
        raise TypeError("gem_path must be a string.")
    if not isinstance(chip_id, str):
        raise TypeError("chip_id must be a string.")
    
    
    # 
    with gzip.open(gem_path, 'rt', encoding='utf-8') as file:
        lines = [next(file) for _ in range(8)]
        rest_of_info = file.read() 
        
        print(lines)
        
    modified_status = False 
    if lines[-1].startswith("#OffsetY=") and lines[-1] != "#OffsetY=0\n":
        lines[-1] = "#OffsetY=0\n"
        modified_status = True
    if lines[-2].startswith("#OffsetX=") and lines[-2] != "#OffsetX=0\n":
        lines[-2] = "#OffsetX=0\n"
        modified_status = True
    
    if modified_status:
        print(f'gem.gz file has been modified: {modified_status}')

        with gzip.open(f'./{chip_id}_modified.gem.gz', 'wt', encoding='utf-8') as file:
            file.writelines(lines)
            file.writelines(rest_of_info)
    
    return modified_status

                
def cellcut(gem_path, mask_path, chip_id, modified_status):
    """
    generating a new cell bin gem based on it and the corresponding mask.
    
    Parameters:
        gem_path (str): the absolute pathway of gem file
        mask_path (str): the result of cell segmentation
        chip_id (str): the chip id
        modified_status (bool): check the modified status of gem file
        
    Return:
        None: the function without return, but it will save the following files:
            - if modified_status: True
                - {chip_id}_modified.gem.cellbin.gef : gef file after cell segmentation
                - {chip_id}_modified.gem.bgef : bgef file after cell segmentation
            - if modified_status: False
                - {chip_id}.gem.cellbin.gef : gef file after cell segmentation
                - {chip_id}.gem.bgef : bgef file after cell segmentation
    """
    cgef_out_dir = "./"
    cc = CellCut(cgef_out_dir=cgef_out_dir)
    if modified_status:
        modified_gem_path = f'./{chip_id}_modified.gem.gz'
        out_path = cc.cell_cut(gem_path=modified_gem_path, mask_path=mask_path)
    else:
        out_path = cc.cell_cut(gem_path=gem_path, mask_path=mask_path)

def cellcorrect(gem_path, mask_path, chip_id, modified_status):
    """
    performing cell correction
    
    Parameters:
        gem_path (str): the absolute pathway of gem file
        mask_path (str): the result of cell segmentation
        chip_id (str): the chip id
        modified_status (bool): check the modified status of gem file
        
    Return:
        None: the function without return, but it will save the following files:
            - if modified_status: True
                - {chip_id}_modified.bgef : bgef file after cell correct
                - {chip_id}_modified.adjusted.cellbin.gef : gef file after cell correct
                - {chip_id}_cellpose_cp_masks_edm_dis_10.tif : mask image after cell correct
            - if modified_status: False
                - {chip_id}.bgef : bgef file after cell correct
                - {chip_id}.adjusted.cellbin.gef : gef file after cell correct
                - {chip_id}_cellpose_cp_masks_edm_dis_10.tif : mask image after cell correct
    """
    out_dir = "./"
    if modified_status:
        modified_gem_path = f'./{chip_id}_modified.gem.gz'
        data = cell_correct(out_dir=out_dir, gem_path=modified_gem_path, mask_path=mask_path, only_save_result=False, fast='EDM', process_count=10)
    else:
        data = cell_correct(out_dir=out_dir, gem_path=gem_path, mask_path=mask_path, only_save_result=False, fast='EDM', process_count=10)
    

def gef2matrix(chip_id, modified_status):
    """
    generating a h5ad file based on cell correct result.
    
    Parameters:
        chip_id (str): the chip id
        
    Return:
        None: the function without return, but it will save the following files:
            - {chip_id}_cellpose.h5ad
    """
    if modified_status:
        data = st.io.read_gef(f'./{chip_id}_modified.adjusted.cellbin.gef', bin_type='cell_bins')
        st.io.stereo_to_anndata(data, flavor='scanpy',output=f'./{chip_id}_cellpose.h5ad')
    else:
        data = st.io.read_gef(f'./{chip_id}.adjusted.cellbin.gef', bin_type='cell_bins')
        st.io.stereo_to_anndata(data, flavor='scanpy',output=f'./{chip_id}_cellpose.h5ad')
    
    
if __name__ == "__main__":
    # like Y00722CC.gem.gz
    gem_path = sys.argv[1]
    # like Y00722CC
    chip_id = sys.argv[2]
    # the mask file is after cell segmentation
    mask_path = sys.argv[3]
    
    print('gem file check---------started')
    modified_status = gem_file_check(gem_path, chip_id)
    print('gem file check---------finished')
    
    print('cellcut---------started')
    cellcut(gem_path, mask_path, chip_id, modified_status)
    print('cellcut---------finished')
    
    print('cellcorrect----------started')
    cellcorrect(gem_path, mask_path, chip_id, modified_status)
    print('cellcorrect----------finished')
    
    print('generate singlecell matrix-------------started')
    gef2matrix(chip_id, modified_status)
    print('generate singlecell matrix-------------finished')