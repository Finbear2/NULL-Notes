from pathlib import Path

def loadStopwords(path="stopwords.txt") -> set:
    with open(path, encoding="utf-8") as f:
        return {line.strip() for line in f if line.strip()}

def tryFile(path):
    file = Path(path)
    if file.is_file():
        return True
    else:
        return False