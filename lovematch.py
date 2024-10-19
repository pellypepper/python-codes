def calculator(first_input, second_input):
     count1 = 0
     count2 = 0
     count3 = 0
     count4 = 0
     total_score = 0
     love = ['l', 'o', 'v', 'e']
     vowels = ['a', 'e', 'i', 'o', 'u']
     consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
     
     # Check for the length of both input
     if len(first_input) == len(second_input):
         total_score += 20
     
     # Check for vowels and consonants in the first letters
  
     if first_input[0] in vowels and second_input[0] in vowels :
            total_score += 10 
     if first_input[0] in consonants and second_input[0] in consonants:
            total_score += 10

     # Count vowels both inputs
     for x in vowels:
       if x in first_input:
            count1 +=1
       if x in second_input:
            count2 +=1
     # Compare vowel  counts
     if count1 == count2:
        total_score += 12
    
     # Count consonants in both inputs 
     for x in consonants:
       
        if x in first_input:
            count3 +=1
        if x in second_input:
            count4 +=1
     # Compare  consonant counts
     if count3 == count4:
        total_score += 12


    # Check for love letters in both inputs 
     for x in love:
        found_in_first = False
        found_in_second = False
        if x in first_input:
            found_in_first = True
        if x in second_input:
           found_in_second = True
        if found_in_first == found_in_second:
            total_score += 7
            break


     if total_score < 30:
        return f"Your love score is {total_score}%. You are not compatible"
     if total_score <= 50:
        return f"Your love score is {total_score}%. You are can work on your relationship if yu both listen to each other"
     if total_score > 50:
        return f"Your love score is {total_score}%. You are compatible"
     if total_score > 70:
        return f"Your love score is {total_score}%. You can get married"
     
# Main program to take input and run the calculator
print(f"{'-'*40}")
print("LOVE MATCH CALCULATOR")
print(f"{'-'*40}")

while True:
    first_input = input("Enter Lover 1 first name: ").lower()
    second_input = input("Enter Lover 2 first name: ").lower()

    # Check if any of the inputs contain digits
    if any(char.isdigit() for char in first_input) or any(char.isdigit() for char in second_input):
        print("Please enter valid names (letters only).")
    else:
        # Break the loop if inputs are valid (no digits)
        break

# Call the calculator function after valid inputs are entered
result = calculator(first_input, second_input)
print(result)