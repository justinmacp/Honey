from utils import *
import json
from nltk.tokenize import word_tokenize
import numpy as np

'''
    uses json, nltk.data, numpy as np
    fill_co_occurrence_matrix takes in the path to the json file with the filtered text from the preprocessing stage and fills a co-occurrence matrix based on the context
    '''
def fill_co_occurrence_matrix(inpath, outpath):     #function call
    words = []                                      #generate a list to store all words
    context = 10                                    #initilaize an integer variable to hold the size of the context
    with open(inpath, 'r') as json_file:            #open the preprocessign result
        data = json.load(json_file)['result']       #extract the sentences
    
    ### Create a list of unique words   ###
    for i in range(len(data)):                          #go through the sentences
        words_in_sentence = sentence_cleanup(data[i])   #tokenize each sentence
        for word in words_in_sentence:                  #go through each word
            words.append(word)                          #add word to list of total words later used to fill co occurrence matrix
    word_keys = list(set(words))                        #create a set of all unique words used only to get the size of the matix

    ### Fill the co occurrence matrix   ###
    co_occurrence = np.zeros((len(word_keys),len(word_keys)))                           #create the matrix filling it with zeros
    for i in range(len(words)-context):                                                 #go through all unique words
        for j in range(0,context):                                                      #each other word within the context
'''
    Possibility to add a weighting function of 'context' at this point, i.e. a gaussian function
'''
            co_occurrence[word_keys.index(words[i])][word_keys.index(words[j])] += 1    #find index of both words in word_keys and increment that matrix entry
            co_occurrence[word_keys.index(words[j])][word_keys.index(words[i])] += 1

    ### Write results to a file         ###
    co_list = list(co_occurrence)                                           #create list since numpy array isn't JSON serializable
    for i in range(len(co_list)):                                           #go through list of arrays
        co_list[i] = list(co_list[i])                                       #turn every array in the list into a list
    with open(outpath, 'w') as json_outfile:                                #open output file
        json.dump({'header': word_keys, 'matrix': co_list},json_outfile)    #dump header and matrix into the output file

    return co_occurrence, word_keys     #return the matrix and its key to interpret the matrix

