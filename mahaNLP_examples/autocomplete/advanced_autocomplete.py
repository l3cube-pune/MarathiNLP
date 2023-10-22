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

# This module will help you to automatically generate next word or sequence of words given a partically complete sentence. let's see how it can be used!

# first we install mahaNLP with pip as:
# !pip install --upgrade pip
# !pip install mahaNLP

# Import the class
from mahaNLP.model_repo import GPTModel

# Create an object
generator = GPTModel()

# List models present in it
print(generator.list_models())

"""
To change the default model:
  Pass the name of the model as the argument:
  generator = GPTModel(model_name = 'name of model')
"""

# This module provides two functionalities:

"""
1) next_word: Predicts the next word in the given sentence

optional parameter(s):
  num_of_predictions (type: integer, Default: 1) =  Used to pass the number of predictions to be made

"""

# Define input sentence
text1 = "मला शाळेत जायला "  # English Translation: 'I want to go to school'

# For predicting next word in the given sequence:
print(generator.next_word(text1))

# To generate n-predictions:
print(generator.next_word(text1, num_of_predictions=4))

"""
2) complete_sentence: Predicts the remaining blank words in the given sentence and completes a sentence.

optional parameter(s):
  num_of_words (type: integer, Default: 25) = Used to pass the number of words to be filled
  num_of_prediction (type: integer,  Default: 1) = Used to pass the number of predictions to be made

"""

# For example, given as sentence:
text2 = 'आज खूप पाऊस'  # English Translation: 'A lot of rain today'

# To get 4 predictions, each containing sequence of 10 generated words in given input sequence:
print(generator.complete_sentence(text2,
                            num_of_words=10,
                            num_of_predictions=4))
