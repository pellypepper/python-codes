class Vehicle:
    def __init__ (self, make, model, year):
        """
        this is the vehicle constructor with its attributes
        """
        self.make = make
        self.model = model
        self.year = year
        self.available = True
    
    def get_details(self):
        """
        this method will print the vehicle details
        """
        return f"Vehicle Details: {self.year} {self.make} {self.model}"
    
    def rent(self):
        """
        this method will print the vehicle is available for rent
        """
        if self.available:
            self.available = False
            print("This vehicle is available for rent")
        else:
            print("Sorry, this vehicle is already rented")
    
    def calculate_rental_cost(self, days, base_rate=100):
        """
        this method will calculate the rental cost
        """
        try:      
            if  not isinstance(days, int):
                raise TypeError("Days must be an integer")
            if days <= 0:
                raise ValueError("Days must be greater than zero")
            return f"The rental cost for {days * base_rate} "
        except (TypeError, ValueError) as e:
             return str(e)
    

class Car(Vehicle):
    def __init__(self, make, model, year, doors):
         """
         this is the car constructor with its attributes
         """
         super().__init__(make, model, year)
         self.doors = doors
    
    def rent(self):
        """
        this method will print the car is available for rent
        """
        if self.available:
            self.available = False
            return f"Renting a car : {self.get_details()} with door {self.doors}"
        else:
            return "Sorry, this car is already rented"

    def calculate_rental_cost(self, days):
        return super().calculate_rental_cost(days, base_rate=200)
    

class Bike(Vehicle):
    def __init__(self, make, model, year, engine_size):
         """
         this is the bike constructor with its attributes
         """
         super().__init__(make, model, year)
         self.engine_size = engine_size
    
    def rent(self):
        """
        this method will print the bike is available for rent
        """
        if self.available:
            self.available = False
            return f"renting a bike : {self.get_details()} with engine size {self.engine_size}"
        else:
            return "Sorry, this bike is already rented"

    def calculate_rental_cost(self, days):
        return super().calculate_rental_cost(days, base_rate=50)
    

car = Car("FORD", "Fiesta", 2019, 4)
bike = Bike("Yamaha", "R1", 2020, 1000)
print(car.rent())
print(car.calculate_rental_cost(5))

print(bike.rent())  
print(bike.calculate_rental_cost(3))
