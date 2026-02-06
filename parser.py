from flask import url_for
from fileLoader import loadStopwords
from markupsafe import Markup
from utils import normalizeWord
import markdown
import string
import re
   
def highlightHtml(text, user):
    
    bufferWords = loadStopwords()
    
    words = []
    
    parsedText = re.split(r'(\b[a-zA-Z]+\b)', text)
    
    for word in parsedText:
        
        if word != "\n":
            wordNorm = normalizeWord(word)
        else:
            wordNorm = "<br/>"
        
        if wordNorm is not None and wordNorm.isalpha() and wordNorm not in bufferWords:
            
            url = url_for('wordPage', user=user.name, word=word.lower())
            words.append(f'<a href="{url}" class="uniqeWord"><i><b>{word}</b></i></a>')
            
        else:
            
            words.append(word)
            
    text = "".join(map(str, words))
    
    html = markdown.markdown(text, extensions=['extra', 'nl2br'])
    
    return Markup(html)
    
# Function to clean text
def cleanText(text, bufferWords):
    
    words = set()
    
    for word in text.split():
        
        if word.startswith("!"):
            
            words.add(word)
            
        else:
            
            word = normalizeWord(word)
            
            if word is not None:
                if word not in bufferWords:
                    words.add(word)  
                        
    return words or set()