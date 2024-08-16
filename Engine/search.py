class WordsFound:
    def __init__(self, queried_word, documentIndex, document):
        self.word = queried_word
        self.documentIndex = ()
        self.wordDocumentIndex = ()

class SearchItem:
    def __init__(self, query, db):
        self.query = query
        self.documentIndex = 0
        self.document = ""
        self.words = [WordsFound]
