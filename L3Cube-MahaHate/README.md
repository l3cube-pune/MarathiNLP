# L3Cube-MahaHate

L3Cube-MahaHate is the largest publicly available Marathi Hate Speech Detection dataset to date. This dataset is made of Marathi tweets which are manually labelled. The annotation guidelines are mentioned in our paper <a href='https://arxiv.org/abs/2203.13778'> link </a>.
The dataset is present in folder L3Cube-MahaHate/

## Dataset Statistics

The dataset is released in 4-class and 2-class form. The 4-class dataset (with labels hate, offensive, pofane, and not) has total of 25000 samples with 21500 train samples, 2000 test samples, and 1500 validation samples. The 2-class dataset (with labels hate and not) has a total of 37500 samples.

The fine-tuned MahaBERT model is available on huggingface <a href='https://huggingface.co/l3cube-pune/mahahate-multi-roberta'> 4-class </a> and <a href='https://huggingface.co/l3cube-pune/mahahate-bert'> 2-class </a>. The benchmark results are described in our paper <a href='https://arxiv.org/pdf/2203.13778.pdf'> pdf </a>

##Citing
```
@inproceedings{patil2022l3cube,
  title={L3Cube-MahaHate: A Tweet-based Marathi Hate Speech Detection Dataset and BERT Models},
  author={Patil, Hrushikesh and Velankar, Abhishek and Joshi, Raviraj},
  booktitle={Proceedings of the Third Workshop on Threat, Aggression and Cyberbullying (TRAC 2022)},
  pages={1--9},
  year={2022}
}
```
