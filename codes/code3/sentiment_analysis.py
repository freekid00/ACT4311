#coding=utf8
"""
Created on Fri Feb 14 08:41:28 2020

@author: Neal LONG

Example of sentiment analysis on articles based on lexicon that covers:
- Data type and operations (such as integer and string here)
- Variable definition and assignment
- Control flow (for loop and if-else)
- Function definition and call
- Others such as comment,indentation, and etc.
- 


1. Read the code, run it and compare/analyze/understand the output
2. Modify the code to improve the efficiency of function analyze_sentiment_polarity
    Hint: use proper data structure to store pos_words and neg_words
"""
# Define a dict to store the sentiment strength score
word_senti_dict={'happy':1,'sad':-1,'good':1,'wonderful':2,'tedious':-1}

# Define a list to store positive words
pos_words = ['happy','good','wonderful']

# Define a list to store positive words
neg_words = ['sad','tedious']

def analyze_sentiment_polarity(article, lower = True):
    """
    Analyze the sentiment polarity of the given article
    Return one integer among -1 or 0 or 1
    """
    pos_count = 0
    neg_count = 0
    raw_words = article.split(" ")
    #knowledge about for loop
    for raw_word in raw_words:
        if lower:
            # normlize the raw_word in lowercase to store to clean_word
            clean_word = raw_word.lower()
        else:
            clean_word = raw_word
        if clean_word in pos_words:
            pos_count += 1
        elif clean_word in neg_words:
            neg_count += 1
    #knowledge about for loop
    if pos_count > neg_count:
        polarity = 1 
    elif neg_count > pos_count:
        polarity = -1
    else:
        polarity = 0
    return polarity
    
    
def analyze_sentiment_score(article, lower = True):
    """
    Analyze the sentiment score of the given article
    Return the sentiment score in integer
    """
    senti_score = 0
    #split article (a string) into words by one whitespace
    raw_words = article.split(" ")
    for raw_word in raw_words:
        if lower:
            # normlize the raw_word in lowercase to store to clean_word
            clean_word = raw_word.lower()
        else:
            clean_word = raw_word
        
        # get the associated sentiment strength of clean_word in word_senti_dict, 
        #       if no, associated strength, return 0
        word_senti = word_senti_dict.get(clean_word,0)
        senti_score += word_senti
    return senti_score

    
articles= ["This is wonderful but tedious","Wonderful but tedious"]
for article in articles:#1m
    print("="*30)
    print("The article to analyze is:", article)
    print("analyze_sentiment_polarity with lowering = ",analyze_sentiment_polarity(article))
    print("analyze_sentiment_polarity with lowering = ",analyze_sentiment_polarity(article, lower=True))
    print("analyze_sentiment_polarity without lowering = ",analyze_sentiment_polarity(article, lower=False))
    print("-"*10)
    print("analyze_sentiment_score with lowering = ",analyze_sentiment_score(article))
    print("analyze_sentiment_score with lowering = ",analyze_sentiment_score(article, lower=True))
    print("analyze_sentiment_score without lowering = ",analyze_sentiment_score(article, lower=False))


        

