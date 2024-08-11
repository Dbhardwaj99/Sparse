def vectorize_string(s):
    vector = [0] * 26
    
    for char in s:
        if 'a' <= char <= 'z':
            vector[ord(char) - ord('a')] += 1
    
    return vector

def store_vectors(strings):
    vectors = [vectorize_string(s.lower()) for s in strings]
    return vectors

def retrieve_vector(vectors, index):
    return vectors[index]

strings = ["hello", "world", "python", "code"]
vectors = store_vectors(strings)

for i, vector in enumerate(vectors):
    print(f"Vector for string '{strings[i]}': {vector}")


# lets implement cosine similarity
def cosine_similarity(v1, v2):
    dot_product = sum([a * b for a, b in zip(v1, v2)])
    magnitude_v1 = sum([a ** 2 for a in v1]) ** 0.5
    magnitude_v2 = sum([a ** 2 for a in v2]) ** 0.5
    
    return dot_product / (magnitude_v1 * magnitude_v2)

index_to_retrieve = 2
retrieved_vector = retrieve_vector(vectors, index_to_retrieve)
print(f"Retrieved vector for string '{strings[index_to_retrieve]}': {retrieved_vector}")
