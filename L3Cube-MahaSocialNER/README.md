# L3Cube-MahaSocialNER

L3Cube-MahaSocialNER, the first major gold standard social media based named entity recognition dataset in Marathi. This dataset manually curated and the original sentences were taken from MahaSent. The annotation guidelines are mentioned in our paper <a href='https://arxiv.org/abs/2401.00170'> link </a>.

## Dataset Statistics

The dataset is released in IOB and non-IOB form. The non-IOB dataset has total of 15864 samples with 12114 train samples, 2250 test samples, and 1500 validation samples categorized into 8 entity classes.

The fine-tuned MahaBERT model is available on huggingface <a href='https://huggingface.co/l3cube-pune/marathi-social-ner'> MahaSocialNER-BERT </a>. The benchmark results are described in our paper <a href='https://arxiv.org/pdf/2401.00170.pdf'> pdf </a>

## Citing

```
@article{chaudhari2023l3cube,
  title={L3Cube-MahaSocialNER: A Social Media based Marathi NER Dataset and BERT models},
  author={Chaudhari, Harsh and Patil, Anuja and Lavekar, Dhanashree and Khairnar, Pranav and Joshi, Raviraj},
  journal={arXiv preprint arXiv:2401.00170},
  year={2023}
}
```
