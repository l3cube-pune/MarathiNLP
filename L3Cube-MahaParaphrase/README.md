# L3Cube-MahaParaphrase Dataset

Paper: [MahaParaphrase: A Marathi Paraphrase Detection Corpus and BERT-based Models](https://huggingface.co/papers/2508.17444) <br>
Code: https://github.com/l3cube-pune/MarathiNLP

## Overview:
The **L3Cube-MahaParaphrase Dataset** is a Marathi paraphrase detection corpus. It is a high-quality, human-annotated corpus specifically designed for **Marathi**, a low-resource Indic language. It contains 8,000 sentence pairs labeled as either **Paraphrase (P)** or **Non-paraphrase (NP)**. This dataset is useful for tasks like paraphrase detection, semantic similarity, and data augmentation, as well as improving NLP models for low-resource languages.

## Language:
- **Primary Language**: Marathi (Low-resource Indic Language)

## Dataset Size:
- **Number of Sentence Pairs**: 8,000
  - **Paraphrase (P)**: 4000 pairs
  - **Non-paraphrase (NP)**: 4000 pairs

## Annotation:
Each sentence pair in the dataset is manually annotated by human experts. The labels include:
- **Paraphrase (P)**: Sentences that convey the same meaning with different wording.
- **Non-paraphrase (NP)**: Sentences that do not convey the same meaning.

## Intended Use:
The dataset is ideal for training and evaluating NLP models for:
- **Paraphrase Detection**
- **Textual Similarity**
- **Data Augmentation for Low-resource Languages**
- **Transfer Learning for Indic Languages**

## Model Benchmarks:
Standard transformer-based models like **BERT** have been evaluated on this dataset, providing a performance baseline for future research.

## Citation:
If you use this dataset, please cite the original work as follows:
```
@article{jadhav2025mahaparaphrase,
  title={MahaParaphrase: A Marathi Paraphrase Detection Corpus and BERT-based Models},
  author={Jadhav, Suramya and Shanbhag, Abhay and Thakurdesai, Amogh and Sinare, Ridhima and Joshi, Ananya and Joshi, Raviraj},
  journal={arXiv preprint arXiv:2508.17444},
  year={2025}
}
```
