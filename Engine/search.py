class WordsFound:
    def __init__(self, queried_word, queryIndex, wordDocumentIndex):
        self.word = queried_word
        self.queryIndex = queryIndex
        self.wordDocumentIndex = wordDocumentIndex

class SearchItem:
    def __init__(self, score: float, document: str, wordFoundArray: list[WordsFound], idx: int):
        self.score = score
        self.documentIndex = idx
        self.document = document
        self.words = wordFoundArray
