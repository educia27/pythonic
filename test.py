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

print("-------------------")

item = ("Bananas", "Pizza")
first, second = item 
print(first, "and", second)

print("-------------------")

snacks = [("Oatmeal", 150), ("Cereal", 280), ("Fit Crunch", 190)]

for index, (name, calories) in enumerate(snacks, start= 1):
    print(f'#{index}: {name} has {calories} calories')

print("-------------------")

flavor_list = ['Vanilla','Strawberry', 'Blueberry', 'Neopolitan']

# for flavor in flavor_list:
#     print(f'{flavor} is delicious and dank.')

for i, sosa in enumerate(flavor_list, 1):
    print(f'{i}: {sosa}')

fresh_fruit = {
 'apple': 10,
 'banana': 8,
 'lemon': 5,
}

count = fresh_fruit.get('lemon', 0)
print(count)