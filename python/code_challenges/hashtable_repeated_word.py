from data_structures.hashtable import Hashtable

# GPT Assisted
def first_repeated_word(input_string):
    normalized_string = ''.join(char if char.isalnum() or char.isspace() else ' ' for char in input_string.lower())
    
    words = normalized_string.split()
    
    hashtable = Hashtable()
    
    for word in words:
        if word:  
            if hashtable.has(word):
                return word
            hashtable.set(word, True)
    
    return None
