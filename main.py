
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



def display_trip():
    result = (randomly_selected_destination + randomly_selected_restaurant + randomly_selected_transportation + randomly_selected_entertainment)
    return result

display_trip()
print(randomly_selected_destination)
print(randomly_selected_restaurant)
print(randomly_selected_transportation)
print(randomly_selected_entertainment)

print("")
