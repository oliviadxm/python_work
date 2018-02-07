#7-1
print("===============7-1===============")
car = input("Which car would you like to rent? ")
print("Let me see if I can find you a " + car.title())

#7-2
print("===============7-2===============")
party_size = input("How many people are in your dinner group? ")
party_size = int(party_size)

if party_size > 8:
    print("You will need to wait for a while.")
else:
    print("Your table is ready.")

#7-3
print("===============7-3===============")
number = input("Please input a number: ")
number = int(number)

if number % 10 == 0:
    print(str(number) + " is a multiple of 10")
else:
    print(str(number) + " is not a multiple of 10")

#7-4
print("===============7-4===============")
prompt = "\nPlease enter a topping of your choice: "
prompt += "\nEnter 'quit' when you finish. "
while True:
    topping = input(prompt)

    if topping == 'quit':
        break
    else:
        print("Topping " + topping + " added!")

#7-5
print("===============7-5===============")
prompt = "Please enter the age: "
prompt += "\nEnter 'quit' when you finish. "
while True:
    age = input(prompt)
    if age == 'quit':
        break
    elif int(age) < 3:
        print("You don't have to pay.")
    elif 3 <= int(age) < 12:
        print("The price is $10.")
    else:
        print("The price is $15.")

#7-6
print("===============7-6===============")
# while True:
#     print(1)

#7-8
print("===============7-8===============")
sandwich_orders = ['sandwich1', 'sandwich2']
finished_sandwich = []

while sandwich_orders:
    current = sandwich_orders.pop()

    print("Making: " + current.title())
    finished_sandwich.append(current)

    print("\nThe following sandwiches have been made:")
    for finished in finished_sandwich:
        print(finished.title())

#7-9
print("===============7-9===============")
sandwiches = ['sandwich1', 'pastrami', 'lbt', 'pastrami', 'regular', 'pastrami']
print(sandwiches)
while 'pastrami' in sandwiches:
    sandwiches.remove('pastrami')

print(sandwiches)

#7-10
print("===============7-10===============")
responses = {}

polling_active = True

while polling_active:
    name = input("\nWhat is your name? ")
    response = input("Where do you want to go for your dream vacation? ")

    responses[name] = response

    repeat = input("Would you like to let another person respond? (yes/no)")

    if repeat == 'no':
        polling_active = False

print("\n--- Poll Results ---")
for name, response in responses.items():
    print(name + " would like to go " + response + ".")