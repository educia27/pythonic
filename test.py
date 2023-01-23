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
print("-------------------")
# Chapter 2 item 11 slicing sequences
list = ['a', 'b','c','d','e', 'f','g','h','i']
# someList[inclusive: exclusive]
print("letters1 : " ,list[2:7])
print("letters2 : " ,list[:5]) # beginning 5 items
print("letters3 : " ,list[1:3])
print("letters4 : " ,list[-5:]) # last 5 items

print("-------------------")
#Chapter 2 item 12 striding and slicing
#someList = [start:end:stride]
x = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']

odds = x[::2]
evens = x[1::2]
print(odds)
print(evens)
print("-------------------")
s = "elephant"

reverse =  s[::-1]
print(reverse)
