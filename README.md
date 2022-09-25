# debiasing_MLMs

You can use debiasing methods in ``[Debiasing isn't enough! -- On the Effectiveness of Debiasing MLMs and their Social Biases in Downstream Tasks (Kaneko et al., COLING2022)](https://arxiv.org/abs/2205.09867)''
You can debias MLMs with Counterfactual Data Augmentation (CDA) debiasing and dropout debiasing.
You can also use Alllayer Token-level debiasing in [this repository](https://github.com/kanekomasahiro/context-debias).

# Setup

I use Python version == 3.8.7.
All requirements can be found in requirements.txt. You can install all required packages with the following:
```
pip install -r requirements.txt
```

# Debiasing MLMs

You create train and development datasets randomly split from a raw dataset with the following:
```
python src/preprocess.py --input /your/dataset --output /your/output/directory
```

## CDA

First, you need to reverse gender words in a dataset.
```
python src/cda --input /your/train/dataset --output /your/output/directory
```

Next, you debias an MLM with cda.
```
./cda.sh TRAIN/DATA/PATH DEVELOPMENT/DATA/PATH MODEL/TYPE SEED
```
`MODEL/TYPE` is such as `bert-base-uncased` and `bert-large-uncased`.

## Dropout

You debias an MLM with dropout-debiasing.
```
./dropout.sh TRAIN/DATA/PATH DEVELOPMENT/DATA/PATH MODEL/TYPE SEED
```

