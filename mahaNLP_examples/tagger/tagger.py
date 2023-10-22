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

# The `mahaNLP.tagger` module will help you to identify and classify every token in the input text into predefined entity group. let's see how it can be used!

# first we install mahaNLP with pip as:
#!pip install --upgrade pip
#!pip install mahaNLP

# import from tagger class
from mahaNLP.tagger import EntityRecognizer

# create object
tagger = EntityRecognizer()

# define input sentence
text = "भारताचे दुसरे राष्ट्रपती डॉ. सर्वपल्ली राधाकृष्णन यांचा जन्मदिवस म्हणजेच, ५ सप्टेंबर हा दिवस शिक्षक दिन म्हणून साजरा करण्यात येतो."

# The tagger module provides two functionalities:

"""
1) get_token_labels: Prints token and entity label for each word

Optional Parameter(s):
  details(minimum, medium, all) in string - Default: minimum
    Used to pass the detailedness to be considered like entity prediction score, start-end index of word, etc.

  as_dict(True, False) in boolean - Default: False
    Used to define the print type
"""
print(tagger.get_token_labels(text))

print(tagger.get_token_labels(text, details='medium', as_dict=False))

print(tagger.get_token_labels(text, details='all', as_dict=False))

print(tagger.get_token_labels(text, details='all', as_dict=True))

"""
2) get_tokens: Prints a string with all entity lables for the respective tokens in the text

"""
print(tagger.get_tokens(text))
