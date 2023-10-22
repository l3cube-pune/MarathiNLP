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

# The `mahaNLP.autocomplete` module will help you to automatically generate next word or sequence of words given a partially complete text. let's see how it can be used!

# first we install mahaNLP with pip as:
# !pip install --upgrade pip
# !pip install mahaNLP

# Import from generator class
from mahaNLP.autocomplete import TextGenerator

# Create object
generator = TextGenerator()

# Define input sentence
text = "आपण आरोग्याची काळजी घेतली"

# The autocomplete module provides two functionalities:

"""
1) next_word: Predicts the next word in the given sentence

optional parameter(s):
  num_of_predictions (type: integer, Default: 1) =  Used to pass the number of predictions to be made

"""

# For predicting next word in the given sequence:
print(generator.next_word(text))

# To generate n-predictions:
print(generator.next_word(text, num_of_predictions=2))

"""
2) complete_sentence: Predicts the remaining blank words in the given sentence and completes a sentence.

optional parameter(s):
  num_of_words (type: integer, Default: 25) = Used to pass the number of words to be filled
  num_of_prediction (type: integer,  Default: 1) = Used to pass the number of predictions to be made

for example,
"""

# To get 4 predictions, each containing sequence of 10 generated words in given input sequence:
print(generator.complete_sentence(text,
                                  num_of_words=10,
                                  num_of_predictions=4))
