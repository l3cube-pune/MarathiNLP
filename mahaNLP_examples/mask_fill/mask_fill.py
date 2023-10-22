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

## The `mahaNLP.mask_fill` module will help you to predict the masked tokens in the given input text. let's see how it can be used!

##first we install mahaNLP with pip as:
# !pip install --upgrade pip
# !pip install mahaNLP

#import from mask_fill class
from mahaNLP.mask_fill import MaskPredictor

#create object
predictor = MaskPredictor()

# define input sentence
text = 'मी महाराष्ट्रात [MASK].' # English Translation: 'I in Maharashtra [MASK]'

# The mask_fill module provides following functionality:

"""
predict_mask: Predicts the masked token

optional parameter(s):
  details (minimum, medium, all) in string - Default: minimum
    Used to pass the detailedness to be considered
  as_dict (True, False) in boolean - Default: False
    Used to define the print type

"""

print(predictor.predict_mask(text))

print(predictor.predict_mask(text, details = 'medium', as_dict = False))

print(predictor.predict_mask(text, details = 'all', as_dict = False))

print(predictor.predict_mask(text, details = 'all', as_dict = True))

