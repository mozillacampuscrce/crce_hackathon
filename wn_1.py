import nltk
from nltk.corpus import wordnet as wn
from nltk.corpus import stopwords
from cos_bow import cosine_similarity
import string

named_entities = []
cos_sim = []
semantic_sim = []
def convert_tag(tag):
    tag_dict = {'N': 'n', 'J': 'a', 'R': 'r', 'V': 'v'}
    try:
        return tag_dict[tag[0]]
    except KeyError:
        return None

def preprocess(token):
    remove_tokens = set(stopwords.words('english')+list(string.punctuation))
    remove_tokens.remove("not")
    filtered_tokens = []
    for w in token:
        if w not in remove_tokens:
            filtered_tokens.append(w)
    return filtered_tokens

def doc_to_synsets(doc):
    tag = nltk.pos_tag(doc)
    nltk2wordnet = [(i[0], convert_tag(i[1])) for i in tag]
    output =[]
    for i,z in nltk2wordnet:
        if (len(wn.synsets(i, z))>0):
            output.append(wn.synsets(i, z)[0])
        else:
            named_entities.append(i)
    return output


def similarity_score(s1, s2):
    list1 = []
    for a in s1:
        list1.append(max([i.path_similarity(a) for i in s2 if i.path_similarity(a) is not None]))
    output = sum(list1)/len(list1)
    return output

def document_path_similarity(doc1, doc2):
    return (similarity_score(doc1, doc2) + similarity_score(doc2, doc1)) / 2

def similarity(a,b):
    tokens1 = nltk.word_tokenize(a)
    tokens2 = nltk.word_tokenize(b)
    processed_tokens1 = preprocess(tokens1)
    processed_tokens2 = preprocess(tokens2)
    synsets1 = doc_to_synsets(processed_tokens1)
    synsets2 = doc_to_synsets(processed_tokens2)
    return round((document_path_similarity(synsets1,synsets2)+cosine_similarity(processed_tokens1,processed_tokens2,named_entities))/2, 2) 
