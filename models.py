from parser import cleanText

def load_stopwords(path="stopwords.txt") -> set:
    with open(path, encoding="utf-8") as f:
        return {line.strip() for line in f if line.strip()}

class Word:
    
    def __init__(self, name, tags, note):
        
        self.name = name
        self.tags = [tags] if tags else []
        self.notes = [note]

class Note:
    
    def __init__(self, text, name):
        
        self.name = name
        self.text = text
        self.words = cleanText(text, load_stopwords())