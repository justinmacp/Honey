# Honey
# Summary
This software is a preprocessing stage for sentiment analysis. In the testing stage it takes a json file and removes all sentences that don't contribute to the sentiment of the text. For our purposes the text will be a book review.
# Overview
<b>Training:</b></br>
In the training stage this software takes in sentences that have a rating attached to it. This rating is a number from 1 to 5, with 5 being the highest rating and indicating that the sentence is in praise of that which it is talking about. In our case, the case of book reviews, the sentence will give an overall judgement of the book and it is our job to find out wheither or not the sentence is praising or criticizing something about the book. The training stage will create a dictionary file which is indicative of the bias of each word.</br></br>
It calculates word bias according to the following formula:</br></br>
2P(word|word occurs in a rank 5 sentence)+P(word|word occurs in a rank 4 sentence)</br>
––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––</br>
2P(word|word occurs in a rank 1 sentence)+P(word|word occurs in a rank 2 sentence)</br></br>
The bias of the word is going to be less than 1 if the word has negative connotations and it is going to be greater than 1 if the word has positive connotations. A threshold value t<1 will be used to remove any word from the dictionary that has a bias between t and 1/t, so that the dictionary only contains biased words.</br></br>
<b>Testing:</b></br>In the testing stage it takes another book review in a json file and removes sentences that are irrelevant, i.e. they don't pass judgement on the book or on anything about the book. The irrelevant sentences are those, that don't contain any of the words in the dictionary.</br>
