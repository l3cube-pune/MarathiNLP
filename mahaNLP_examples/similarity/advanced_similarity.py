# MIT License

# Copyright (c) 2022 L3Cube Pune

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# This module will help you to detect the similarity between marathi texts. let's see how it can be used!

# first we install mahaNLP with pip as:
# !pip install --upgrade pip
# !pip install mahaNLP

# Import class
from mahaNLP.model_repo import SimilarityModel

# Create object
analyzer = SimilarityModel()

# List models present in it
print(analyzer.list_models())

"""
To change the default model:
  Pass the name of the model as the argument:
  analyzer = SimilarityModel(model_name = 'name of model')

"""
analyzer = SimilarityModel(model_name='marathi-sentence-bert-nli')

# The similarity module provides two functionalities:

"""
1) embed_sentences: Embeds the sentences and return the values in an array.

2) get_similarity_score: Checks the similarity of a sentence with respect to array of sentences
    Optional Parameter(s):
      as_dict (True, False) in boolean - Default: False
        Used to define the print type
"""

# Define input sentence to embed
# English Translation: 'There are total 28 states in India.'
text1 = 'भारतात एकूण २८ राज्ये आहेत.'

# For embedding given input sentence:
print(analyzer.embed_sentences(text1))

# Example:

# English Translation: 'Elections are being held for 15 gram panchayats in Vasai taluka.'
textsource = 'वसई तालुक्यातील 15 ग्रामपंचायतींसाठी निवडणूक होत आहे.'
textsentences = ['वसई तालुक्यातील 15 ग्रामपंचायतींसाठी निवडणूक होत आहे.', '28 ते 2 डिसेंबर पर्यंत उमेदवारी अर्ज भरण्याची वेळ असून आज आणि उध्या दोन दिवसात ऑफलाईन उमेदवारी अर्ज भरण्यासाठी 5 वाजेपर्यंत वेळ वाढवून दिला आहे.',
                 'त्यामुळे आज दिवसभरात उमेदवारांनी आपले उमेदवारी अर्ज भरण्यासाठी तहसील कार्यालयात गर्दी केली होती.']
# English Translation:
# [
# 'Elections are being held for 15 gram panchayats in Vasai taluka.',
# 'The time to fill candidature form is from 28th to 2nd December and the time for filling offline candidature form has been extended till 5 pm today and tomorrow.',
# 'Therefore, candidates thronged the tehsil office to fill their nomination forms today.'
# ]

# To find the similarity scores associated with given sentences
print(analyzer.get_similarity_score(textsource, textsentences))

# returns a dictionary as output
print(analyzer.get_similarity_score(textsource, textsentences, as_dict=True))
