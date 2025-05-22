#!bin/bash

matrix_file=$1

python -u /data/work/ascites/code/02_data_analysis/SequencingCancerFinder-master/infer.py \
	--ckp='/data/work/ascites/code/02_data_analysis/cancer-finder_model/model_epoch92.pkl' \
	--matrix=$matrix_file \
	--out='output.csv' \
	--threshold=0.5
