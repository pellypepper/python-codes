""" 
this a  program that register student for exam and store them in a file reg_form.txt
the program takes in the numbers of student to register and ask the user to enter the student ID number of each student
the program then store the student ID number in a file reg_form.txt

"""

print("Welcome to the Student Register Program")
print("Please enter the number of students you would like to register")
num_input = int(input()) #take in the number of student to register
total_students = []

#iterate through the number of student to register
for i in range(num_input):
    print("Please enter the student's ID number : " )
    i = input("must not exceed 5 characters") 

    total_students.append(i) #append the student ID number to a list

    reg_form = open("reg_form.txt", "a")  # open the file in append mode
    reg_form.write(i + " " + "....." + "\n") #write the student ID number to the file
    reg_form.close() #close the file

 # open the file in read mode
form = open("reg_form.txt", "r")
form_read = form.readlines()

for x in form_read:
    x =x.strip() #strip the white space
    print(x)

form.close() #close the file