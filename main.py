from utils import *
from glove_model import *

'''
    training on codewords.json; results placed in dict.json
'''
sentence_list = retrieve_sentences('Preprocessing/Training_Data/codewords2.json')
word_count = retrieve_wordcount(sentence_list)
word_bias(word_count,'Preprocessing/Training_Results/dict3.json')

'''
    testing on data.txt using dict.json; results placed in dataout.json
'''
sentence_filter('Preprocessing/Test_Data/data.txt','Preprocessing/Results/dataout.json','Preprocessing/Training_Results/dict3.json')

'''
    Post processing: employing the GloVe algorithm
'''
fill_co_occurrence_matrix('Preprocessing/Results/dataout.json','Postprocessing/cooccur.json')
