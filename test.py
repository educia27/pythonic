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
print("-------------------")
#chapter 12 item 13 catch all unpacking over slicing
car_ages = [0, 9, 4, 8, 7, 20, 19, 1, 6, 15]
car_ages_descending = sorted(car_ages,reverse=True)
#catch all unpacking thru a starred expression
#allows one part of the unpacking assignment to receive all values that didnt
#match any other part of the unpacking pattern 
oldest, second_oldest, *others = car_ages_descending
print(oldest,second_oldest, others)
print("-------------------")
#chapter 12 item 14: sort by complex criteria using key parameter
class Tool:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
    
    def __repr__(self):
        return f'Tool{self.name!r}, {self.weight})'

tools = [
        Tool('level', 3.5),
        Tool('hammer', 1.25),
        Tool('screwdriver', 0.5),
        Tool('chisel', 0.25),
    ]    

print('Unsorted:', repr(tools))
tools.sort(key=lambda x: x.name)
print('\nSorted: ', tools)
print("-------------------")
#Chapter 2 avoiding dict insertion ordering 
# the way that dictionaries preserve insertion ordering is now 
# part of the Python language specificcation
def my_func(**kwargs):
    for key, value in kwargs.items():
        print(f'{key} = {value}')

my_func(sosa = "300", gbe = "gloryGang")

print("-------------------")
#Prefer get over in  and keyError to handle missing dictionary keys
counters2 = {
 'pumpernickel': 2,
 'sourdough': 1,
}
county = counters2.get(key, 0)
counters2[key] = county + 1
print("this is count :", county)
print("this is counters :", counters2)

print("-----------------------")

from collections import defaultdict

visits = {
 'Mexico': {'Tulum', 'Puerto Vallarta'},
 'Japan': {'Hakone'},
}

class Visits:
    def __init__(self):
        self.data = defaultdict(set)
    
    def add(self, country, city):
        self.data[country].add(city)

visits = Visits()
visits.add('England', 'Bath')
visits.add('England','London')
print(visits.data)