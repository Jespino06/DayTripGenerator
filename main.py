
import random


location_lists = ['Las Vegas', 'Vancouver', 'Cancun', 'New Orleans ']
restaurant_list = ['Hells kitchen', 'Papadilla','Sofrito', 'Amy Ruth ']
transportation_list = ['Bus', 'Train', 'Flight', 'Road trip']


def my_destinations():
    for location in location_lists:
        print (location)
        
my_destinations()

print("")

def my_resturants():
    for restaurant in restaurant_list:
        print (restaurant)
        
my_resturants()

print("")

def my_transportation():
    for transportation in transportation_list:
        print (transportation)
        
my_transportation()

a = (random.choice(location_lists))
b = (random.choice(restaurant_list))
c = (random.choice(transportation_list))
print(a+" ",b+" ", c)
