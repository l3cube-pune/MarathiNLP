# L3CubeMahaSent

We present L3CubeMahaSent - the largest publicly available Marathi Sentiment Analysis dataset to date.This dataset is gathered using Twitter.
This dataset contains total 18378 tweets which are classified into three classes - positive(1), negative(-1) and neutral(0).
Out of these 15864 tweets are considered for splitting them into train, test and validation datasets.
The remaining 2514 tweets are also provided in a separate sheet.The statistics of train , test and validation dataset are as follows : 
1)Train-(Total : 12114) : It contains 4038 positive,negative,neutral tweets each.
2)Test-(Total : 2250) : It contains 750 positive,negative,neutral tweets each.
3)Validation-(Total : 1500) : It contains 500 positive,negative,neutral tweets each.
For conducting baseline experiments on our dataset, hashtags, mentions and special symbols were removed while preprocessing.
The accuracies for Two-class(positive,negative) and Three-class(positive,negative,neutral) for some good-performing models are as follows :-
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
