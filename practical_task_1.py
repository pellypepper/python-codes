class Course:
    # Class attribute for the course name
    name = "Fundamentals of Computer Science"

    # Class attribute for the contact website
    contact_website = "www.hyperiondev.com"
    
    # Method to display contact details
    def contact_details(self):
        print("Please contact us by visiting", self.contact_website)
   
    def  head_office_location(self):
        print("Our head office is located in Cape Town")

# Example usage:
# Create an instance of the Course class
course = Course()

# Call the contact_details method to display contact information
course.contact_details()

# create a new class that inherits from the Course class
class OOPCourse(Course):
    def __init__(self, decription, trainer):
        """
        This is the constructor for the OOPCourse class and attributes
        """
        self.decription = " Object Oriented Programming"
        self.trainer = "John Doe"
    
    def trainer_details(self):
        """
        This method will print the trainer and the course description
        """
        print(f"qualified trainer {self.trainer} will be taking you through the course and the course is {self.decription}")
    
    def show_course_id(self):
        """
        This method will print the course id
        """
        print("The course id is #12345")

course_1 = OOPCourse("Object Oriented Programming", "John Doe")
course_1.trainer_details()
course_1.show_course_id()
course_1.contact_details()