from data_structures.hashtable import Hashtable

# GPT assisted
def left_join(synonyms, antonyms):
    result = []
    for key in synonyms.keys():
        synonym = synonyms.get(key)
        antonym = antonyms.get(key) if antonyms.contains(key) else "NONE"
        result.append([key, synonym, antonym])
    return result