# L3CubeMahaSent

We present L3CubeMahaSent - the largest publicly available Marathi Sentiment Analysis dataset to date.This dataset is made of marathi tweets which are manually labelled. The annotation guidelines are mentioned in our paper. (link)

## Dataset Statistics

This dataset contains total 18,378 tweets which are classified into three classes - Positive(1), Negative(-1) and Neutral(0).

Out of these 15,864 tweets are considered for splitting them into train(tweets-train.csv), test(tweets-test.csv) and validation(tweets-valid.csv) datasets. We have done this to avoid class imbalance in our dataset. <br>
The remaining 2,514 tweets are also provided in a separate sheet(tweets-extra.csv). The statistics of the dataset is as follows : 

|Split|Total tweets|Tweets per class|
|:--------:|:----:|:----:|
|Train|12114|4038|
|Test|2250|750|
|Validation|1500|500|


The extra sheet contains 2355 positive and 159 negative tweets.<br>

For conducting baseline experiments on our dataset, hashtags, mentions and special symbols were removed while preprocessing.

The accuracies for Two-class(positive,negative) and Three-class(positive,negative,neutral) for some good-performing models are as follows :

1) BERT - IndicBERT(INLP) : 
- two-class accuracy -- 84.13
- three-class accuracy -- 92.93
2) CNN - IndicNLP FastText (trainable) :
- two-class accuracy -- 83.24
- three-class accuracy -- 93.13
3) CNN - IndicNLP FastText (static) :
- two-class accuracy -- 83.00
- three-class accuracy -- 92.47
4) BiLSTM - IndicNLP FastText (trainable) :
- two-class accuracy -- 82.89
- three-class accuracy -- 91.80
5) BiLSTM - IndicNLP FastText (static) :
- two-class accuracy -- 82.41
- three-class accuracy -- 92.67

Further details can be found in this paper. (link)
