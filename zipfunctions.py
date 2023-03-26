names = ["Anna", "John", "Joey", "Mikey", "Bradock"]

ages = [18,23,56,78,19]

# for i in range(len(names)):
#     print(f'Names: {names[i]}, Age: {ages[i]}')

print (list(zip(names,ages)))

for name,age in zip(names,ages):
    print(f'Names: {name}, Age: {age}')


sales = [123, 567, 6754, 3420, 800]

costs = [200, 450, 300, 120, 500]

for sale, cost in zip(sales,costs):
    print(sale-cost)

zipped = [("erik", 40), ("uhtred", 78), ("ashton", 23), ("sosa", 34)]

names1, ages1 = zip(*zipped) # unzip using * operator 

#print(names1, "\n", ages1)

print(list(names1))
print(list(ages1))

letters = ["b","d","a","c"]

nums = [3,2,4,1]

data = sorted(zip(letters,nums))

print(data)

letters,nums = zip(*data)

print(letters)
print(nums)

mydict = dict(zip(letters,nums))
print(mydict)