def vectorize_string(s):
    # Initialize a vector of zeros for 'a' to 'z'
    vector = [0] * 26
    
    # Count the frequency of each character
    for char in s:
        if 'a' <= char <= 'z':
            vector[ord(char) - ord('a')] += 1
    
    return vector

def store_vectors(strings):
    # Vectorize each string and store the vectors in a list
    vectors = [vectorize_string(s.lower()) for s in strings]
    return vectors

def retrieve_vector(vectors, index):
    # Retrieve a vector by its index
    return vectors[index]

# Example usage
strings = ["hello", "world", "python", "code"]
vectors = store_vectors(strings)

# Print all vectors
for i, vector in enumerate(vectors):
    print(f"Vector for string '{strings[i]}': {vector}")

# Retrieve a specific vector
index_to_retrieve = 2
retrieved_vector = retrieve_vector(vectors, index_to_retrieve)
print(f"Retrieved vector for string '{strings[index_to_retrieve]}': {retrieved_vector}")
