# L3Cube-MahaCorpus
L3Cube-MahaCorpus a Marathi monolingual data set scraped from different internet sources. We expand the existing Marathi monolingual corpus with 24.8M sentences and 289M tokens.
We also present, MahaBERT, MahaAlBERT, and MahaRoBerta all BERT-based masked language models, and MahaFT, the fast text word embeddings both trained on full Marathi corpus with 752M tokens. 
The evaluation details are mentioned in our paper <a href='https://arxiv.org/abs/2202.01159'> link </a>
## Dataset Statistics
L3Cube-MahaCorpus(full) = L3Cube-MahaCorpus(news) + L3Cube-MahaCorpus(non-news)

Full Marathi Corpus incorporates all existing <a href='https://github.com/AI4Bharat/indicnlp_corpus'> sources </a>.
|Dataset|#tokens(M)|#sentences(M)|Link|
|:--------:|:----:|:----:|:----:|
|L3Cube-MahaCorpus(news)|212|17.6|<a href='https://drive.google.com/file/d/1gLI38-YdvapattwxC3z46Fgzif7j8_Ji/view?usp=sharing'> link </a>|
|L3Cube-MahaCorpus(non-news)|76.4|7.2|<a href='https://drive.google.com/file/d/1KHHJByCFwJxMJaGkO3FjIQbkLbc7rHAQ/view?usp=sharing'> link </a>|
|L3Cube-MahaCorpus(full)|289|24.8|<a href='https://drive.google.com/file/d/1sHIIq7C-WA6nSQaoVr4uL6pas8MVNmAr/view?usp=sharing'> link </a>|
|Full Marathi Corpus(all sources)|752|57.2|<a href='https://drive.google.com/file/d/1UjZ-X2S77AQyCkHqw2mFXRWYf9WOZS0m/view?usp=sharing'> link </a>|

## Marathi BERT models and Marathi Fast Text model
The full Marathi Corpus is used to train BERT language models and made available on HuggingFace model hub.
|Model|Description|Link|
|:--------:|:----:|:----:|
|MahaBERT|Base-BERT|<a href='https://huggingface.co/l3cube-pune/marathi-bert'> link </a>|
|MahaRoBERTa|RoBERTa|<a href='https://huggingface.co/l3cube-pune/marathi-roberta'> link </a>|
|MahaAlBERT|AlBERT|<a href='https://huggingface.co/l3cube-pune/marathi-albert'> v1 </a> <a href='https://huggingface.co/l3cube-pune/marathi-albert-v2'> v2 </a>|
|MahaGPT|GPT2|<a href='https://huggingface.co/l3cube-pune/marathi-gpt'> link </a>|
|MahaFT|Fast Text|<a href='https://drive.google.com/file/d/1xuQPMUIFvjgQranChgJ3alHXMJVeCVz0/view?usp=sharing'> bin </a> <a href='https://drive.google.com/file/d/1-2rCOsgxKgTigonta4FvA4WBWIaXVX73/view?usp=sharing'> vec </a>|

# L3Cube-MahaHate

L3Cube-MahaHate is the largest publicly available Marathi Hate Speech Detection dataset to date. This dataset is made of marathi tweets which are manually labelled. The annotation guidelines are mentioned in our paper <a href='https://arxiv.org/abs/2203.13778'> link </a>.
The dataset is present in folder L3Cube-MahaHate/

## Dataset Statistics

The dataset is released in 4-class and 2-class form. The 4-class dataset (with labels hate, offensive, pofane, and not) has total of 25000 samples with 21500 train samples, 2000 test samples, and 1500 validation samples. The 2-class dataset (with labels hate and not) has a total of 37500 samples.

The fine-tuned MahaBERT model is available on huggingface <a href='https://huggingface.co/l3cube-pune/mahahate-multi-roberta'> 4-class </a> and <a href='https://huggingface.co/l3cube-pune/mahahate-bert'> 2-class </a>. The benchmark results are described in our paper <a href='https://arxiv.org/pdf/2203.13778.pdf'> pdf </a>

# L3CubeMahaSent

L3CubeMahaSent is the largest publicly available Marathi Sentiment Analysis dataset to date. This dataset is made of marathi tweets which are manually labelled. The annotation guidelines are mentioned in our paper <a href='https://arxiv.org/abs/2103.11408'> link </a>.

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

The fine-tuned IndicBERT model is available on huggingface <a href='https://huggingface.co/l3cube-pune/MarathiSentiment'> here </a>.
Further details about the dataset and baseline experiments can be found in this <a href='https://arxiv.org/abs/2103.11408'> paper </a> <a href='https://arxiv.org/pdf/2103.11408.pdf'> pdf </a>.

## License

L3Cube-MahaCorpus, L3Cube-MahaHate and L3CubeMahaSent is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License</a>.

## Citing
```
@article{joshi2022l3cube,
  title={L3Cube-MahaCorpus and MahaBERT: Marathi Monolingual Corpus, Marathi BERT Language Models, and Resources},
  author={Joshi, Raviraj},
  journal={arXiv preprint arXiv:2202.01159},
  year={2022}
}
```

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
@inproceedings{kulkarni2022experimental,
  title={Experimental evaluation of deep learning models for marathi text classification},
  author={Kulkarni, Atharva and Mandhane, Meet and Likhitkar, Manali and Kshirsagar, Gayatri and Jagdale, Jayashree and Joshi, Raviraj},
  booktitle={Proceedings of the 2nd International Conference on Recent Trends in Machine Learning, IoT, Smart Cities and Applications},
  pages={605--613},
  year={2022},
  organization={Springer}
}
```

This project is co-ordinated and mentored by <a href='https://www.linkedin.com/in/ravirajoshi/'> Raviraj Joshi </a> under L3Cube Pune. For any queries contact ravirajoshi@gmail.com .
