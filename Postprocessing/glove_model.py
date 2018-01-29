from utils import *
import json
import nltk.data

## Create the co-occurrence matrix

def fill_coocurrence_matrix(path):
    tokenizer = nltk.data.load('tokenizer/punkt/english.pickle')
    count = 0
    word_keys = [{}]
    with open(path, 'r') as json_file:
        data = json.load(json_file)['review']
    sentences = tokenizer.tokenize(data)
    for element in sentences:
        word_keys.update(retrieve_wordcount(element))
        for word1 in sentence:
            for word2 in sentence:
                if not word1 == word2
                    word_keys[count]['word1'] = word1
                    word_keys[count]['word2'] = word2
                    word_keys[count]['count'] =
