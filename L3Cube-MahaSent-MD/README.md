# L3Cube-MahaSent-MD

L3Cube-MahaSent-MD is the largest publicly available multi-domain Marathi Sentiment Analysis dataset to date. 
This is a manually annotated dataset consisting of domains like Movie Reviews, Subtitles, General Tweets, and Politial Tweets. The annotation guidelines and baseline results are mentioned in our paper <a href='https://arxiv.org/abs/2306.13888'> arxiv </a>.

## Dataset Statistics

This dataset contains a total of 60k sentences which are classified into three classes - Positive(1), Negative(-1) and Neutral(0).

The statistics of the dataset, path, and models are listed below : 

|Dataset|Domain|Samples (train, test, valid)|Data|Model|
|:--------:|:----:|:----:|:----:|:----:|
|MahaSent-MR|Marathi Movie Reviews|12k + 1.5k + 1.5k = 15k|<a href='https://github.com/l3cube-pune/MarathiNLP/tree/main/L3Cube-MahaSent-MD/MahaSent_MR'>Data</a>|<a href='https://huggingface.co/l3cube-pune/marathi-sentiment-movie-reviews'>Model</a>|
|MahaSent-ST|Marathi Subtitles|12k + 1.5k + 1.5k = 15k|<a href='https://github.com/l3cube-pune/MarathiNLP/tree/main/L3Cube-MahaSent-MD/MahaSent_ST'>Data</a>|<a href='https://huggingface.co/l3cube-pune/marathi-sentiment-subtitles'>Model</a>|
|MahaSent-GT|Marathi Generic Tweets|12k + 1.5k + 1.5k = 15k|<a href='https://github.com/l3cube-pune/MarathiNLP/tree/main/L3Cube-MahaSent-MD/MahaSent_GT'>Data</a>|<a href='https://huggingface.co/l3cube-pune/marathi-sentiment-tweets'>Model</a>|
|MahaSent-PT|Marathi Political Tweets|12k + 1.5k + 1.5k = 15k|<a href='https://github.com/l3cube-pune/MarathiNLP/tree/main/L3Cube-MahaSent-MD/MahaSent_PT'>Data</a>|<a href='https://huggingface.co/l3cube-pune/marathi-sentiment-political-tweets'>Model</a>|
|MahaSent-All|All of the above|48k + 6k + 6k = 60k|<a href='https://github.com/l3cube-pune/MarathiNLP/tree/main/L3Cube-MahaSent-MD/MahaSent_All'>Data</a>|<a href='https://huggingface.co/l3cube-pune/marathi-sentiment-md'>Model</a>|


### Citing
```
@article{pingle2023l3cube,
  title={L3Cube-MahaSent-MD: A Multi-domain Marathi Sentiment Analysis Dataset and Transformer Models},
  author={Pingle, Aabha and Vyawahare, Aditya and Joshi, Isha and Tangsali, Rahul and Joshi, Raviraj},
  journal={arXiv preprint arXiv:2306.13888},
  year={2023}
}
```
