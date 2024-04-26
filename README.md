# L3Cube-MahaNLP
Despite being the third most popular language in India, the Marathi language lacks useful NLP resources. With <a href='https://arxiv.org/abs/2205.14728'> L3Cube-MahaNLP</a>, we aim to build resources and a library for Marathi natural language processing. We have contributed un-supervised, supervised datasets, and Transformer models for Marathi. The supervised datasets include Marathi sentiment analysis, named entity recognition, and hate speech detection. With this, we at L3Cube-Pune aim to bring Marathi to the forefront of IndicNLP. Our vision is to make Marathi a resource-rich language and promote AI for Maharashtra!

[Update] The library is now available in a python package:
```
pip install mahaNLP
```
Usage examples are provided in this demo <a href='https://colab.research.google.com/drive/1POx3Bi1cML6-s3Z3u8g8VpqzpoYCyv2q'> Colab </a>.

[Update] We have released a new code-mixed Marathi-English unsupervised dataset MeCorpus and supervised datasets like MeSent, MeHate, and MeLID. <br>
[Update] We have released a new multi-domain Sentiment analysis dataset MahaSent-MD with 60k samples across four diverse domains. A new sentiment analysis <a href='https://huggingface.co/l3cube-pune/marathi-sentiment-md'>model</a> is also released on HF.

## L3Cube-MahaCorpus and Marathi BERT
L3Cube-MahaCorpus is a Marathi monolingual data set scraped from different internet sources. We expand the existing Marathi monolingual corpus with 24.8M sentences and 289M tokens.
We also present, MahaBERT, MahaAlBERT, and MahaRoBerta all BERT-based masked language models, and MahaFT, the fast text word embeddings both trained on full Marathi corpus with 752M tokens. 
The evaluation details are mentioned in our paper <a href='https://arxiv.org/abs/2202.01159'> link </a>
## Dataset Statistics
L3Cube-MahaCorpus(full) = L3Cube-MahaCorpus(news) + L3Cube-MahaCorpus(non-news)

Full Marathi Corpus incorporates all existing <a href='https://github.com/AI4Bharat/indicnlp_corpus'> sources </a>.
|Dataset|#tokens(M)|#sentences(M)|Link|
|:--------:|:----:|:----:|:----:|
|L3Cube-MahaCorpus (news)|212|17.6|<a href='https://drive.google.com/file/d/1gLI38-YdvapattwxC3z46Fgzif7j8_Ji/view?usp=sharing'> link </a>|
|L3Cube-MahaCorpus (non-news)|76.4|7.2|<a href='https://drive.google.com/file/d/1KHHJByCFwJxMJaGkO3FjIQbkLbc7rHAQ/view?usp=sharing'> link </a>|
|L3Cube-MahaCorpus (full)|289|24.8|<a href='https://drive.google.com/file/d/1sHIIq7C-WA6nSQaoVr4uL6pas8MVNmAr/view?usp=sharing'> link </a>|
|Full Marathi Corpus (all sources)|752|57.2|<a href='https://drive.google.com/file/d/1UjZ-X2S77AQyCkHqw2mFXRWYf9WOZS0m/view?usp=sharing'> link </a>|

## L3Cube-MeCorpus and code-mixed MeBERT
L3Cube-MeCorpus is a first-of-its-kind large code-mixed Marathi-English (Mr-En) corpus with 10 million social media sentences released in <a href='https://arxiv.org/abs/2306.14030'> paper </a>.

|Dataset|#tokens(M)|#sentences(M)|Link|
|:--------:|:----:|:----:|:----:|
|L3Cube-MeCorpus (Roman)|70.9|5|<a href='https://drive.google.com/file/d/1yyoANEBbj6keb0zfcXTpKmw0bueKy_fa/view?usp=sharing'> link </a>|
|L3Cube-MeCorpus (Devanagari)|68.6|5|<a href='https://drive.google.com/file/d/1WNVXj6KZ0_kgr-wYb5CBUbaL4dlM3QVa/view?usp=sharing'> link </a>|
|L3Cube-MeCorpus (Roman + Devanagari)|139.5|10|<a href='https://drive.google.com/file/d/1fvDEVlb1SCaxqUl3Xu5LYzAJWLzHeLy0/view?usp=sharing'> link </a>|

### Marathi BERT models and Marathi Fast Text model
The full Marathi Corpus is used to train BERT language models and made available on Hugging Face model hub.
|Model|Description|Link|
|:--------:|:----:|:----:|
|MahaGemma-7B|Gemma-7B|<a href='https://huggingface.co/l3cube-pune/marathi-gpt-gemma-7b'> v1 </a>|
|MahaGemma-2B|Gemma-2B|<a href='https://huggingface.co/l3cube-pune/marathi-gpt-gemma-2b'> v1 </a>|
|MahaBERT|Base-BERT|<a href='https://huggingface.co/l3cube-pune/marathi-bert'> v1 </a>, <a href='https://huggingface.co/l3cube-pune/marathi-bert-v2'> v2 </a>, <a href='https://arxiv.org/abs/2202.01159'> paper </a>|
|MahaRoBERTa|RoBERTa|<a href='https://huggingface.co/l3cube-pune/marathi-roberta'> link </a>|
|MahaAlBERT|AlBERT|<a href='https://huggingface.co/l3cube-pune/marathi-albert'> v1 </a>, <a href='https://huggingface.co/l3cube-pune/marathi-albert-v2'> v2 </a>|
|MahaGPT|GPT2|<a href='https://huggingface.co/l3cube-pune/marathi-gpt'> link </a>|
|MahaFT|Fast Text|<a href='https://drive.google.com/file/d/1xuQPMUIFvjgQranChgJ3alHXMJVeCVz0/view?usp=sharing'> bin </a>, <a href='https://drive.google.com/file/d/1-2rCOsgxKgTigonta4FvA4WBWIaXVX73/view?usp=sharing'> vec </a>|
|MahaTweetBERT|MahaBERT + Tweets|<a href='https://huggingface.co/l3cube-pune/marathi-tweets-bert'> model </a>, <a href='https://arxiv.org/abs/2210.04267'> paper </a>|
|MahaSBERT|Sentence-BERT|<a href='https://huggingface.co/l3cube-pune/marathi-sentence-similarity-sbert'> MahaSBERT-STS </a>, <a href='https://huggingface.co/l3cube-pune/marathi-sentence-bert-nli'> MahaSBERT </a> , <a href='https://arxiv.org/abs/2211.11187'> paper </a>|
|IndicSBERT|Sentence-BERT (for cross-language) |<a href='https://huggingface.co/l3cube-pune/indic-sentence-similarity-sbert'> IndicSBERT-STS </a>, <a href='https://huggingface.co/l3cube-pune/indic-sentence-bert-nli'> IndicSBERT  </a> , <a href='https://arxiv.org/abs/2304.11434'> paper </a>|
|MeBERT|Codemixed Marathi-English BERT (Roman) |<a href='https://huggingface.co/l3cube-pune/me-bert'> me-bert </a>, <a href='https://arxiv.org/abs/2306.14030'> paper </a>|
|MeRoBERTa|Codemixed Marathi-English RoBERTa (Roman) |<a href='https://huggingface.co/l3cube-pune/me-roberta'> me-roberta </a>, <a href='https://arxiv.org/abs/2306.14030'> paper </a>|
|MeBERT-Mixed|Codemixed Marathi-English BERT (Roman + Devanagari) |<a href='https://huggingface.co/l3cube-pune/me-bert-mixed'> me-bert-mixed </a>, <a href='https://huggingface.co/l3cube-pune/me-bert-mixed-v2'> me-bert-mixed-v2 </a>, <a href='https://arxiv.org/abs/2306.14030'> paper </a>|
|MeRoBERTa-Mixed|Codemixed Marathi-English RoBERTa (Roman + Devanagari) |<a href='https://huggingface.co/l3cube-pune/me-roberta-mixed'> me-roberta-mixed </a>, <a href='https://arxiv.org/abs/2306.14030'> paper </a>|

### Supervised Datasets

|Dataset|Description|Samples(train, valid, test)|link|model|paper|
|:--------:|:----:|:----:|:----:|:----:|:----:|
MahaSQuAD|Marathi Question Answering Dataset|142k (118516, 11873, 11803)|<a href='https://github.com/l3cube-pune/MarathiNLP/tree/main/L3Cube-MahaSQuAD'> data </a>|<a href='https://huggingface.co/l3cube-pune/marathi-question-answering-squad-bert'> MahaSQuAD-BERT </a>|<a href=''> link </a>|
MahaNER|Marathi Named Entity Recognition dataset with 8 entity classes|25k (21.5k, 1.5k, 2k)|<a href='https://github.com/l3cube-pune/MarathiNLP/tree/main/L3Cube-MahaNER'> data </a>|<a href='https://huggingface.co/l3cube-pune/marathi-ner'> MahaNER-BERT </a>|<a href='https://arxiv.org/abs/2204.06029'> link </a>|
MahaSocialNER|Social media based Marathi Named Entity Recognition dataset with 8 entity classes|18k (12k, 1.5k, 2.2k)|<a href='https://github.com/l3cube-pune/MarathiNLP/tree/main/L3Cube-MahaSocialNER'> data </a>|<a href='https://huggingface.co/l3cube-pune/marathi-social-ner'> MahaSocialNER-BERT </a>|<a href='http://arxiv.org/abs/2401.00170'> link </a>|
MahaHate|Marathi Hate Speech Detection dataset with 4 class (hate, offensive, pofane, and not) and 2 class (hate and not) labels|4-class: 25k (21.5k, 1.5k, 2k), 2-class:  37500|<a href='https://github.com/l3cube-pune/MarathiNLP/tree/main/L3Cube-MahaHate'> data </a>|<a href='https://huggingface.co/l3cube-pune/mahahate-multi-roberta'> 4-class </a> , <a href='https://huggingface.co/l3cube-pune/mahahate-bert'> 2-class </a>|<a href='https://arxiv.org/abs/2203.13778'> link </a>|
MahaSent|Marathi Sentiment Analysis dataset with three classes - Positive(1), Negative(-1) and Neutral(0)|18,378 (12114, 1500, 2250); extra(2,514=2355(+1) + 159(-1))|<a href='https://github.com/l3cube-pune/MarathiNLP/tree/main/L3CubeMahaSent%20Dataset'> data </a>|<a href='https://huggingface.co/l3cube-pune/MarathiSentiment'> MarathiSentiment </a>|<a href='https://arxiv.org/abs/2103.11408'> link </a>|
HateEval-Mr|Another dataset for evaluation of Hate Speech models with two classes - Hate(1) and None(0)|2k samples|<a href='https://github.com/l3cube-pune/MarathiNLP/tree/main/HateEval'> data| |<a href='https://arxiv.org/abs/2210.04267'> link </a>|
MahaSent-MD|A Multi-domain Marathi Sentiment Analysis dataset (4 domains - Marathi Movie Reviews, TV Subtitles, Generic Tweets, and Political Tweets) with three classes - Positive(1), Negative(-1) and Neutral(0)|60k samples|<a href='https://github.com/l3cube-pune/MarathiNLP/tree/main/L3Cube-MahaSent-MD/'> data| <a href='https://huggingface.co/l3cube-pune/marathi-sentiment-md'>MahaSent-MD</a> |<a href='https://arxiv.org/abs/2306.13888'> link </a>|
MeSent|A code-mixed Marathi-English Sentiment Analysis dataset with three classes - Positive(1), Negative(-1) and Neutral(0)|12k samples|<a href='https://github.com/l3cube-pune/MarathiNLP/tree/main/MeEval/L3Cube-MeSent'> data| <a href='https://huggingface.co/l3cube-pune/me-sent-roberta'>me-sent-roberta</a> |<a href='https://arxiv.org/abs/2306.14030'> link </a>|
MeHate|A code-mixed Marathi-English Hate speech identification dataset with two classes - Hate(1) and None(0)|2768 samples|<a href='https://github.com/l3cube-pune/MarathiNLP/tree/main/MeEval/L3Cube-MeHate'> data| <a href='https://huggingface.co/l3cube-pune/me-hate-bert'>me-hate-bert</a> |<a href='https://arxiv.org/abs/2306.14030'> link </a>|
MeLID|A code-mixed Marathi-English language identification (LID) dataset with three classes - Marathi, English, and Undefined|12k samples|<a href='https://github.com/l3cube-pune/MarathiNLP/tree/main/MeEval/L3Cube-MeLID'> data| <a href='https://huggingface.co/l3cube-pune/me-lid-bert'>me-lid-bert</a> |<a href='https://arxiv.org/abs/2306.14030'> link </a>|

## License

L3Cube-MahaCorpus, L3Cube-MahaNER, L3Cube-MahaHate, L3Cube-HateEval-Mr, L3Cube-MahaSent-MD, L3CubeMahaSent, L3Cube-MeCorpus, L3Cube-MahaSent-MD, L3Cube-MeSent, L3Cube-MeHate, and L3Cube-MeLID are licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License</a>. The datasets are released to the community for research purposes only and the group is not responsible for any misuse of these datasets.

## Citing
```
@article{joshi2022l3cube,
  title={L3Cube-MahaNLP: Marathi Natural Language Processing Datasets, Models, and Library},
  author={Joshi, Raviraj},
  journal={arXiv preprint arXiv:2205.14728},
  year={2022}
}
```
```
@inproceedings{joshi-2022-l3cube,
    title = "L3Cube-MahaCorpus and MahaBERT: Marathi Monolingual Corpus, Marathi BERT Language Models, and Resources",
    author = "Joshi, Raviraj",
    booktitle = "Proceedings of the WILDRE-6 Workshop within the 13th Language Resources and Evaluation Conference",
    month = jun,
    year = "2022",
    address = "Marseille, France",
    publisher = "European Language Resources Association",
    url = "https://aclanthology.org/2022.wildre-1.17",
    pages = "97--101",
}
```

## Publications

```
Joshi, Raviraj. "L3Cube-MahaCorpus and MahaBERT: Marathi Monolingual Corpus, Marathi BERT Language Models, and Resources." LREC 2022 Workshop Language Resources and Evaluation Conference 20-25 June 2022. 2022.

Chavan, Tanmay, et al. "My Boli: Code-mixed Marathi-English Corpora, Pretrained Language Models and Evaluation Benchmarks." arXiv preprint arXiv:2306.14030 (2023).

Pingle, Aabha, et al. "L3Cube-MahaSent-MD: A Multi-domain Marathi Sentiment Analysis Dataset and Transformer Models." arXiv preprint arXiv:2306.13888 (2023).

Pingle, Aabha, et al. "Robust Sentiment Analysis for Low Resource languages Using Data Augmentation Approaches: A Case Study in Marathi." arXiv preprint arXiv:2310.00734 (2023).

Deode, Samruddhi, et al. "L3Cube-IndicSBERT: A simple approach for learning cross-lingual sentence representations using multilingual BERT." arXiv preprint arXiv:2304.11434 (2023).

Joshi, Ananya, et al. "L3Cube-MahaSBERT and HindSBERT: Sentence BERT Models and Benchmarking BERT Sentence Representations for Hindi and Marathi." arXiv preprint arXiv:2211.11187 (2022).

Gokhale, Omkar Bhushan, et al. "Spread Love Not Hate: Undermining the Importance of Hateful Pre-training for Hate Speech Detection." I Can't Believe It's Not Better Workshop: Understanding Deep Learning Through Empirical Falsification.

Sabane, Maithili, et al. "Enhancing Low Resource NER using Assisting Language and Transfer Learning." 2023 2nd International Conference on Applied Artificial Intelligence and Computing (ICAAIC). IEEE, 2023.

Litake, Onkar, et al. "L3Cube-MahaNER: A Marathi Named Entity Recognition Dataset and BERT models." Proceedings of the WILDRE-6 Workshop within the 13th Language Resources and Evaluation Conference. 2022.

Litake, Onkar, et al. "Mono vs Multilingual BERT: A Case Study in Hindi and Marathi Named Entity Recognition." arXiv preprint arXiv:2203.12907 (2022).

Velankar, Abhishek, Hrushikesh Patil, and Raviraj Joshi. "Mono vs multilingual bert for hate speech detection and text classification: A case study in marathi." IAPR Workshop on Artificial Neural Networks in Pattern Recognition. Springer, Cham, 2023.

Patil, Hrushikesh, Abhishek Velankar, and Raviraj Joshi. "L3Cube-MahaHate: A Tweet-based Marathi Hate Speech Detection Dataset and BERT Models." Proceedings of the Third Workshop on Threat, Aggression and Cyberbullying (TRAC 2022). 2022.

Velankar, Abhishek, et al. "Hate and offensive speech detection in Hindi and Marathi." arXiv preprint arXiv:2110.12200 (2021).

Kulkarni, Atharva, et al. "L3CubeMahaSent: A Marathi Tweet-based Sentiment Analysis Dataset." Proceedings of the Eleventh Workshop on Computational Approaches to Subjectivity, Sentiment and Social Media Analysis. 2021.

Kulkarni, Atharva, et al. "Experimental Evaluation of Deep Learning Models for Marathi Text Classification." Proceedings of the 2nd International Conference on Recent Trends in Machine Learning, IoT, Smart Cities and Applications. Springer, Singapore, 2022.
```

This project is led by <a href='https://www.linkedin.com/in/ravirajoshi/'> Raviraj Joshi </a> under L3Cube Labs, Pune. For any queries contact ravirajoshi@gmail.com .
