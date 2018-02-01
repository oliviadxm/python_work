#3-1
print "************* 3-1 *************"
friends = ['A', 'B', 'C']
print friends[0]
print friends[1]
print friends[2]

#3-2
print "************* 3-2 *************"
message = "Hi my friend " + friends[0] + "."
print message
message = "Hi my friend " + friends[1] + "."
print message
message = "Hi my friend " + friends[2] + "."
print message

#3-3
print "************* 3-3 *************"
transportations = ['car', 'motorcycle']
brands = ['Honda', 'Subaru']
message = "I would like to own a " + brands[0] + " " + transportations[0] + "."
print message
message = "I would like to own a " + brands[0] + " " + transportations[1] + "."
print message
message = "I would like to own a " + brands[1] + " " + transportations[0] + "."
print message
message = "I would like to own a " + brands[1] + " " + transportations[1] + "."
print message

#3-4
print "************* 3-4 *************"
guests = ['Abby', 'Bob', 'Cathy']
print "The guests list is length of " + str(len(guests))
print "Hi " + guests[0] + ", I would like to invite you to dinner. Would you like to come?"
print "Hi " + guests[1] + ", I would like to invite you to dinner. Would you like to come?"
print "Hi " + guests[2] + ", I would like to invite you to dinner. Would you like to come?"

#3-5
print "************* 3-5 *************"
print guests[0] + " cannot make it. Replacing..."
guests[0] = 'Alex'
print "Hi " + guests[0] + ", I would like to invite you to dinner. Would you like to come?"
print "Hi " + guests[1] + ", I would like to invite you to dinner. Would you like to come?"
print "Hi " + guests[2] + ", I would like to invite you to dinner. Would you like to come?"

#3-6
print "************* 3-6 *************"
print "Hi all, I have found a larger table."
guests.insert(0, "Zoey")
print "The guests list is length of " + str(len(guests))
guests.insert(1, "Betty")
print "The guests list is length of " + str(len(guests))
guests.append("Dylon")
print "The guests list is length of " + str(len(guests))
print "Hi " + guests[0] + ", I would like to invite you to dinner. Would you like to come?"
print "Hi " + guests[1] + ", I would like to invite you to dinner. Would you like to come?"
print "Hi " + guests[2] + ", I would like to invite you to dinner. Would you like to come?"
print "Hi " + guests[3] + ", I would like to invite you to dinner. Would you like to come?"
print "Hi " + guests[4] + ", I would like to invite you to dinner. Would you like to come?"
print "Hi " + guests[5] + ", I would like to invite you to dinner. Would you like to come?"

#3-7
print "************* 3-7 *************"
print "Hi all, sorry about this but I can only invite two people for dinner."
guest1 = guests.pop()
print "Hi " + guest1 + ", sorry I can not invite you to dinner."
print "The guests list is length of " + str(len(guests))
guest2 = guests.pop()
print "Hi " + guest2 + ", sorry I can not invite you to dinner."
print "The guests list is length of " + str(len(guests))
guest3 = guests.pop()
print "Hi " + guest3 + ", sorry I can not invite you to dinner."
print "The guests list is length of " + str(len(guests))
guest4 = guests.pop()
print "Hi " + guest4 + ", sorry I can not invite you to dinner."
print "The guests list is length of " + str(len(guests))
print "Hi " + guests[0] + ", you are still on my list for dinner."
print "Hi " + guests[1] + ", you are still on my list for dinner."
del guests[0]
print "The guests list is length of " + str(len(guests))
del guests[0]
print "The guests list is length of " + str(len(guests))
print guests

#3-8
print "************* 3-8 *************"
places = ['Seoul', 'Tokyo', 'Paris', 'London', 'Hawaii']
print places
print sorted(places)
print places
print sorted(places, reverse=True)
print places
places.reverse()
print places
places.reverse()
print places
places.sort()
print places
places.sort(reverse=True)
print places

#3-9 changes are inline from 3-4 to 3-7

#3-10
cities = ['Vancouver', 'Seattle', 'Worcester', 'New York']
cities.append('Woburn')
cities.insert(3, 'Jersey City')
print "cities length " + str(len(cities))
print sorted(cities)
print sorted(cities, reverse=True)
