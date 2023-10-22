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

#  This module will help you to predict the masked token(s) in the given input text. let's see how it can be used!

# first we install mahaNLP with pip as:
# !pip install --upgrade pip
# !pip install mahaNLP

# Import the class
from mahaNLP.model_repo import MaskFillModel

# Create object
predictor = MaskFillModel()

# List models present in it
print(predictor.list_models())

"""
To change the default model:
  Pass the name of the model as the argument:
  predictor = MaskFillModel(model_name = 'name of model')
"""
#predictor = MaskFillModel(model_name = 'marathi-roberta')

# The mask_fill module provides following functionality:

"""
predict_mask: Predicts the masked token

optional parameter(s):
  details (minimum, medium, all) in string - Default: minimum
    Used to pass the detailedness to be considered
  as_dict (True, False) in boolean - Default: False
    Used to define the print type
"""

# Define input sentence
# English Translation: 'I in Maharashtra [MASK]'
text = 'मी महाराष्ट्रात [MASK].'

"""
Note: while defining the masking token, make sure to change the masking style accordingly based on the type of model supplied (bert, roberta etc.)
      for example, in bert-based models we define mask token as [MASK] while in roberta-based models with define it as <mask>
"""

# Get predictions
print(predictor.predict_mask(text))

# when you want to retrieve scores for each token, set details to "medium"
print(predictor.predict_mask(text, details='medium', as_dict=False))

print(predictor.predict_mask(text, details='all', as_dict=False))

# returns a list of dictionaries as output
print(predictor.predict_mask(text, details='all', as_dict=True))
