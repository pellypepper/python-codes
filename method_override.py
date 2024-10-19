"""
this is a simple program that take user input 
and check if the use age is eligigle to drive a car
"""
import sys

#user should input their name, age, hair colour and eye colour
name_input = input("Enter your Name:  ")
age_input = input("Enter your Age (must be a number): ")
hair_colour_input = input("Enter your hair colour: ")
eye_colour_input = input("Enter your eye colour: ")


#throw error if user input doesnt match the required input
try:
    if name_input.isdigit():
        raise Exception("Name cannot be a number")
    
    if age_input.isalpha():
        raise Exception("Age cannot be a string")
     
except Exception as e:
    print(e)
    sys.exit()

#class for adult
class Adult:
    def __init__ (self, name_input, age_input, hair_colour_input, eye_colour_input):
        """
        this is the adlt constructor with its attributes
        """
        self.name = name_input
        self.age = age_input
        self.hair_colour = hair_colour_input
        self.eye_colour = eye_colour_input
    
    def can_drive(self):
        """
        this method print if the user is eligible to drive
        """
        print(f"{self.name} is old enough to drive")

class Child(Adult):
    def __init__(self, name_input, age_input, hair_colour_input, eye_colour_input):
        """
        this is the child class extended from the adult class
        """
        super().__init__(name_input, age_input, hair_colour_input, eye_colour_input)
    
    def can_drive(self):
        """
        this method print if the user is not eligible to drive
        """
        print(f"{self.name} is too young to drive")

age_input = int(age_input)

#chek if the user is above 18 or not
if age_input >= 18:
    person1 = Adult(name_input, age_input, hair_colour_input, eye_colour_input)
    #call the can_drive method
    person1.can_drive()
elif age_input < 18 :
    person1 = Child(name_input, age_input, hair_colour_input, eye_colour_input)
    #call the can_drive method
    person1.can_drive()