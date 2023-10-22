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

# The `mahaNLP.hate` module will help you to perform marathi hate speech detection task. let's see how it can be used!

# first we install mahaNLP with pip as:
# !pip install --upgrade pip
# !pip install mahaNLP

# import from hate class
from mahaNLP.hate import HateAnalyzer

# create object
analyzer = HateAnalyzer()

print(analyzer.list_supported_labels())

# define input sentence
# English Translation: 'She is stupid. I don't like her.'
text1 = 'ती मूर्ख आहे. मला ती आवडत नाही.'

# English Translation: 'I appreciate you so much.'
text2 = 'मला तुझे खूप कौतुक वाटते.'

# The hate module provides following functionality:

"""
get_hate_score: Gives the hate score of a sentence. It gives the scores as hate (1) and non-hate (0)

"""

print(analyzer.get_hate_score(text1))

print(analyzer.get_hate_score(text2))
