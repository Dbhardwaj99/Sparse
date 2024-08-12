from Engine.utils import calculate_consine_similarity, generate_tf_idf_score
from Engine.vector_document import Vector

# G704
class SearchItem:
    def __init__(self, queriedString:str) -> None:
        self.keywords = []
        self.similarity_array = []
        self.similardocument = ""
        self.queriedString = queriedString


    def search(self, queriedDb):
        query_tf_idf = quriedDb.process_query(queriedDB.vocabulary, queriedDB.idfScores)

        similarities = []

        for idx, document in enumerate(db.documentList):
            similarity = calculate_consine_similarity(query_tf_idf, document.tf_idf_vector)
            similarities.append((similarity, idx, document.originalDoc))

        return similarities
        similarities.sort(reverse=True, key= lambda x: x[0])
