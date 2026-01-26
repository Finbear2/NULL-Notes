import string

def normalizeWord(word):
    
    word = word.lower()
    word = word.strip(string.digits)
    word = word.strip(string.punctuation)
    
    if len(word) <= 3:
        return None
    else:
        return word
    
# Function to clean text
def cleanText(text, bufferWords):
    
    words = set()
    
    for word in text.split():
        
        if word.startswith("!"):
            
            words.add(word)
            
        else:
            
            word = normalizeWord(word)
            
            if word:
                if word not in bufferWords:
                    words.add(word)  
                        
    return words or set()