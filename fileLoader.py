def loadStopwords(path="stopwords.txt") -> set:
    with open(path, encoding="utf-8") as f:
        return {line.strip() for line in f if line.strip()}
