import time
from document import original_document
from global_document import globalvector

def createVectorDB():
    tic = time.perf_counter()

    vectordb = globalvector(original_document)
    vectordb.createdocumentlist()
    vectordb.createvocabulary()
    vectordb.generateIDFScore()
    vectordb.generateTFIDFScores()

    toc = time.perf_counter()
    print("Time: " + str(toc-tic))

    return vectordb

def searchDB(query, db):
    results = db.search(query)

    if results:
        print(f"Results for the query '{query}':")
        for similarity, doc_idx in results:
            print(f"Document {doc_idx} (Cosine Similarity: {similarity:.4f})")
    else:
        print(f"No documents found for the query '{query}'.")
