from vector_document import Vector
import math

def generate_tf_idf_score(vector, vocabulary, idf):
    tf_idf_vector = []

    for word in vocabulary:
        tf = vector.wordcountDict.get(word, 0) / len(vector.bagOfWords)
        tf_idf_score = tf * idf[word]
        tf_idf_vector.append(tf_idf_score)

    return tf_idf_vector

def process_query(query, volabulary, idf):
    query_vector = Vector(query)
    query_vector.generatewordcountDict()
    return generate_tf_idf_score(query_vector, volabulary, idf)

def calculate_consine_similarity(query_tfidf, document_tfidf):
    dot_product = sum(v1 * v2 for v1, v2 in zip(query_tfidf, document_tfidf))

    magnitude_query = math.sqrt(sum(v1**2 for v1 in query_tfidf))
    magnitude_document = math.sqrt(sum(v2**2 for v2 in document_tfidf))\
    
    if not magnitude_query or not magnitude_document:
        return 0.00
    
    return dot_product/(magnitude_document * magnitude_query)


