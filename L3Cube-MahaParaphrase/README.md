# L3Cube-MahaParaphrase Dataset

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
@article{joshi2022l3cube,
  title={L3cube-mahanlp: Marathi natural language processing datasets, models, and library},
  author={Joshi, Raviraj},
  journal={arXiv preprint arXiv:2205.14728},
  year={2022}
}
```
