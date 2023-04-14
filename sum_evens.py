def sum_even_numbers(seq): 
    evens = [x for x in seq if x % 2 == 0]
    
    total = 0
    for number in evens:
        total += number
        
    return total
