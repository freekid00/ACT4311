# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 23:52:33 2020

@author: Neal LONG
"""

class Sentiment_Polarity: 

    def __init__(self, lower_input = True):
        self.lower = lower_input
        
        # Define a set to store positive words
        self.pos_words = {'happy','good','wonderful'}
        
        # Define a set to store positive words
        self.neg_words = {'sad','tedious'}


    def analyze(self, article):
        """
        Analyze the sentiment polarity of the given article
        Return one integer among -1 or 0 or 1
        """
        pos_count = 0
        neg_count = 0
        raw_words = article.split(" ")
        #knowledge about for loop
        for raw_word in raw_words:
            if self.lower:
                # normlize the raw_word in lowercase to store to clean_word
                clean_word = raw_word.lower()
            else:
                clean_word = raw_word
            if clean_word in self.pos_words:
                pos_count += 1
            elif clean_word in self.neg_words:
                neg_count += 1
        #knowledge about for loop
        if pos_count > neg_count:
            polarity = 1 
        elif neg_count > pos_count:
            polarity = -1
        else:
            polarity = 0
        return polarity


class Sentiment_Score: 
    def __init__(self, lower_input = True):
        self.lower = lower_input

        # Define a dict to store the sentiment strength score
        self.word_senti_dict={'happy':1,'sad':-1,'good':1,'wonderful':2,'tedious':-1}
        
    def analyze(self, article):
        """
        Analyze the sentiment score of the given article
        Return the sentiment score in integer
        """
        senti_score = 0
        #split article (a string) into words by one whitespace
        raw_words = article.split(" ")
        for raw_word in raw_words:
            if self.lower:
                # normlize the raw_word in lowercase to store to clean_word
                clean_word = raw_word.lower()
            else:
                clean_word = raw_word
            
            # get the associated sentiment strength of clean_word in word_senti_dict, 
            #       if no, associated strength, return 0
            word_senti = self.word_senti_dict.get(clean_word,0)
            senti_score += word_senti
        return senti_score
