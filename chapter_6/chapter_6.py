#6-1
print("---------6/1---------")
person = {
    'first_name': 'hyesung',
    'last_name': 'shin',
    'age': 39,
    'city': 'seoul',
    }
print(person['first_name'])
print(person['last_name'])
print(person['age'])
print(person['city'])

#6-2
print("---------6/2---------")
favorite_num = {
    'A': 1,
    'B': 2,
    'C': 3,
    'D': 4,
    'E': 5,
    }

print("A's favorite number is " + str(favorite_num['A']))
print("B's favorite number is " + str(favorite_num['B']))
print("C's favorite number is " + str(favorite_num['C']))
print("D's favorite number is " + str(favorite_num['D']))
print("E's favorite number is " + str(favorite_num['E']))

#6-3
print("---------6/3---------")
glossary = {
    'print': 'output the value',
    'str': 'convert number to string',
    'title': 'capitalize the first letter of the word',
    'for': 'loop through each value in the list',
    'if-else': 'check for condition',
}
print('print: ' + glossary['print'])
print('str: ' + glossary['str'])
print('title: ' + glossary['title'])
print('for: ' + glossary['for'])
print('if-else: ' + glossary['if-else'])

#6-4
print("---------6/4---------")
glossary['list'] = 'a list of values'
glossary['range'] = 'a list of numbers in the range given'
glossary['append'] = 'append the value to the end of the list'
glossary['insert'] = 'insert value to the position given'
glossary['del'] = 'delete a value'
for key, value in glossary.items():
    print(key + ": " + value)

#6-5
print("---------6/5---------")
rivers = {
    'nile': 'egypt',
    'yellow-river': 'china',
    'han-river': 'korea',
    }
for key, value in rivers.items():
    print("The " + key.title() + " runs through " + value.title())

for key in rivers.keys():
    print(key)

for value in rivers.values():
    print(value)

#6-6
print("---------6/6---------")
print("exercise is in favorite_languages.py")

#6-7
print("---------6/7---------")
person2 = {
    'first_name': 'eric',
    'last_name': 'mun',
    'age': 39,
    'city': 'seoul',
    }
person3 = {
    'first_name': 'andy',
    'last_name': 'lee',
    'age': 38,
    'city': 'seoul',
    }
people = [person, person2, person3]
for p in people:
    print("First Name: " + p['first_name'].title())
    print("Last Name: " + p['last_name'].title())
    print("Age: " + str(p['age']))
    print("City: " + p['city'].title())
    print("---")

# 6-8
print("---------6/8---------")
pet1 = {
    'kind': 'dog',
    'owner': 'alex',
    }
pet2 = {
    'kind': 'cat',
    'owner': 'ben',
    }
pet3 = {
    'kind': 'dog',
    'owner': 'jeo',
    }
pets = [pet1, pet2, pet3]
for pet in pets:
    print("Pet Kind: " + pet['kind'] + " Owner: " + pet['owner'])

# 6-9
print("---------6/9---------")
favorite_places = {
    'james': ['las vegas', 'boston'],
    'lena': ['new york', 'seattle', 'beijing'],
    'pat': ['london', 'paris']
}
for key, value in favorite_places.items():
    print(key.title() + "'s favorite places are: ")
    for v in value:
        print(v.title())

# 6-10
print("---------6/10---------")
favorite_nums = {
    'A': [1, 2],
    'B': [2, 3],
    'C': [3],
    'D': [4, 8],
    'E': [5, 6],
    }
for key, value in favorite_nums.items():
    print(key + "'s favorite numbers are(is):")
    for v in value:
        print(v)

# 6-11
print("---------6/11---------")
cities = {
    'boston': {
        'state': 'ma',
        'place': 'boston common',
        'zip': '01801',
        },
    'seattle': {
        'state': 'wa',
        'place': 'space needle',
        'zip': '98119',
        },
    'new york': {
        'state': 'ny',
        'place': 'time square',
        'zip': '10004',
        },
    }
for city, city_info in cities.items():
    print(city.title())
    for k, v in city_info.items():
        print(k.title() + ": " + v.title())
