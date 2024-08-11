from make_vectors import Vector
import math
from collections import defaultdict
from misc import process_query, generate_tf_idf_score

class globalvector:
    def __init__(self, documents) -> None:
        self.original_document = documents
        self.vocabulary = set()
        self.documentList = []
        self.idfScores = {}

    def createdocumentlist(self):
        for docs in self.original_document.values():
            tempVector = Vector(docs)
            tempVector.generatewordcountDict()
            self.documentList.append(tempVector)

    def createvocabulary(self):
        for document in self.documentList:
            self.vocabulary.update(document.bagOfWords)
        
        self.vocabulary = sorted(self.vocabulary)

    def generateIDFScore(self):
        idf = defaultdict(float)

        doc_length = len(self.documentList)

        for word in self.vocabulary:
            doc_count = sum(1 for document in self.documentList if word in document.wordcountDict)
            idf[word] = math.log(doc_length/ (1 + doc_count)) + 1

        self.idfScores = idf
    
    def generateTFIDFScores(self):
        for document in self.documentList:
            tf_idf_vector = []

            for word in self.vocabulary:
                tf = document.wordcountDict.get(word, 0) / len(document.bagOfWords)
                tf_idf_score = tf * self.idfScores[word]

                tf_idf_vector.append(tf_idf_score)

            document.tf_idf_vector = tf_idf_vector
            print(tf_idf_vector)

    def search(self, queried_string):
        query_tf_idf = process_query(queried_string, self.vocabulary, self.idfScores)

        
    


    