# L3Cube-MahaNER

L3Cube-MahaNER, the first major gold standard named entity recognition dataset in Marathi. This dataset manually curated and the original sentences were sampled from the MahaCorpus. The annotation guidelines are mentioned in our paper <a href='https://arxiv.org/abs/2204.06029'> link </a>.
The dataset is present in folder L3Cube-MahaNER/

## Dataset Statistics

The dataset is released in IOB and non-IOB form. The non-IOB dataset has total of 25000 samples with 21500 train samples, 2000 test samples, and 1500 validation samples categorized into 8 entity classes.

The fine-tuned MahaBERT model is available on huggingface <a href='https://huggingface.co/l3cube-pune/marathi-ner'> MahaNER-BERT </a>. The benchmark results are described in our paper <a href='https://arxiv.org/pdf/2204.06029.pdf'> pdf </a>

## Citing

```
@inproceedings{litake2022l3cube,
  title={L3Cube-MahaNER: A Marathi Named Entity Recognition Dataset and BERT models},
  author={Litake, Onkar and Sabane, Maithili Ravindra and Patil, Parth Sachin and Ranade, Aparna Abhijeet and Joshi, Raviraj},
  booktitle={Proceedings of the WILDRE-6 Workshop within the 13th Language Resources and Evaluation Conference},
  pages={29--34},
  year={2022}
}
```
