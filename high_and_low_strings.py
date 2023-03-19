def high_and_low(numbers):
    int_array = []
    numbers = numbers.split()
    
    for number in numbers:
        number_int = int(number)
        int_array.append(number_int)
        
    final = (sorted(int_array, reverse=True))
    
    high_and_low = [final[0],final[len(final)-1]]
                    
    back_to_str = ' '.join(str(e) for e in high_and_low)
                    
    return (back_to_str)