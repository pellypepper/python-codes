import sys
from tabulate import tabulate

"""
a program that calculates the total cost of a holiday trip
it stores the list of cities in a list and uses a dictionary to store the cost of each city
it calculates the total cost of the hotel stay, plane cost and car rental
it uses the tabulate module to display the list of cities in a table format

"""

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

def hotel_cost(city_num):
    """
    calculate the total cost of the hotel stay
    """

    costpernight = 20
    hotel_total = city_num * costpernight

    return hotel_total
   

def plane_cost(choice):
     """
     calculate the total cost of the plane cost
     """ 

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
   
     return city_cost.get(choice, 0)
        

def car_rental(rental_num):
    """
    calculate the total cost of the car rental
    """

    car_total = rental_num * 30
    return car_total

    
def holiday_cost(city_num, choice , rental_num):
    """
    calculate the total cost of the holiday
    """

    hotel = hotel_cost(city_num)
    plane = plane_cost(choice)
    car = car_rental(rental_num)

    print("The total cost of your hotel stay is : $",hotel)
    print("The total cost of your car rental is : $",car)
    print("The total cost of your plane cost is : $",plane)
  
    total_cost = hotel + plane + car

    print(f"The total cost of your holiday is :  ${total_cost:.2f}")
    return total_cost



def store_input ():
    """
    store the input of the user
    """  

    print(tabulate(city, headers=header, tablefmt="grid"))
    while True:
        choice = input("Enter the city of your choice: ").title()

        # Check if the selected city exists in the city list
        found = False
        for row in city:
            if choice in row:
                found = True
                city_num = int(input("Enter the number of nights you want to stay in the hotel: "))
                rental_num = int(input("Enter the number of days you want to rent a car: "))
                holiday_cost(city_num, choice, rental_num)
                return  # Exit the loop after successful input and calculation

        if not found:
            print("City not found in the list. Please try again.")



print("Check your total holiday cost")
print("1. Continue")
print("2. Exit")
user_input = input("Enter your choice between 1 and 2 :")
if user_input == "1":
    store_input()

else:
    print("Goodbye")
    sys.exit()
 
  
if __name__ == "__main__":
    import unittest

    class TestHolidayOperation(unittest.TestCase):

        def test_hotel_cost(self):
            self.city_value = 5
            

            result = hotel_cost(self.city_value)

            self.assertEqual(result, 100)
    
        def test_plane_cost(self):
            self.choice = "Texas"
            

            result = plane_cost(self.choice)

            self.assertEqual(result, 400)
        
        def test_car_rental(self):
            self.rental_value = 5

            result = car_rental(self.rental_value)
            self.assertEqual(result, 150)

        def test_holiday_cost(self):
            self.city_value = 5
            self.choice = "Texas"
            self.rental_value = 5

            result = holiday_cost(self.city_value, self.choice, self.rental_value)
            self.assertEqual(result, 650)


unittest.main()