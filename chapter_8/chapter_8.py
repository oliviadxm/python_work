# 8-1
print("=============== 8-1 ===============")


def display_message():
    print("I am learning chapter 8.")


display_message()


# 8-2
print("=============== 8-2 ===============")


def favorite_book(title):
    print("One of my favorite boos is " + title.title())


favorite_book("Alice in wonderland")


# 8-3
print("=============== 8-3 ===============")


def make_shirt(size, text):
    print("A shirt with size " + size + " and '" + text + "' should be made")


make_shirt("M", "Hello World.")
make_shirt(size='L', text='Hey yo.')

# 8-4
print("=============== 8-4 ===============")


def make_shirt2(size='large', text='I love Python.'):
    print("A shirt with size " + size + " and '" + text + "' should be made")


make_shirt2()
make_shirt2(size='medium')
make_shirt2(size='small', text='lol')

# 8-5
print("=============== 8-5 ===============")


def describe_city(name, country='canada'):
    print(name + " is in " + country)


describe_city('Vancouver')
describe_city('Toronto')
describe_city('Seattle')

# 8-6
print("=============== 8-6 ===============")


def city_country(name, country):
    print(name.title() + ", " + country.title())


city_country('santiago', 'chile')
city_country('seoul', 'korea')
city_country('vancouver', 'canada')


# 8-7
print("=============== 8-7 ===============")


def make_album(artist, title, tracks=''):
    album = {'artist': artist, 'album': title}
    if tracks:
        album['tracks'] = tracks
    print(album)
    return album


make_album('Shinhwa', 'Return', 10)


# 8-8
print("=============== 8-8 ===============")
while True:
    print("\n Please tell me the information:")
    print("(enter 'q' to quit at any time")
    artist = input("What's the name of the artist:")
    if artist == 'q':
        break
    title = input("what's the title of the album:")
    if title == 'q':
        break

    album = make_album(artist, title)
    print(album)

# 8-9
print("=============== 8-9 ===============")
magicians = ['A', 'B', 'C']


def show_magicians(m):
    for magician in m:
        print(magician)


show_magicians(magicians)


# 8-10
print("=============== 8-10 ===============")

great_magician = []


def make_great(m1, m2):
    while m1:
        magician = m1.pop()
        magician = "Great" + magician
        m2.append(magician)
    show_magicians(m2)


make_great(magicians, great_magician)

# 8-11
print("=============== 8-11 ===============")
make_great(magicians, great_magician)


# 8-12
print("=============== 8-12 ===============")


def make_sandwich(*items):
    print("The sandwich with the following items: ")
    for item in items:
        print("- " + item)


make_sandwich('ham')
make_sandwich('bacon', 'cheese')
make_sandwich('lettuce', 'bacon', 'tomato')

# 8-13
print("=============== 8-13 ===============")


def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile


user_profile = build_profile('Olivia', 'Mo',
                             location='worcester',
                             field='cs')
print(user_profile)

# 8-14
print("=============== 8-14 ===============")


def build_car(manufacturer, model, **info):
    car = {}
    car['manufacturer'] = manufacturer
    car['mode'] = model
    for key, value in info.items():
        car[key] = value
    return car


car = build_car('subaru', 'outback', color='blue', tow_package=True)
print(car)