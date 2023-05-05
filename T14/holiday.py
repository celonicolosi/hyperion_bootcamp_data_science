# According to the task file: "It is good practice to define all your
# functions at the top of your code file and the ‘calling’ of them below."

# A function to assert that the user's input is a valid number instead of
# writing while loops for each user input(num_nights and rental_days)
def is_valid_number(message):
    while True:
        try:
            number = int(input(message))
            assert number > 0
            return number
        
        except AssertionError:
            print("\nINVALID CHOICE! Please enter a valid number. (Positive numbers)\n")
    
        except ValueError:
            print("\nINVALID CHOICE! Please enter only numbers.\n")

# This function will take the num_nights as an argument, and return a total
# cost for the hotel stay  
def hotel_cost(num_nights):
    return num_nights * hotels[city_flight]

# This function will take the city_flight as an argument and return a cost for
# the flight
def plane_cost(city_flight):
    return flights[city_flight]

# This function will take the rental_days as an argument and return the total
# cost of the car rental
def car_rental(rental_days):
    # it even give discount to the user if they hire the car for more than
    # 3 days or 7 days
    if rental_days >= 7:
        return (rental_days * 45) - 50
    elif rental_days >= 3:
        return (rental_days * 45) - 20
    else:
        return rental_days * 45
    
def holiday_cost(hotel_cost, plane_cost, car_rental):
    return hotel_cost + plane_cost + car_rental

# create a dictionary of cities and their flight costs (best option for direct
# flights, Economy class, from London, based on Skyscanner)
flights = {
    "Rio De Janeiro": 1000,
    "Lisbon": 115,
    "New York": 480,
    "Tokyo": 1200,
    "Paris": 100,
    "Madrid": 150,
    "Berlin": 150,
    "Rome": 70
}

# create a dictionary of cities and their hotel costs (best option for 3 stars
# hotels, based on Skyscanner)
hotels = {
    "Rio De Janeiro": 27,
    "Lisbon": 73,
    "New York": 210,
    "Tokyo": 49,
    "Paris": 86,
    "Madrid": 69,
    "Berlin": 130,
    "Rome": 72
}

# welcome message
print("\nWelcome to the Holiday Planner!\n")

# presenting the user a list of cities to choose to fly to
print("Here are the cities you can fly to:\n")
for city in cities:
    print("- " + city)

# get the user's choice of city to fly to while treating errors
while True:
    try:
        city_flight = input("\nWhich city would you like to fly to: ").title()
        assert city_flight in cities
        break

    except AssertionError:
        print("\nINVALID CHOICE! Please enter a valid city.\n")

# get the user's choice of nights to stay in a hotel while treating errors
num_nights = is_valid_number("\nHow many nights will you be staying in a hotel for: ")
rental_days = is_valid_number("\nHow many days will you be hiring a car for: ")

# split the print in more lines to make it more readable respecting the 79
# characters per line rule (yeah, I know that some lines above are more than!)
print("\nTotal cost of your holiday: $"
      + str(holiday_cost(hotel_cost(num_nights), plane_cost(city_flight),
                         car_rental(rental_days))) + "\n")
