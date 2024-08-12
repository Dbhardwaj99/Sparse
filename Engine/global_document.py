from Engine.vector_document import Vector
import math
from collections import defaultdict
from Engine.utils import process_query, generate_tf_idf_score, calculate_consine_similarity

class globalvector:
    def __init__(self, documents) -> None:
        self.original_document = documents
        self.vocabulary = set()
        self.documentList = []
        self.idfScores = {}

    def createdocumentlist(self):
        for docs in self.original_document.values():
            tempVector = Vector(docs.lower())
            tempVector.generatewordcountDict()
            self.documentList.append(tempVector)

    def appenddocument(self, document):
        tempVector = Vector(document)
        tempVector.generatewordcountDict()
        tempVector.tf_idf_vector = generate_tf_idf_score(tempVector, self.vocabulary, self.idfScores)
        self.documentList.append(tempVector)
        self.createvocabulary()
        self.generateIDFScore()
        print("Document added successfully!")

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
            document.tf_idf_vector = generate_tf_idf_score(document, self.vocabulary, self.idfScores)

    def search(self, queried_string):
        query_tf_idf = process_query(queried_string, self.vocabulary, self.idfScores)

        similarities = []

        for idx, document in enumerate(self.documentList):
            similarity = calculate_consine_similarity(query_tf_idf, document.tf_idf_vector)
            similarities.append((similarity, idx, document.originalDoc))

        similarities.sort(reverse=True, key= lambda x: x[0])
        return similarities
