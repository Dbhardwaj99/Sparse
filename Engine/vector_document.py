class Vector:
    def __init__(self, document: str) -> None:
        self.originalDoc = document
        self.wordcountDict = {}
        self.wordPosDict = {}
        self.bagOfWords = []
        self.tf_idf_vector = {}

    def generatewordcountDict(self):
        if type(self.originalDoc) != str:
            raise ValueError("The Document must be a string")

        con = {}
        pos = {}

        for word in self.originalDoc.split(" "):
            pos[word] = [i for i in range(len(self.originalDoc)) if self.originalDoc.startswith(word, i)]
            if word in con and word in pos:
                # pos[word].append(self.originalDoc.index(word))
                con[word] += 1
            else:
                # pos[word] = [self.originalDoc.index(word)]
                con[word] = 1

        self.bagOfWords = list(con.keys())
        self.wordcountDict = con
        self.wordPosDict = pos

    def printValues(self):
        print("Bag of words: ")
        for word in self.bagOfWords:
            print(word)

        print("Word count dictionary: ")
        for key, value in self.wordcountDict.items():
            print(f"{key} appears {value} times in the document!")

        print("Vector embedding od this document: \n" + str(self.tf_idf_vector))
