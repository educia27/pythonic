numbers = [1,22,44,3,5,78,6,21,8]

even = [x for x in numbers if x % 2 == 0]

print(even)

powers = [2 ** i for i in numbers]

print(powers)

words = ['automobile','car','anger','fox','anchor']

words = [word.upper() if word.startswith('a') else word for word in words]

print(words)