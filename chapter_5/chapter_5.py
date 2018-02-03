#5-1
print("************** #5-1 **************")
car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')

print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')

print "-------------"
topping = 'mushroom'
print("Is topping == 'mushroom'? I predict True.")
print(topping == 'mushroom')

print("\nIs topping == 'sausage'? I predict False.")
print(topping == 'sausage')

print "-------------"
fruit = 'apple'
print("Is fruit == 'apple'? I predict True.")
print(fruit == 'apple')

print("\nIs fruit == 'orange'? I predict False.")
print(fruit == 'orange')

print "-------------"
language = 'python'
print("Is language == 'java'? I predict False.")
print(language == 'java')

print("\nIs language == 'python'? I predict True.")
print(language == 'python')

print "-------------"
name = 'alex'
print("Is name == 'alex'? I predict True.")
print(name == 'alex')

print("\nIs name == 'betty'? I predict False.")
print(name == 'betty')

#5-2
print("************** #5-2 **************")
print("Test for equality with string")
print(name == 'alex')
print("Test for inequality with string")
print(name != 'betty')
print("Test using lower() function")
print(name.lower() == 'alex')
print("Numerical test with equality")
print(13 == 13)
print("Numerical test with inequality")
print(13 != 14)
print("Numerical test with greater than")
print(13 > 5)
print("Numerical test with greater than or equal to")
print(13 >= 5)
print("Numerical test with less than")
print(3 < 13)
print("Numerical test with less than or equal to")
print(3 <= 13)
print("Test using and keyword")
print(13 > 4 and 5 > 4)
print("Test using or keyword")
print(13 > 4 or 5 < 3)
print("Test whether an item is in a list")
list = ['apple', 'pineapple']
print('apple' in list)
print("Test whether an item is not in a list")
print('orange' not in list)

#5-3
print("************** #5-3 **************")
alien_color = 'green'
if alien_color == 'green':
    print("You just earned 5 points!")
else:
    print()

#5-4
print("************** #5-4 **************")
alien_color = 'yellow'
if alien_color != 'green':
    print("You just earned 10 points!")
else:
    print("You just earned 5 points!")

alien_color = 'green'
if alien_color == 'green':
    print("You just earned 5 points!")
else:
    print("You just earned 10 points!")

#5-5
print("************** #5-5 **************")
alien_color = 'green'
if alien_color == 'green':
    print("You just earned 5 points!")
elif alien_color == 'yellow':
    print("You just earned 10 points!")
elif alien_color == 'red':
    print("You just earned 15 points!")

alien_color = 'yellow'
if alien_color == 'green':
    print("You just earned 5 points!")
elif alien_color == 'yellow':
    print("You just earned 10 points!")
elif alien_color == 'red':
    print("You just earned 15 points!")

alien_color = 'red'
if alien_color == 'green':
    print("You just earned 5 points!")
elif alien_color == 'yellow':
    print("You just earned 10 points!")
elif alien_color == 'red':
    print("You just earned 15 points!")

#5-6
print("************** #5-6 **************")
age = 5
if age < 2:
    print("You're a baby.")
elif 2 <= age < 4:
    print("You're a toddler.")
elif 4 <= age < 13:
    print("You're a kid.")
elif 13 <= age < 20:
    print("You're a teenager.")
elif 20 <= age < 65:
    print("You're an adult.")
elif age >= 65:
    print("You're an elder.")

#5-7
print("************** #5-7 **************")
fruits = ['apple', 'pineapple', 'mango']
if 'banana' in fruits:
    print "'banana' is not my favorite fruit."
if 'pineapple' in fruits:
    print "'pineapple' is my favorite fruit."
if 'orange' in fruits:
    print "'orange' is not my favorite fruit."
if 'apple' in fruits:
    print "'apple' is my favorite fruit."
if 'mango' in fruits:
    print "'mango' is my favorite fruit."

#5-8
print("************** #5-8 **************")
names = ['admin', 'oli', 'terry', 'ty', 'che']
for name in names:
    if name == 'admin':
        print("Hello admin, would you like to see a status report?")
    else:
        print("Hello " + name + ", thank ou for logging in again.")

#5-9
print("************** #5-9 **************")
if names:
    print()
else:
    print("We need to find some users!")

#5-10
print("************** #5-10 **************")
current_users = ['admin', 'oli', 'terry', 'ty', 'che']
new_users = ['a', 'b', 'c', 'd', 'e']
for user in new_users:
    if user.lower() in current_users:
        print("Please enter a new username.")
    else:
        print("The username is available.")

#5-11
print("************** #5-11 **************")
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for number in nums:
    if number == 1:
        print("1st")
    elif number == 2:
        print("2nd")
    elif number == 3:
        print("3rd")
    else:
        print(str(number) + "th")

#5-12
print("************** #5-12 **************")
