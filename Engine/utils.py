from Engine.vector_document import Vector
import math

def generate_tf_idf_score(vector, vocabulary, idf):
    tf_idf_vector = {}

    for word in vocabulary:
        tf = vector.wordcountDict.get(word, 0) / len(vector.bagOfWords)
        tf_idf_score = tf * idf[word]
        # print(type(tf_idf_score))
        tf_idf_vector[word] = tf_idf_score
        # tf_idf_vector.append(tf_idf_score)

    return tf_idf_vector

def process_query(query, volabulary, idf):
    query_vector = Vector(query)
    query_vector.generatewordcountDict()
    queredied_tf_idf_score = generate_tf_idf_score(query_vector, volabulary, idf)
    query_vector.tf_idf_vector = queredied_tf_idf_score

    return query_vector

def calculate_consine_similarity(query_tfidf, document_tfidf):
    dot_product = sum(v1 * v2 for v1, v2 in zip(query_tfidf.values(), document_tfidf.values()))

    magnitude_query = math.sqrt(sum(v1**2 for v1 in query_tfidf.values()))
    magnitude_document = math.sqrt(sum(v2**2 for v2 in document_tfidf.values()))

    if not magnitude_query or not magnitude_document:
        return 0.00

    return dot_product/(magnitude_document * magnitude_query)

def findWords(queried_vector, document_vector):
    #import the two vectors and we can compare better using the bag of words and the tfidf vector

    common_words = set(queried_vector.bagOfWords).intersection(set(document_vector.bagOfWords))

    position_word = []

    for word in common_words:
        position_word.append((word, queried_vector.wordPosDict[word], document_vector.wordPosDict[word]))

    return position_word
