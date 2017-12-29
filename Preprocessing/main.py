'''
    training on codewords.json; results placed in dict.json
'''
from utils import *

vocab_count = list()    #for GloVe purposes
sentences1,sentences2,sentences3,sentences4,sentences5, = retrieve_sentences('Training_Data/codewords.json')
wordcount5 = retrieve_wordcount(sentences5)
wordcount4 = retrieve_wordcount(sentences4)
wordcount3 = retrieve_wordcount(sentences3)
wordcount2 = retrieve_wordcount(sentences2)
wordcount1 = retrieve_wordcount(sentences1)
vocab_count.append(wordcount1)
vocab_count.append(wordcount2)
vocab_count.append(wordcount3)
vocab_count.append(wordcount4)
vocab_count.append(wordcount5)
dependent_words, expected_value, standard_deviation, probability_given_5, probability_given_4, probability_given_3, probability_given_2, probability_given_1 = wordbias(wordcount1,wordcount2,wordcount3,wordcount4,wordcount5,'Training_Results/dict.json')
'''
    testing on data.txt using dict.json; results placed in dataout.json
'''
sentence_filter('Test_Data/data.txt','Results/dataout.json','Training_Results/dict.json')
