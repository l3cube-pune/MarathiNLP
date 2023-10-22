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

# This module will help you to identify and classify every token in the input text into predefined entity group. let's see how it can be used!

# first we install mahaNLP with pip as:
# !pip install --upgrade pip
# !pip install mahaNLP

# Import the class
from mahaNLP.model_repo import NERModel

# Create an object
tagger = NERModel()

# List models present in it
print(tagger.list_models())

"""
To change the default model:
  Pass the name of the model as the argument:
  tagger = NERModel(model_name = 'name of model')
"""

# The tagger module provides two functionalities:

"""
1) get_token_labels: Prints token and entity label for each word

Optional Parameter(s):
  details(minimum, medium, all) in string - Default: minimum
    Used to pass the detailedness to be considered like entity prediction score, start-end index of word, etc.

  as_dict(True, False) in boolean - Default: False
    Used to define the print type
"""

# Define input sentence
text = "१७ तारखेला आदित्य पुण्यात आला."

# To identify entity type/group for each word in the given text:
print(tagger.get_token_labels(text))

# when details = "medium" is set, the function returns scores assciated with each word as well
print(tagger.get_token_labels(text, details='medium', as_dict=False))

print(tagger.get_token_labels(text, details='all', as_dict=False))

# returns list of dictionaries as output
print(tagger.get_token_labels(text, details='all', as_dict=True))

# English Translation: 'Megha and Lata will go to Mahabaleshwar on 4th.'
text2 = 'मेघा आणि लता ४ तारखेला महाबळेश्वरला जाणार आहे.'

# The `get_tokens` function returns a string containing entity-group for each word in text
print(tagger.get_tokens(text2))
