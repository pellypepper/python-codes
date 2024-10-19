#Puesdo code
# import the sys module and the tabulate module
# declare a list called city
# declare a function called hotel_cost that takes in a parameter called city_num
# declare a variable called costpernight and assign 20 to it
# declare a variable called hotel_total and assign the city_num multiplied by 30
# return the hotel_total
# declare a function called plane_cost that takes in a parameter called choice
# declare a dictionary called city_cost
# using a for loop to iterate through the city_cost
# using if statement to check if choice is in city
# return the city_cost of the choice
# declare a function called car_rental that takes in a parameter called rental_num
# declare a variable called car_total and assign the rental_num multiplied by 50
# return the car_total
# declare a function called holiday_cost that takes in three parameters city_num, choice and rental_num
# declare a variable called hotel and assign the hotel_cost function with city_num as the argument
# declare a variable called plane and assign the plane_cost function with choice as the argument
# declare a variable called car and assign the car_rental function with rental_num as the argument
# print the total cost of your hotel stay
# print the total cost of your car rental
# print the total cost of your plane cost
# declare a variable called total_cost and assign the sum of hotel, plane and car
# print the total cost of your holiday
# declare a function called store_input

# declare a variable called header and assign a list of strings
# print the list of cities
# declare a variable called choice and assign the input function
# declare a variable called found and assign False to it
# using a for loop to iterate through the city
# using if statement to check if choice is in row
# assign True to found
# declare a variable called city_num and assign the integer of the input function
# declare a variable called rental_num and assign the integer of the input function
# call the holiday_cost function with city_num, choice and rental_num as the arguments
# break out of the loop
# using if statement to check if found is False  
# print city not found in the list
# call the store_input function
# declare a variable called user_input and assign the input function
#using if statement to check if user_input is 1
# call the store_input function
# using else if statement to check if user_input is 2
# exit the program
# print goodbye

# import the sys module and the tabulate module
import sys
from tabulate import tabulate

 # declare a list called city
city = [[1, "Texas"],
            [2, "London"],
            [3, "Lagos"],
            [4, "Paris"],
            [5, "Greece"],
            [6, "Dubai"],
            [7, "Tokyo"],
            [8, "Sydney"],
            [9, "Nicosia"],
            [10, "Barcelona"]]
    # declare a variable called header and assign a list of strings
header = ["No", "City"]


# declare a function called hotel_cost that takes in a parameter called city_num
def hotel_cost(city_num):


    # declare a variable called costpernight and assign 20 to it
    costpernight = 20
    # declare a variable called hotel_total and assign the city_num multiplied by 30
    hotel_total = city_num * costpernight
    # return the hotel_total
    return hotel_total
   

# declare a function called plane_cost that takes in a parameter called choice
def plane_cost(choice):



    # declare a dictionary called city_cost
    city_cost = {
       "Texas": 400,
       "London": 500,
       "Lagos": 600,
       "Paris": 700,
       "Greece": 800,
       "Dubai": 900,
       "Tokyo": 1000,
       "Sydney": 1100,
       "Nicosia": 1200,
       "Barcelona": 1300
   }
    # using a for loop to iterate through the city_cost
    for city in city_cost:
        # using if statement to check if choice is in city
        if choice in city:
            # return the city_cost of the choice
            return city_cost[choice]
        

# declare a function called car_rental that takes in a parameter called rental_num
def car_rental(rental_num):


    # declare a variable called car_total and assign the rental_num multiplied by 50
    car_total = rental_num * 30
    # return the car_total
    return car_total

    
# declare a function called holiday_cost that takes in three parameters city_num, choice and rental_num
def holiday_cost(city_num, choice , rental_num):


    # declare a variable called hotel and assign the hotel_cost function with city_num as the argument
    hotel = hotel_cost(city_num)
    # declare a variable called plane and assign the plane_cost function with choice as the argument
    plane = plane_cost(choice)
    # declare a variable called car and assign the car_rental function with rental_num as the argument
    car = car_rental(rental_num)
    # print the total cost of your hotel stay
    print("The total cost of your hotel stay is : $",hotel)
    # print the total cost of your car rental
    print("The total cost of your car rental is : $",car)
    # print the total cost of your plane cost
    print("The total cost of your plane cost is : $",plane)
    # declare a variable called total_cost and assign the sum of hotel, plane and car
    total_cost = hotel + plane + car
    # print the total cost of your holiday
    print(f"The total cost of your holiday is :  ${total_cost:.2f}")


# declare a function called store_input
def store_input ():

    
     # print the list of cities
    print(tabulate(city, headers=header, tablefmt="grid"))
    # declare a variable called choice and assign the input function
    choice = input("Enter the city of your choice : ")
    choice = choice.title()

    # declare a variable called found and assign False to it
    found = False
    # using a for loop to iterate through the city
    for row in city:
        # using if statement to check if choice is in row
        if choice in row:
            # assign True to found
            found = True
            # declare a variable called city_num and assign the integer of the input function
            city_num = int(input("Enter the number of nights you want to stay in the hotel: "))
            # declare a variable called rental_num and assign the integer of the input function
            rental_num = int(input("Enter the number of days you want to rent a car: "))
            # call the holiday_cost function with city_num, choice and rental_num as the arguments
            holiday_cost(city_num, choice, rental_num)
            # break out of the loop
            break
    # using if statement to check if found is False  
    if not found:
        # print city not found in the list
        print("City not found in the list")
        # call the store_input function
        store_input()

print("Check your total holiday cost")
print("1. Continue")
print("2. Exit")
 # declare a variable called user_input and assign the input function
user_input = input("Enter your choice between 1 and 2 :")
# using if statement to check if user_input is 1
if user_input == "1":
    # call the store_input function
    store_input()
# using else if statement to check if user_input is 2
else:
    # exit the program
    sys.exit()
    # print goodbye
    print("Goodbye")


