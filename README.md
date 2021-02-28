# L3CubeMahaSent

We present L3CubeMahaSent - the largest publicly available Marathi Sentiment Analysis dataset to date.This dataset is gathered using Twitter.<br>
This dataset contains total 18378 tweets which are classified into three classes - positive(1), negative(-1) and neutral(0).<br>
Out of these 15864 tweets are considered for splitting them into train(tweets-train.csv), test(tweets-test.csv) and validation(tweets-valid.csv) datasets.<br>
The remaining 2514 tweets are also provided in a separate sheet(tweets-extra.csv). The statistics of the dataset is as follows : <br>
1)Train-(Total : 12114 tweets) : It contains 4038 positive,negative,neutral tweets each.<br>
2)Test-(Total : 2250 tweets) : It contains 750 positive,negative,neutral tweets each.<br>
3)Validation-(Total : 1500 tweets) : It contains 500 positive,negative,neutral tweets each.<br>
4)Extra-(Total : 2514 tweets) : It contains 2355 positive and 159 negative tweets.<br>
For conducting baseline experiments on our dataset, hashtags, mentions and special symbols were removed while preprocessing.<br>
The accuracies for Two-class(positive,negative) and Three-class(positive,negative,neutral) for some good-performing models are as follows :-<br>

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
