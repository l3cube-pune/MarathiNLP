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

## The `mahaNLP.sentiment` module will help you to perform sentiment analysis task on marathi text. let's see how it can be used!

##first we install mahaNLP with pip as:
# !pip install --upgrade pip
# !pip install mahaNLP

#import sentiment class
from mahaNLP.sentiment import SentimentAnalyzer

#create object
analyzer = SentimentAnalyzer()

# define input sentence
text1 = 'दिवाळीच्या सणादरम्यान सगळे आनंदी असतात.' # English Translation: 'Everyone is happy during Diwali festival.'
text2 = 'मी तुझा तिरस्कार करते.' # English Translation:  'I hate you.'
text3 = 'मी कॉलेजला जात आहे.' # English Translation: 'I am going to college.'

# The autocomplete module provides following functionality:

"""
get_polarity_score: Gives the polarity score of words in a sentence along with the tokens (Neutral, Positive, Negative)

"""

# Example:
print(analyzer.get_polarity_score(text1))

# Example:
print(analyzer.get_polarity_score(text2))

# Example:
print(analyzer.get_polarity_score(text3))