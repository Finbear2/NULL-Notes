from fileLoader import loadStopwords
from markupsafe import Markup
from utils import normalizeWord
import markdown
import string
import re
   
def highlightHtml(text):
    
    bufferWords = loadStopwords()
    
    words = []
    
    parsedText = re.split(r'(\b[a-zA-Z]+\b)', text)
    
    for word in parsedText:
        
        wordNorm = normalizeWord(word)
        
        if wordNorm is not None and wordNorm.isalpha() and wordNorm not in bufferWords:
            
            words.append(f'<span class="uniqeWord"><i><b>{word}</b></i></span>')
            
        else:
            
            words.append(word)
            
    text = "".join(map(str, words))
    
    html = markdown.markdown(text, extensions=['extra'])
    
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