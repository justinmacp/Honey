import json
'''
    uses json
    retrieve_sentences(path) takes in the path to a json file that is structured as follows:
    
    {"review":
        [{"rating": "5", "sentence": "This is sentence one."},
        {"rating": "5", "sentence": "Sentence two is here."},
        .
        .
        .
        {"rating": "4", "sentence": "The tenth of sentences, which is coincidentally also the last sentence, is written here"}]
    }
    
    it returns 5 lists for each of the different ratings, neglecting any rating that is not an integer number from 1 to 5
'''
def retrieve_sentences(path):               #function to retrieve histogram of word probabilities
    with open(path) as json_file:           #open file
        data = json.load(json_file)         #load file into data
        list5 = list()                      #initialize list for sentences ranked 5
        list4 = list()                      #initialize list for sentences ranked 4
        list3 = list()                      #initialize list for sentences ranked 3
        list2 = list()                      #initialize list for sentences ranked 2
        list1 = list()                      #initialize list for sentences ranked 1
        for p in data['review']:            #parse through sentences
            if p['rating'] == '5' :         #if sentence is ranked 5
                list5.append(p['sentence']) #add sentence to list of rank 5 sentences
            elif p['rating'] == '4' :       #if sentence is ranked 4
                list4.append(p['sentence']) #add sentence to list of rank 4 sentences
            elif p['rating'] == '3' :       #if sentence is ranked 3
                list3.append(p['sentence']) #add sentence to list of rank 3 sentences
            elif p['rating'] == '2' :       #if sentence is ranked 2
                list2.append(p['sentence']) #add sentence to list of rank 2 sentences
            elif p['rating'] == '1' :       #if sentence is ranked 1
                list1.append(p['sentence']) #add sentence to list of rank 1 sentences
    json_file.close()                       #close the file
    return list1,list2,list3,list4,list5    #return all lists in rising order

'''
    retrieve_wordcount(sentencelist) takes in a list that is generated by retrieve_sentences, i.e. this list will contain all sentences from a review in a list and it returns the individual words in all the sentences along with their total count in a dictionary
'''
def retrieve_wordcount(sentencelist):               #function to retrieve wordcount
    wordlist = list()                               #create list to store words
    for p in sentencelist:                          #for each sentence in the list
        splitsen = p.split()                        #split sentences into individual words
        for element in splitsen:                    #for all words in the sentence
            wordlist.append(element)                #add all words to the wordlist
    wordlist = [x for x in wordlist if x != '-']    #remove all dashes from the wordlist

    for i in range(len(wordlist)):          #iterate through all words to remove punctuation etc.
        newstring = wordlist[i]             #place full word into a placeholder
        
        #check beginning of word for apostrophes etc.
        if not (newstring[0].isalnum()):    #if first character is not aphanumeric
            newstring = newstring[1:]       #remove it
        
        #check end of word for punctuation, elipses etc.
        if not (newstring[len(newstring)-1].isalnum()):         #in a 3x nested if statement check the last 3 characters
            newstring = newstring[:len(newstring)-1]            #if last char is a symbol remove it
            if not (newstring[len(newstring)-1].isalnum()):     #if second last char is a symbol
                newstring = newstring[:len(newstring)-1]        #remove it
                if not (newstring[len(newstring)-1].isalnum()): #if third last char is a symbol
                    newstring = newstring[:len(newstring)-1]    #remove it

    wordlist[i] = newstring #replace word from list with the cleaned up string
    
    #instantiate a dictionary object to give the number of times a word has been counted for each word
    dict = {}                       #instantiate the dictionary object
    for element in wordlist:        #go throught the wordlist
        if not element in dict:     #if word doesnt exist in dictionary
            dict[element] = 1       #add word to dictionary
        else:                       #if word already exists in dictionary
            dict[element] += 1      #increment count of word
    return dict                     #return dictionary

'''
    wordbias(wordlist1,wordlist2,wordlist3,wordlist4,wordlist5) takes in dictionaries of words and their wordcounts as generated by retrieve_wordcount. wordbias will perform statistical analysis to check for dependence of a word to the ranking and it will output a dictionary that contains all dependent words with their calcuated bias. Optionally it will also return the expected ranking of a word and the standard deviation of that ranking
'''
def wordbias(wordlist1,wordlist2,wordlist3,wordlist4,wordlist5):    #function to filter out words and give their biases
    probability_given_5 = {}                                        #dictionary that holds 'word' and P('word'|rating = 5)
    probability_given_4 = {}                                        #dictionary that holds 'word' and P('word'|rating = 4)
    probability_given_3 = {}                                        #dictionary that holds 'word' and P('word'|rating = 3)
    probability_given_2 = {}                                        #dictionary that holds 'word' and P('word'|rating = 2)
    probability_given_1 = {}                                        #dictionary that holds 'word' and P('word'|rating = 1)
    total_probability = {}                                          #dictionary that holds 'word' and P('word')
    threshold = .9                                                  #thesholding value to determine if a word is biased
    dependent_words = {}                                            #list of all biased words
    expected_value = {}                                             #expected rating of a word
    standard_deviation = {}                                         #standard deviation of the rating of a given word
    
    #make sure all dictionaries have the same words
    for word in wordlist1:          #iterate through words with rating 1
        if not word in wordlist2:   #if wordlist1 contains a word that is not in dictionary of words with rating 2
            wordlist2[word] = 0     #add that word to dictionary 2
        if not word in wordlist3:   #etc.
            wordlist3[word] = 0
        if not word in wordlist4:
            wordlist4[word] = 0
        if not word in wordlist5:
            wordlist5[word] = 0
    for word in wordlist2:
        if not word in wordlist1:
            wordlist1[word] = 0
        if not word in wordlist3:
            wordlist3[word] = 0
        if not word in wordlist4:
            wordlist4[word] = 0
        if not word in wordlist5:
            wordlist5[word] = 0
    for word in wordlist3:
        if not word in wordlist1:
            wordlist1[word] = 0
        if not word in wordlist2:
            wordlist2[word] = 0
        if not word in wordlist4:
            wordlist4[word] = 0
        if not word in wordlist5:
            wordlist5[word] = 0
    for word in wordlist4:
        if not word in wordlist1:
            wordlist1[word] = 0
        if not word in wordlist2:
            wordlist2[word] = 0
        if not word in wordlist3:
            wordlist3[word] = 0
        if not word in wordlist5:
            wordlist5[word] = 0
    for word in wordlist5:
        if not word in wordlist1:
            wordlist1[word] = 0
        if not word in wordlist2:
            wordlist2[word] = 0
        if not word in wordlist3:
            wordlist3[word] = 0
        if not word in wordlist4:
            wordlist4[word] = 0

    #calculate the sum of all words for each list
    total1 = sum(wordlist1.values())    #the sum of the number words that have been counted in the dictionary of words with rating 1
    total2 = sum(wordlist2.values())    #etc.
    total3 = sum(wordlist3.values())
    total4 = sum(wordlist4.values())
    total5 = sum(wordlist5.values())

    #calculate the probability of a word given its ranking:
    for word in wordlist1:                                          #for all words in dictionary 1
        probability_given_1[word] = float(wordlist1[word])/total1   #P('word'|ranking) = number of 'word'/number of all words given a certain ranking
    for word in wordlist2:                                          #etc.
        probability_given_2[word] = float(wordlist2[word])/total2
    for word in wordlist3:
        probability_given_3[word] = float(wordlist3[word])/total3
    for word in wordlist4:
        probability_given_4[word] = float(wordlist4[word])/total4
    for word in wordlist5:
        probability_given_5[word] = float(wordlist5[word])/total5

    ################################ Using calculations of correlation to calcuate dependence ################################
    
    #EXPECTED VALUE FOR THE RATING OF A WORD
    for word in wordlist1:  #iterate through wordlist1 since it has been augmented to contain all words in all 5 lists
        expected_value[word] = (1.*wordlist1[word] + 2.*wordlist2[word] + 3.*wordlist3[word] + 4.*wordlist4[word] + 5.*wordlist5[word])/(wordlist1[word]+wordlist2[word]+wordlist3[word]+wordlist4[word]+wordlist5[word])    #calcualte the expected rating of that word
        
    #STANDARD DEVIATION OF THE RATING OF A WORD
        standard_deviation[word] = (probability_given_1[word]*(1.-expected_value[word])**2 + probability_given_2[word]*(2.-expected_value[word])**2 + probability_given_3[word]*(3.-expected_value[word])**2 + probability_given_4[word]*(4.-expected_value[word])**2 + probability_given_5[word]*(5.-expected_value[word])**2)**0.5   #calcualte the standard deviation of that rating

    ################################ Using P(X|Y) = P(X)*P(Y) to calcuate dependence ################################

    #check if the word is in the threshold for each value of the ranking: A random variable ('word') is dependent on another random variable (ranking)
    for word in wordlist1:  #for each word
        total_probability[word] = (probability_given_1[word] + probability_given_2[word] + probability_given_3[word] + probability_given_4[word] + probability_given_5[word])/5.    #calculate the total probability
        #to check if the 'word' is dependent on the ranking we introduce a threshold.
        #independence is granted when the fllowing condition is true: P('word'|ranking) = P('word') for all rankings
        #dependence is granted when there is no independence
        threshold1 = threshold*total_probability[word] > probability_given_1[word] or (1./threshold*total_probability[word]) < probability_given_1[word]
        threshold2 = threshold*total_probability[word] > probability_given_2[word] or (1./threshold*total_probability[word]) < probability_given_2[word]
        threshold3 = threshold*total_probability[word] > probability_given_3[word] or (1./threshold*total_probability[word]) < probability_given_3[word]
        threshold4 = threshold*total_probability[word] > probability_given_4[word] or (1./threshold*total_probability[word]) < probability_given_4[word]
        threshold5 = threshold*total_probability[word] > probability_given_5[word] or (1./threshold*total_probability[word]) < probability_given_5[word]
        if threshold1 and threshold2 and threshold3 and threshold4 and threshold5 and probability_given_5[word] != 0 and probability_given_4[word] != 0 and probability_given_3[word] != 0 and probability_given_2[word] != 0 and probability_given_1[word] != 0: #if the word is dependent on the ranking
            dependent_words[word] = (2.*probability_given_5[word]+probability_given_4[word])/(probability_given_2[word]+2.*probability_given_1[word])
        #add the word to the dependent word dictionary with value:  2*P('w'|5)+1*P('w'|4)
        #                                                           ---------------------
        #                                                           2*P('w'|1)+1*P('w'|2)
    return dependent_words, expected_value, standard_deviation, probability_given_5, probability_given_4, probability_given_3, probability_given_2, probability_given_1









