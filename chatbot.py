import nltk
from nltk.corpus import stopwords
import string
import random
from nltk.stem import PorterStemmer

def preprocess(input):

    token = nltk.word_tokenize(input)
    remove_tokens = set(stopwords.words('english')+list(string.punctuation))
    ps = PorterStemmer()
    filtered_tokens = []
    for w in token:
        if w not in remove_tokens:
            filtered_tokens.append(ps.stem(w))
    return filtered_tokens

def reply(input):
    greeting_inputs = ["hello", "hi", "greetings", "sup", "what's up","hey"]
    greeting_response = ["hi!", "hey!", "hi there!", "hello!"]

    thanking_inputs = ["thank","thankyou"]
    thanking_response = ["You are welcome.","Always a pleasure."]

    leaving_inputs = ["bye"]
    leaving_response = ["Bye! Take care!","GoodBye! See you later!"]

    no_response = ["Sorry! I can't answer this question.", "Sorry! Maybe try asking something else?"]

    for word in input:
        if word in greeting_inputs:
            return random.choice(greeting_response)
        if word in leaving_inputs:
            return random.choice(leaving_response)
        if word in thanking_inputs:
            return random.choice(thanking_response)
        else:
            #### AllenNLP ####
            return random.choice(no_response)

user = ""
flag = True
while(flag==True):
    user = str(input())
    user = user.lower()
    tokens = preprocess(user)
    print(reply(tokens))
