
numbers = [1,2,3,4,5,6]

def square(x):
    return x * x

#new_list = [square(i) for i in numbers] # list comprehension

new_list = map(square, numbers)
new_list1 = map(str, numbers)

print(new_list)
print(list(new_list)) #must type cast into a list after using the map function 
print(list(new_list1))


# for i in numbers:
#     new_list.append(square(i))



