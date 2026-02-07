from pathlib import Path
from models import Word
from models import Note
import inspect

def index(user):
    
    Notes = dict()
    Words = dict()
    
    notesFolder = Path(f"Notes/{user.name}")
    
    for file in notesFolder.glob("*.md"):
        
        if file.name not in Notes:
        
            Notes[file.name] = Note(file.read_text(encoding="utf-8"), file.name)
        
            for word in Notes[file.name].words:
                
                if word in Words:
                    
                    Words[word].notes.append(file.name)
                    
                else:
                    
                    tag = "important" if word.startswith("!") else None
                    Words[word] = Word(word, tag, file.name)
                        
    return Notes, Words
        
def indexSingular(Notes, Words, Filename, User):
    
    notesFolder = Path(f"Notes/{User.name}")
    
    notesTry = Notes.get(Filename)      
    
    if notesTry:
    
        for word in Notes[Filename].words:
        
            for Word in Words:
                    
                if word == Word:
                    
                    if Filename in Words[word].notes:
                        
                        Words[Word].notes.remove(Filename)
                                
        Notes.pop(Filename, None)
    
    for file in notesFolder.glob("*.md"):
        
        if file.name == Filename:
        
            Notes[file.name] = Note(file.read_text(encoding="utf-8"), file.name)
        
            for word in Notes[file.name].words:
                
                if word in Words:
                    
                    Words[word].notes.append(file.name)
                    
                else:
                    
                    tag = "important" if word.startswith("!") else None
                    Words[word] = Word(word, tag, file.name)   
                        
                            
                    
    return Notes, Words