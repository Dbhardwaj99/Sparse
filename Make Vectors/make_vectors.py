class Vector:
    def __init__(self, document: str) -> None:
        self.originalDoc = document
        self.wordcountDict = {}
        self.bagOfWords = []
        self.tf_idf_vector = []
    
    def generatewordcountDict(self):
        if type(self.originalDoc) != str:
            raise ValueError("The Document must be a string")
        
        con = {}

        for word in self.originalDoc.split(" "):
            if word in con:
                con[word] += 1
            else:
                con[word] = 1

        self.bagOfWords = list(con.keys())
        self.wordcountDict = con

    def printValues(self):
        print("Bag of words: ")
        for word in self.bagOfWords:
            print(word)

        print("Word count dictionary: ")
        for key, value in self.wordcountDict.items():
            print(f"{key} appears {value} times in the document!")

        print("Vector embedding od this document: \n" + str(self.tf_idf_vector))


