def disemvowel(string_):
    char_remove = ["a","e","i","o","u","A","E","I","O","U"]
    
    for char in char_remove:
        string_ = string_.replace(char, "")
    
    return(string_)