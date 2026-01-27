from parser import cleanText
from fileLoader import loadStopwords

class Word:
    
    def __init__(self, name, tags, note):
        
        self.name = name
        self.tags = [tags] if tags else []
        self.notes = [note]

class Note:
    
    def __init__(self, text, name):
        
        self.name = name
        self.text = text
        self.words = cleanText(text, loadStopwords())