def remove(s):
    newWord = []
    for word in s.split(" "):
        if word.count("!") != 1:
            newWord.append(word)
            
    string = " ".join(newWord)    
    return string
            