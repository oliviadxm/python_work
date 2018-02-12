# 9-1
print("============== 9-1 ==============")


class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print("This restaurant's name is: " + self.restaurant_name.title() + ".")
        print("And it serve " + self.cuisine_type.title() + " food.")

    def open_restaurant(self):
        print("The restaurant " + self.restaurant_name.title() + " is open now.")


restaurant = Restaurant("UNO", "america")
print("The name of the restaurant is " + restaurant.restaurant_name + ".")
print("The cuisine type of the restaurant is " + restaurant.cuisine_type.title() + ".")
restaurant.describe_restaurant()
restaurant.open_restaurant()

# 9-2
print("============== 9-2 ==============")
restaurant2 = Restaurant("domino", 'pizza')
restaurant3 = Restaurant("kyodon", 'japanese')
restaurant.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()

# 9-3
print("============== 9-3 ==============")


class User:

    def __init__(self, first_name, last_name, login):
        self.first_name = first_name
        self.last_name = last_name
        self.login = login
        self.login_attempts = 0

    def describe_user(self):
        print("User's first name: " + self.first_name.title())
        print("User's last name: " + self.last_name.title())
        print("User's login: " + self.login)

    def greet_user(self):
        print("Hi " + self.first_name.title() + ":")
        print("\tWelcome!")

    def login_attempt(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


user = User("ann", "brown", "abrown")
user2 = User("alex", "carter", "acarter")
user.describe_user()
user.greet_user()
user2.describe_user()
user2.greet_user()

# 9-4
print("============== 9-4 ==============")

restaurant4 = Restaurant('noodle place', 'chinese')
print("The number of customers is " + str(restaurant4.number_served))
restaurant4.number_served = 3
print("The number of customers is " + str(restaurant4.number_served))

# 9-5
print("============== 9-5 ==============")

user5 = User('ming', 'xiao', 'mxiao')
print("User has been attempted to login " + str(user5.login_attempts))
user5.login_attempt()
user5.login_attempt()
print("User has been attempted to login " + str(user5.login_attempts))
user5.reset_login_attempts()
print("User has been attempted to login " + str(user5.login_attempts))

# 9-6
print("============== 9-6 ==============")


class IceCreamStand(Restaurant):

    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['strawberry', 'kiwi']


ice_cream = IceCreamStand('cold stone', 'ice cream')
print(ice_cream.restaurant_name.title() + " is an " + ice_cream.cuisine_type + " restaurant.")
print("It has ice cream of the following flavors: ")
print(ice_cream.flavors)

# 9-7
print("============== 9-7 ==============")
# 9-8
print("============== 9-8 ==============")


class Privileges:

    def __init__(self, privileges=['can add post', 'can delete post', 'can ban user']):
        self.privileges = privileges

    def show_privileges(self):
        print(self.privileges)


class Admin(User):

    def __init__(self, first_name, last_name, login):
        super().__init__(first_name, last_name, login)
        self.privileges = Privileges()

#     def show_previleges(self):
#         print(self.privileges)
#
#
# user7 = Admin('benjamin', 'cat', 'bcat')
# user7.show_previleges()


user7 = Admin('benjamin', 'cat', 'bcat')
user7.privileges.show_privileges()

# 9-9
print("============== 9-9 ==============")
print("In car.py")