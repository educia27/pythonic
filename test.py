import sys

# str = "we lit"
# print(type(str))

a = b'h\x65llo'
print(list(a))
print(a)

print("-------------------")
# b = 0b10111011
# c = 0xc5f

# print('Binary is %d and heximal is %d' % (b,c))

pantry = [
    ('strawberries', 300),
    ('cantaloupe', 600),
    ('apples', 900),
]

for i, (item, count) in enumerate(pantry):
    print('%d: %-10s = %.2f' % (i, item, count))

print("-------------------")

key = "Nutter Butters"
value = 2.5

formatted = '{} = {}'.format(key, value)
print(formatted)