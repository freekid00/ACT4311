# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 23:58:47 2020

@author: Neal LONG
"""

from sentiment_class import Sentiment_Score,Sentiment_Polarity

article = "Wonderful but tedious"
model_1 = Sentiment_Polarity()

print("Sentiment_Polarity with lowering = ",model_1.analyze(article))

model_2 = Sentiment_Score(lower_input=False)
print("Sentiment_Score without lowering = ",model_2.analyze(article))
