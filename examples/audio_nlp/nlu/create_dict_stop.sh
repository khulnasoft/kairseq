#!/bin/bash

### Script handling creation of data binaries
### for model training within kairseq


kairseq_root="."

data_root=$1
train_prefix="${data_root}/train"
valid_prefix="${data_root}/eval"
test_prefix="${data_root}/test"

dest_dir="$data_root/"

#echo "src dict: $src_dict" > "$dest_dir/src_dict.txt"
#echo "trg dict: $tgt_dict" > "$dest_dir/tgt_dict.txt"

    #--tgtdict $tgt_dict \
PYTHONPATH=$kairseq_root \
  python $kairseq_root/kairseq_cli/preprocess.py \
    --source-lang "parse" \
    --trainpref "$train_prefix" \
    --validpref "$valid_prefix" \
    --destdir "$dest_dir" \
    --only-source \
    --dict-only \
    --workers 60;

PYTHONPATH=$kairseq_root \
  python $kairseq_root/kairseq_cli/preprocess.py \
    --source-lang "ltr" \
    --trainpref "$train_prefix" \
    --validpref "$valid_prefix" \
    --destdir "$dest_dir" \
    --only-source \
    --dict-only \
    --workers 60;
