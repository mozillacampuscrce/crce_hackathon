import numpy as np

def compute_cosine_similarity(vector_A,vector_B):
    val = np.dot(vector_A,vector_B) /( np.linalg.norm(vector_A) * np.linalg.norm(vector_B))
    if (val>0):
        return val
    else:
        return 0

def cosine_similarity(a,b,x):
    tokens = sorted(set(x))
    bag_of_words_a = []
    bag_of_words_b = []
    for word in tokens:
        bag_of_words_a.append(a.count(word))
    for word in tokens:
        bag_of_words_b.append(b.count(word))
    return round(compute_cosine_similarity(bag_of_words_a,bag_of_words_b), 2)
