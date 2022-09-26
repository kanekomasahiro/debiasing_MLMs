# debiasing_MLMs

You can use debiasing methods in "[Debiasing isn't enough! -- On the Effectiveness of Debiasing MLMs and their Social Biases in Downstream Tasks (Kaneko et al., COLING2022)](https://arxiv.org/abs/2205.09867)"
You can debias MLMs with Counterfactual Data Augmentation (CDA) debiasing and dropout debiasing as in this repository.
You can also use Alllayer Token-level debiasing in [this repository](https://github.com/kanekomasahiro/context-debias).

# Setup

Use Python version == 3.8.7.
All requirements can be found in requirements.txt. You can install all required packages as follows:
```
pip install -r requirements.txt
```
Moreover, you need git clone of [transformers](https://github.com/huggingface/transformers) library in transformers directory.

# Debiasing MLMs

Create training and development datasets by randomly splitting a raw dataset as follows:
```
python src/preprocess.py --input /your/dataset --output /your/output/directory
```

## CDA

First, reverse gender words in a dataset using the following:
```
python src/cda --input /your/train/dataset --output /your/output/directory
```

Next, debias an MLM using CDA as follows.
```
./cda.sh TRAIN/DATA/PATH DEVELOPMENT/DATA/PATH MODEL/TYPE SEED
```
`MODEL/TYPE` is such as `bert-base-uncased` and `bert-large-uncased`.

## Dropout

Debias an MLM with dropout-debiasing.
```
./dropout.sh TRAIN/DATA/PATH DEVELOPMENT/DATA/PATH MODEL/TYPE SEED
```

