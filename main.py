
Location_list = ['Las Vegas', 'Vancouver', 'Cancun', 'New Orleans ']
Restaurant_list = ['Hells kitchen', 'Papadilla','Sofrito', 'Amy Ruths ']
Transportation_list = ['a bus', 'a train', 'a flight', 'on a road trip']
Entertainment_list = ['at a theatrical show!', "at a concert!", "dancing!", "sightseeing!"]

print("")

# input("Want a spontanous day trip?! Type Yes  ")

print("")

import random
a = (random.choice(Location_list))


import random
b = (random.choice(Restaurant_list))


import random
c = (random.choice(Transportation_list))


import random
d = (random.choice(Entertainment_list))



import random
a = (random.choice(Location_list))
b = (random.choice(Restaurant_list))
c = (random.choice(Transportation_list))
d = (random.choice(Entertainment_list))
print("You have an exciting trip to " + a + ".") 
print("Your special place to dine is " + b + ".")
print("Your mode of transportation is " + c + ".")
print("You will have such an exciting time " + d + ".")

print("")

new_choice=input("Not happy with a selection, type the one you would like to change. ")

if new_choice == "Location":
    print("Your new selection is :", random.choice(Location_list))
elif new_choice == "Restaurant":
    print("Your new selection is :", random.choice(Restaurant_list))
elif new_choice == "Transportation":
    print("Your new selection is :", random.choice(Transportation_list))
elif new_choice == "Entertainment":
    print("Your new selection is :", random.choice(Entertainment_list))

print("")   