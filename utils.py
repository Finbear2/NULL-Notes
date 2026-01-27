import string

def normalizeWord(word):
    
    word = word.lower()
    word = word.strip(string.digits)
    word = word.strip(string.punctuation)
    
    if len(word) <= 3:
        return None
    else:
        return word