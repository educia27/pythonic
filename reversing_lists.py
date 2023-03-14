values = [1,2,3,4,5,6,7,8,9]

# revlist = []

# for index in range(len(values)):
#     revlist.append(values[len(values) - index - 1])

# print(revlist)

# values.reverse()

# print(values)

values1 = list(reversed(values))

print(values1)

values = values[::-1]

print("reversing: ", values)