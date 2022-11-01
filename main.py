
Location_list = ['Las Vegas!', 'Vancouver!', 'Cancun!', 'New Orleans! ']
Restaurant_list = ['Hells kitchen!', 'Papadilla!','Sofrito!', 'Amy Ruths! ']
Transportation_list = ['a bus!', 'a train!', 'a flight!', 'on a road trip!']
Entertainment_list = ['at a theatrical show!', "at a concert!", "dancing!", "sightseeing!"]

print("")

import random

def randomizer_list(list):
    randomized_choice = (random.choice(list))
    return randomized_choice

randomly_selected_destination = randomizer_list(Location_list)

randomly_selected_restaurant = randomizer_list(Restaurant_list)

randomly_selected_transportation = randomizer_list(Transportation_list)

randomly_selected_entertainment = randomizer_list(Entertainment_list)


def display_trip(destination, restaurant, transportation, entertainment):
    result = (destination + restaurant + transportation + entertainment)
    return result

display_trip(randomly_selected_destination, randomly_selected_restaurant, randomly_selected_transportation, randomly_selected_entertainment)
print(randomly_selected_destination)
print(randomly_selected_restaurant)
print(randomly_selected_transportation)
print(randomly_selected_entertainment)


def destination_generator():
    user_choice = input("Are you satisfied with the selected destionation? Y/N ")
    if user_choice == "Y":
        randomly_selected_destination = randomizer_list(Location_list)
        return randomly_selected_destination
    elif user_choice == "N":
        (randomizer_list)(Location_list)
        newly_selected_location = randomizer_list(Location_list)
        print(newly_selected_location)
    elif user_choice == "N":
        (randomizer_list)(Restaurant_list)
        newly_selected_restaurant = randomizer_list(Restaurant_list)
        print(newly_selected_restaurant)
    elif user_choice == "N":
        (randomizer_list)(Transportation_list)
        newly_selected_transportation = randomizer_list(Transportation_list)
        print(newly_selected_transportation)
    elif user_choice == "N":
        (randomizer_list)(Entertainment_list)
        newly_selected_entertainment = randomizer_list(Entertainment_list)
        print(newly_selected_entertainment)

destination_generator()
print(randomly_selected_destination)



    



        






# input("Are you happy with all of the selections, if not which would you change? " )

# def confirm_trip():
#     while input == "Yes":
#        print(randomly_selected_destination)
#     if input == "No, change location":
#        print(randomly_selected_destination = randomizer_list(Location_list)) 



















# import random
# b = (random.choice(Restaurant_list))


# import random
# c = (random.choice(Transportation_list))


# import random
# d = (random.choice(Entertainment_list))


# #Execution of random choices
# import random
# a = (random.choice(Location_list))
# b = (random.choice(Restaurant_list))
# c = (random.choice(Transportation_list))
# d = (random.choice(Entertainment_list))
# print("You have an exciting trip to " + a) 
# print("Your special place to dine is " + b)
# print("Your mode of transportation is " + c)
# print("You will have such an exciting time " + d)


# print("")

# new_choice=input("Not happy with a selection, key in: Location, Restaurant, Transportation, or Entertainment.  ")

# if new_choice == "Location":
#     print("Your new selection is :", random.choice(Location_list))
# elif new_choice == "Restaurant":
#     print("Your new selection is :", random.choice(Restaurant_list))
# elif new_choice == "Transportation":
#     print("Your new selection is :", random.choice(Transportation_list))
# elif new_choice == "Entertainment":
#     print("Your new selection is :", random.choice(Entertainment_list))

 




# from random import choice


