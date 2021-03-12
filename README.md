# L3CubeMahaSent

We present L3CubeMahaSent - the largest publicly available Marathi Sentiment Analysis dataset to date.This dataset is made of marathi tweets which are manually labelled. The annotation guidelines are mentioned in our paper. (link)

## Dataset Statistics

This dataset contains a total of 18,378 tweets which are classified into three classes - Positive(1), Negative(-1) and Neutral(0).

Out of these, 15,864 tweets are considered for splitting them into train(tweets-train.csv), test(tweets-test.csv) and validation(tweets-valid.csv) datasets. This has been done to avoid class imbalance in our dataset. <br>
The remaining 2,514 tweets are also provided in a separate sheet(tweets-extra.csv). The statistics of the dataset is as follows : 

|Split|Total tweets|Tweets per class|
|:--------:|:----:|:----:|
|Train|12114|4038|
|Test|2250|750|
|Validation|1500|500|


The extra sheet contains 2355 positive and 159 negative tweets.

## Baseline Experimentations

For conducting baseline experiments on our dataset, hashtags, mentions and special symbols were removed as a part of preprocessing.

The accuracies for Two-class(positive,negative) and Three-class(positive,negative,neutral) for some good-performing models are as follows :

As a part of baseline experiments, following models were used:

- CNN
- BiLSTM

fastText embeddings provided by IndicNLP (link) and Facebook (link) were also used along with the above two models. These embeddings are used in two variations: static and trainable.

- ULMFiT pretrained by iNLTK (link)
- BERT based models:
  - Multilingual BERT (link)
  - IndicBERT (link)

Details of the best performing models are given in the following table:

|Model|3-class|2-class|
|:--------:|:----:|:----:|
|CNN IndicFT trainable|83.24|93.13|
|BiLSTM IndicFT trainable|82.89|91.80|
|IndicBERT|84.13|92.93|


Further details can be found in this paper. (link)
