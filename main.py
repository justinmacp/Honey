'''
    training on codewords.json; results placed in dict.json
'''
from utils import *

sentences50,sentences60,sentences70,sentences80,sentences90 = retrieve_sentences('Preprocessing/Training_Data/codewords2.json')
wordcount90 = retrieve_wordcount(sentences90)
wordcount80 = retrieve_wordcount(sentences80)
wordcount70 = retrieve_wordcount(sentences70)
wordcount60 = retrieve_wordcount(sentences60)
wordcount50 = retrieve_wordcount(sentences50)
dependent_words, expected_value, standard_deviation, probability_given_5, probability_given_4, probability_given_3, probability_given_2, probability_given_1 = wordbias(wordcount50,wordcount60,wordcount70,wordcount80,wordcount90,'Preprocessing/Training_Results/dict.json')
'''
    testing on data.txt using dict.json; results placed in dataout.json
'''
sentence_filter('Preprocessing/Test_Data/data.txt','Preprocessing/Results/dataout.json','Preprocessing/Training_Results/dict.json')
