motorcycles = ['honda', 'yamaha', 'suzuki']
print motorcycles

# motorcycles[0] = 'ducati'
# print motorcycles

motorcycles.append('ducati')
print motorcycles

# motorcycles.insert(0, "ducati")
# print motorcycles

# del motorcycles[0]
# print motorcycles

# del motorcycles[1]
# print motorcycles

# popped_motorcycle = motorcycles.pop()
# print motorcycles
# print popped_motorcycle

# last_owned = motorcycles.pop()
# print "The last motorcycle I owned was a " + last_owned.title() + "."

# first_owned = motorcycles.pop(0)
# print "The first motorcycle I owned was a " + first_owned + "."

# motorcycles.remove('ducati')
# print motorcycles

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print motorcycles
print "\nA " + too_expensive.title() + " is too expensive for me."