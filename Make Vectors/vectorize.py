import math
from collections import defaultdict, Counter

# Sample documents
documents = [
    "the cat in the hat",
    "the quick brown fox",
    "the fox jumped over the lazy dog",
]

# Preprocess text: lowercasing and tokenization
def preprocess(text):
    return text.lower().split()

# Calculate Term Frequency (TF)
def compute_tf(doc):
    tf = Counter(doc)
    for term in tf:
        tf[term] = tf[term] / len(doc)
    return tf

# Calculate Inverse Document Frequency (IDF)
def compute_idf(docs):
    idf = defaultdict(lambda: 0)
    total_docs = len(docs)
    
    for doc in docs:
        for term in set(doc):
            idf[term] += 1
    
    for term, count in idf.items():
        idf[term] = math.log(total_docs / (1 + count)) + 1  # Added 1 to avoid division by zero
    
    return idf

# Compute TF-IDF for each document
def compute_tfidf(docs):
    idf = compute_idf(docs)
    tfidf_docs = []
    
    for doc in docs:
        tf = compute_tf(doc)
        tfidf = {term: tf[term] * idf[term] for term in tf}
        tfidf_docs.append(tfidf)
    
    return tfidf_docs

# Cosine Similarity between two TF-IDF vectors
def cosine_similarity(vec1, vec2):
    # Get the common terms
    common_terms = set(vec1.keys()).intersection(vec2.keys())
    
    # Numerator of the cosine similarity
    numerator = sum([vec1[term] * vec2[term] for term in common_terms])
    
    # Denominator of the cosine similarity
    sum1 = sum([vec1[term]**2 for term in vec1.keys()])
    sum2 = sum([vec2[term]**2 for term in vec2.keys()])
    denominator = math.sqrt(sum1) * math.sqrt(sum2)
    
    if not denominator:
        return 0.0
    return numerator / denominator

processed_docs = [preprocess(doc) for doc in documents]
tfidf_docs = compute_tfidf(processed_docs)

query = "fox over dog"
processed_query = preprocess(query)
query_tfidf = compute_tf(processed_query)

similarities = []
for idx, doc_tfidf in enumerate(tfidf_docs):
    similarity = cosine_similarity(doc_tfidf, query_tfidf)
    similarities.append((similarity, idx))

similarities.sort(reverse=True, key=lambda x: x[0])

print("Query:", query)
print("\nDocuments ranked by similarity:")
for similarity, idx in similarities:
    print(f"Document {idx + 1}: {documents[idx]} (Score: {similarity:.4f})")