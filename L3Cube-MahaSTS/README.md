# L3Cube-MahaSTS Dataset

Paper: [L3Cube-MahaSTS: A Marathi Sentence Similarity Dataset and Models](https://arxiv.org/abs/2508.21569) <br>
Code: https://github.com/l3cube-pune/MarathiNLP

## Overview:
The **L3Cube-MahaSTS Dataset** is a human-annotated **Sentence Textual Similarity (STS)** corpus for **Marathi**, a low-resource Indic language. It contains **16,860 sentence pairs** annotated with **continuous similarity scores ranging from 0 to 5**. 

To ensure robust and balanced supervision, the dataset is **uniformly distributed** across six score buckets (0, 1, 2, 3, 4, 5), which helps reduce label bias and improves model generalization in low-resource settings. This dataset is ideal for training regression-based semantic similarity models and benchmarking STS performance in Indic NLP.

## Language:
- **Primary Language**: Marathi (Low-resource Indic Language)

## Dataset Size:
- **Number of Sentence Pairs**: 16,860
- **Similarity Score Range**: 0 to 5 (Continuous)
- **Balanced Buckets**: Uniform distribution across 6 score-based buckets

## Annotation:
Each sentence pair is manually annotated by human experts. The annotations reflect **semantic similarity** using a fine-grained **0–5 scale**:
- **0**: Completely unrelated
- **1–2**: Low to moderate similarity
- **3–4**: High similarity
- **5**: Paraphrases or semantically equivalent

The bucketed distribution ensures that models trained on the dataset do not overfit to any particular similarity level.

## Intended Use:
This dataset can be used to train and evaluate NLP models for:
- **Sentence Textual Similarity (STS)**
- **Semantic Sentence Matching**
- **Regression-based Similarity Scoring**
- **Transfer Learning for Indic Languages**
- **Sentence Embedding Evaluation**

## Model Benchmarks:
We introduce [**MahaSBERT-STS-v2**](https://huggingface.co/l3cube-pune/marathi-sentence-similarity-sbert-v2), a Sentence-BERT model fine-tuned on the MahaSTS dataset. It is benchmarked against other multilingual and Indic BERT models.

These evaluations demonstrate the effectiveness of the MahaSTS dataset and highlight the benefits of human-annotated supervision in low-resource language settings.

## Citation:
If you use this dataset, please cite the original work as follows:

```
@article{mirashi2025l3cube,
  title={L3Cube-MahaSTS: A Marathi Sentence Similarity Dataset and Models},
  author={Mirashi, Aishwarya and Joshi, Ananya and Joshi, Raviraj},
  journal={arXiv preprint arXiv:2508.21569},
  year={2025}
}
```
