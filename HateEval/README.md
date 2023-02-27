# L3Cube-HateEval-Mr and HateEval-Hi: Gold datasets for hate speech detection in Marathi and Hindi

HateEval contains two datasets created for the evaluation of hate speech detection models in Marathi and Hindi. 
HateEval-Mr.csv contains 2004 tweets in Marathi, while HateEval-Hi.csv contains 2008 tweets in Hindi. 
The tweets in are manually annotated and labeled as hateful (1) and none (0). The definition of hateful can be found in our <a href='https://arxiv.org/abs/2203.13778'> MahaHate </a> paper.

Note: The tweets in the HateEval-Mr evaluation set do not overlap with the MahaHate dataset and have completely different tweets. 
The tweets contained in HateEval datasets are randomly sampled subsets of much larger corpora of tweets. 
The larger corpora have been used for training large language models. Further details on our work, evaluation datasets, and baseline numbers are presented in this <a href="https://arxiv.org/abs/2210.04267"> paper </a>.

As described in our paper the dataset was mainly created for evaluation purposes however it can also be used for training/validation as these are gold-standard datasets with 2k samples each. 

# Citing
If you use our datasets or other findings from the paper, please consider citing our work:
```
@inproceedings{gokhalespread,
  title={Spread Love Not Hate: Undermining the Importance of Hateful Pre-training for Hate Speech Detection},
  author={Gokhale, Omkar Bhushan and Kane, Aditya and Patankar, Shantanu and Chavan, Tanmay and Joshi, Raviraj Bhuminand},
  booktitle={I Can't Believe It's Not Better Workshop: Understanding Deep Learning Through Empirical Falsification}
}
```
