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
    results  = db.search(query)
    # results = SearchItem(query, db)
    # results.search()

    if results:
        print_result(results, query)
        pass
    else:
        print(f"No documents found for the query '{query}'.")

    toc = time.perf_counter()
    print("Time: " + str(toc-tic))

def colorPrint(word, doc):
   # example of word : Document 6 (Cosine Similarity: 0.0616)
    # words: [('captcha', [0], [4, 126])]


    pass

def print_result(results, query):
    print(f"Results for the query '{query}':")
    for similarity, doc_idx, doc, words in results:
        if similarity > 0.0:
            print(f"Document {doc_idx} (Cosine Similarity: {similarity:.4f})\n words: {words}")
            colorPrint(words, results[0][2])
            # print(f"\nMost similar Document: {results[0][2]}")
