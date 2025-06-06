## MahaEmotions Dataset

**Dataset Name:** L3Cube-MahaEmotions

**Short Description:**
L3Cube-MahaEmotions is a high-quality Marathi emotion recognition dataset designed to address the challenge of limited annotated data in low-resource languages. It features 11 fine-grained emotion labels and combines synthetically annotated training data (generated using Large Language Models like GPT-4) with manually labeled validation and test sets to establish a reliable gold-standard benchmark. The dataset is built upon the existing MahaSent dataset.

**Publication:**
Kowtal, Nidhi, and Raviraj Joshi. "L3Cube-MahaEmotions: A Marathi Emotion Recognition Dataset with Synthetic Annotations using CoTR prompting and Large Language Models." arXiv preprint arXiv:2506.00863 (2025).
[https://arxiv.org/abs/2506.00863](https://arxiv.org/abs/2506.00863)


**Resources Link:**
[Dataset](https://huggingface.co/datasets/l3cube-pune/MahaEmotions)
[Model](https://huggingface.co/l3cube-pune/marathi-emotion-detect)

**GitHub Repository:**
[https://github.com/l3cube-pune/MarathiNLP](https://github.com/l3cube-pune/MarathiNLP)

**Dataset Size:**
* **Total Samples:** 15,000 Marathi sentences
* **Train Set:** 12,000 samples (synthetically annotated)
* **Validation Set:** 1,500 samples (manually annotated)
* **Test Set:** 1,500 samples (manually annotated)

**Language:**
Marathi

**Emotion Labels:**
1.  Happiness
2.  Sadness
3.  Respect
4.  Anger
5.  Fear
6.  Surprise
7.  Disgust
8.  Excitement
9.  Pride
10. Sarcasm
11. Neutral

**Data Collection Methodology:**
* Built upon L3Cube's MahaSent-GT (Marathi sentiment analysis corpus from Twitter).
* **Synthetic Annotation (Training Data):** Achieved using GPT-4 with Chain-of-Translation (CoTR) prompting (Marathi to English translation, then emotion labeling via single prompt).
* **Manual Annotation (Validation & Test Data):** High-quality human-labeled gold-standard benchmark. Primary emotion selected if multiple were present.

**Intended Use Cases:**
* Emotion recognition in low-resource languages (Marathi).
* Benchmarking LLMs and fine-tuned models for Marathi emotion classification.
* Research on synthetic data generation for NLP.
* Development of Marathi NLP applications requiring emotion understanding.

**Evaluation Metrics:**
Commonly includes Accuracy, F1-score (Micro, Macro, Weighted), Precision, Recall.

**Citation:**
```bibtex
@article{kowtal2025l3cube,
  title={L3Cube-MahaEmotions: A Marathi Emotion Recognition Dataset with Synthetic Annotations using CoTR prompting and Large Language Models},
  author={Kowtal, Nidhi and Joshi, Raviraj},
  journal={arXiv preprint arXiv:2506.00863},
  year={2025}
}
