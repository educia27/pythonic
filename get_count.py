def get_count(sentence):
    if len(sentence) == 0:
        return 0
    vowels = ["a","e","i","o","u"]
    
    final = [i for i in sentence if i in vowels]
    
    return len(final)