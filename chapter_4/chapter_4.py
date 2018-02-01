#4-1
print "************* 4-1 *************"
pizzas = ['sausage', 'hawaii', 'cheese']
for pizza in pizzas:
    print "I like " + pizza + " pizza!"

print "I really love pizza!"

#4-2
print "************* 4-2 *************"
animals = ['cat', 'rabbit', 'dog']
for animal in animals:
    print "A " + animal + " would make a great pet!"

print "Any of these animals would make a great pet!"

#4-3
print "************* 4-3 *************"
for value in range(1, 21):
    print(value)

#4-4
print "************* 4-4 *************"
# for value in range(1, 1000001):
#     print value
print "taking to long, omit for now."

#4-5
print "************* 4-5 *************"
million = list(range(1, 1000001))
print min(million)
print max(million)
print sum(million)

#4-6
print "************* 4-6 *************"
for value in range(1, 20, 2):
    print value

#4-7
print "************* 4-7 *************"
values = list(range(3, 31, 3))
for value in values:
    print value

#4-8
print "************* 4-8 *************"
for values in range(1, 11):
    print values ** 3

#4-9
print "************* 4-9 *************"
cube = [value ** 3 for value in range(1, 11)]
print cube

#4-10
print "************* 4-10 *************"
values = list(range(1, 10))
print values[:3]
print values[3:-3]
print values[-3:]

#4-11
print "************* 4-11 *************"
friend_pizzas = pizzas[:]
pizzas.append("A")
friend_pizzas.append("B")
print "My favorite pizzas are "
print pizzas
print "My friend's favorite pizzas are "
print friend_pizzas

#4-12
# see second section of foods.py

#4-13
print "************* 4-13 *************"
foods = ('apple', 'orange', 'banana', 'peach', 'mango')
for food in foods:
    print food

#foods[1] = "watermalon"
print "Modified fruits"

foods = ('apple', 'honeydew', 'watermalon', 'peach', 'mango')
for food in foods:
    print food