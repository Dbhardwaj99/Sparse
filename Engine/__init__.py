import time
from Engine.document import original_document
from Engine.global_document import globalvector
from Engine.search import SearchItem
# import document, global_document

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
    tic = time.perf_counter()
    results = SearchItem(query, db)
    results.search()

    if results:
        print(f"Results for the query '{query}':")
        for similarity, doc_idx, doc in results:
            print(f"Document {doc_idx} (Cosine Similarity: {similarity:.4f})")
        print(f"\nMost similar Document: {results[0][2]}")
    else:
        print(f"No documents found for the query '{query}'.")

    toc = time.perf_counter()
    print("Time: " + str(toc-tic))
