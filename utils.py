import string

def normalizeWord(word):
    
    word = word.lower()
    word = word.strip(string.digits)
    word = word.strip(string.punctuation)
    
    if len(word) <= 3:
        return None
    else:
        if '"' in word or '(' in word or ')' in word or '[' in word or ']' in word or '/' in word or ':' in word:
            return None
        else:
            return word