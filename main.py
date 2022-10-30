
location_lists = ['Las Vegas', 'Vancouver', 'Cancun', 'New Orleans ']
restaurant_list = ['Hells kitchen', 'Papadilla','Sofrito', 'Amy Ruths ']
transportation_list = ['a bus', 'a train', 'a flight', 'on a road trip']
entertainment_list = ['at a theatrical show!', "at a concert!", "dancing!", "sightseeing!"]

print("")

input("Want a spontanous day trip?! Type Yes  ")

print("")

import random
a = (random.choice(location_lists))


import random
b = (random.choice(restaurant_list))


import random
c = (random.choice(transportation_list))


import random
d = (random.choice(entertainment_list))



import random
a = (random.choice(location_lists))
b = (random.choice(restaurant_list))
c = (random.choice(transportation_list))
d = (random.choice(entertainment_list))
print("You have an exciting trip to " + a + ".") 
print("Your special place to dine is " + b + ".")
print("Your mode of transportation is " + c + ".")
print("You will have such an exciting time " + d + ".")

print("")

input("Want another destination?, type I want something else. ")
import random
random_index = random.randrange(len(location_lists))
print(location_lists[random_index])

print("")

input("Want another restaurant?, type I want something else. ")
import random
random_index = random.randrange(len(restaurant_list))
print(restaurant_list[random_index])

print("")

input("Want another transportation?, type I want something else. ")
import random
random_index = random.randrange(len(transportation_list))
print(transportation_list[random_index])

print("")

input("Want another entertainment?, type I want something else. ")
import random
random_index = random.randrange(len(entertainment_list))
print(entertainment_list[random_index])

print("")





