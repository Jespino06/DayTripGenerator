
Location_list = ['Las Vegas!', 'Vancouver!', 'Cancun!', 'New Orleans! ']
Restaurant_list = ['Hells kitchen!', 'Papadilla!','Sofrito!', 'Amy Ruths! ']
Transportation_list = ['a bus!', 'a train!', 'a flight!', 'a road trip!']
Entertainment_list = ['at a theatrical show!', "at a concert!", "dancing!", "sightseeing!"]

print("")

def greeting():
    message = "Hi there, welcome to Day Trip Generator! Let's get started!!! Your chosen adventure is...drum roll:"
    print(message)

greeting()

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
    randomizer_list(Location_list)
    randomly_selected_destination = randomizer_list(Location_list)
    print(randomly_selected_destination)

    randomizer_list(Restaurant_list)
    randomly_selected_restaurant = randomizer_list(Restaurant_list)
    print(randomly_selected_restaurant)

    randomizer_list(Transportation_list)
    randomly_selected_transportation = randomizer_list(Transportation_list)
    print(randomly_selected_transportation)

    randomizer_list(Entertainment_list)
    randomly_selected_entertainment = randomizer_list(Entertainment_list)
    print(randomly_selected_entertainment)


destination_generator()





def customer_satisfaction():
    print()
    user_choice = input("Are you satisfied with the selected destionation, type Yes or No, change location, restaurant, transportation, or entertainment ")
    if user_choice == "Yes":
        randomly_selected_destination = randomizer_list(Location_list)
        return randomly_selected_destination
    elif user_choice == "No, change restaurant.":
        (randomizer_list)(Restaurant_list)
        newly_selected_restaurant = randomizer_list(Restaurant_list)
        print(newly_selected_restaurant)
    elif user_choice == "No, change transportation.":
        (randomizer_list)(Transportation_list)
        newly_selected_transportation = randomizer_list(Transportation_list)
        print(newly_selected_transportation)
    elif user_choice == "No, change entertainment.":
        (randomizer_list)(Entertainment_list)
        newly_selected_entertainment = randomizer_list(Entertainment_list)
        print(newly_selected_entertainment)
    

customer_satisfaction()


print("")

def display_trip():
    result = (randomly_selected_destination + randomly_selected_restaurant + randomly_selected_transportation + randomly_selected_entertainment)
    return result


display_trip()
print("Have a great time in " + randomly_selected_destination)
print("Enjoy a delicious meal at " + randomly_selected_restaurant)
print("Safe travels on " + randomly_selected_transportation)
print("Have tons of fun " + randomly_selected_entertainment)

print("")