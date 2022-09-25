#!/bin/bash

TRAIN_DATA_PATH=$1
DEV_DATA_DIR=$2
model=$3
seed=$4 

path_to_train_file=${TRAIN_DATA_PATH}
path_to_validation_file=${DEV_DATA_DIR}
MODEL_DIR=dropout_model/${model}

python src/run_mlm_no_trainer.py \
    --model_name_or_path $model \
    --train_file $path_to_train_file \
    --validation_file $path_to_validation_file \
    --num_train_epochs 3 \
    --max_seq_length 128 \
    --per_device_train_batch_size 32 \
    --per_device_eval_batch_size 32 \
    --attention_probs_dropout_prob 0.15 \
    --hidden_dropout_prob 0.20 \
    --seed $seed \
    --output_dir $MODEL_DIR
