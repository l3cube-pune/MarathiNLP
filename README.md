# L3CubeMahaSent

We present L3CubeMahaSent - the largest publicly available Marathi Sentiment Analysis dataset to date. This dataset is made of marathi tweets which are manually labelled. The annotation guidelines are mentioned in our paper <a href='https://arxiv.org/abs/2103.11408'> link </a>.

## Dataset Statistics

This dataset contains a total of 18,378 tweets which are classified into three classes - Positive(1), Negative(-1) and Neutral(0).
All tweets are present in their original form, without any preprocessing.

Out of these, 15,864 tweets are considered for splitting them into train(tweets-train.csv), test(tweets-test.csv) and validation(tweets-valid.csv) datasets. This has been done to avoid class imbalance in our dataset. <br>
The remaining 2,514 tweets are also provided in a separate sheet(tweets-extra.csv).<br>

The statistics of the dataset are as follows : 

|Split|Total tweets|Tweets per class|
|:--------:|:----:|:----:|
|Train|12114|4038|
|Test|2250|750|
|Validation|1500|500|

The extra sheet contains 2355 positive and 159 negative tweets. These tweets have not been considered during baseline experiments.

## Baseline Experimentations

Two-class(positive,negative) and Three-class(positive,negative,neutral) sentiment analysis / classification was performed on the dataset.

### Models

Some of the models used or performing baseline experiments were:

- CNN, BiLSTM
  - fastText embeddings provided by <a href='https://github.com/AI4Bharat/indicnlp_corpus'> IndicNLP </a> and <a href='https://fasttext.cc/docs/en/crawl-vectors.html'> Facebook </a> are also used along with the above two models. These embeddings are used in two variations: static and trainable.

- BERT based models:
  - Multilingual BERT
  - IndicBERT

### Results

Details of the best performing models are given in the following table:

|Model|3-class|2-class|
|:--------:|:----:|:----:|
|CNN IndicFT trainable|83.24|93.13|
|BiLSTM IndicFT trainable|82.89|91.80|
|IndicBERT|84.13|92.93|

The fine-tuned IndicBERT model is available on huggngface <a href='https://huggingface.co/l3cube-pune/MarathiSentiment'> here </a>.
Further details about the dataset and baseline experiments can be found in this <a href='https://arxiv.org/abs/2103.11408'> paper </a> <a href='https://arxiv.org/pdf/2103.11408.pdf'> pdf </a>.

## License

L3CubeMahaSent is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License</a>.

## Citing

```
@inproceedings{kulkarni2021l3cubemahasent,
  title={L3CubeMahaSent: A Marathi Tweet-based Sentiment Analysis Dataset},
  author={Kulkarni, Atharva and Mandhane, Meet and Likhitkar, Manali and Kshirsagar, Gayatri and Joshi, Raviraj},
  booktitle={Proceedings of the Eleventh Workshop on Computational Approaches to Subjectivity, Sentiment and Social Media Analysis},
  pages={213--220},
  year={2021}
}
```
```
@article{kulkarni2021experimental,
  title={Experimental Evaluation of Deep Learning models for Marathi Text Classification},
  author={Kulkarni, Atharva and Mandhane, Meet and Likhitkar, Manali and Kshirsagar, Gayatri and Jagdale, Jayashree and Joshi, Raviraj},
  journal={arXiv preprint arXiv:2101.04899},
  year={2021}
}
```
