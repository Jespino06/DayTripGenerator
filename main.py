import threading

location_lists = ['Las Vegas', 'Vancouver', 'Cancun', 'New Orleans ']
restaurant_list = ['Hells kitchen', 'Papadilla','Sofrito', 'Amy Ruth ']
transportation_list = ['Bus', 'Train', 'Flight', 'Road trip']
entertainment_list = ['A Play', "A concert", "Dancing", "Sightseeing"]

print("")


import random

a = (random.choice(location_lists))
b = (random.choice(restaurant_list))
c = (random.choice(transportation_list))
d = (random.choice(entertainment_list))
print(a+" ",b+" ", c+" ", d)




