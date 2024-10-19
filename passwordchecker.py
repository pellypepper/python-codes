import string

print(f"{'*'*40}")
print("PASSWORD CHECKER")
print(f"{'*'*40}")
print(f"{'*'*40}")
print(f"{'*'*40}")


print("Enter your password to check if it is strong")
input_password = input("it must be at least 8 characters long: ")
total_score = 0
found_lower = False
found_upper = False
found_digit = False
found_alpha = False
found_punctuation = False 

try:
    # Loop through each character in the input_password
    for x in input_password: 
      if x.isdigit():
         found_digit = True
      if x.isalpha():
         found_alpha = True
      if x.islower():
        found_lower = True
      if x.isupper():
        found_upper = True
      if x in string.punctuation:
        found_punctuation = True

    # Check if both lower and upper case letters are present
    if found_lower and found_upper:
        total_score += 10
    elif found_lower == False or found_upper == False:
        raise ValueError("Password must contain both upper and lower case letters")
 
    # Check if both digits and alphabetic characters are present
    if found_digit and found_alpha:
            total_score += 10
    elif found_digit  == False or found_alpha == False:
            raise TypeError("Password must contain at least one digit")
    
    # Check for at least one punctuation sign
    if found_punctuation:
        total_score += 10
    else:
        raise ValueError("Password must contain at least one punctuation sign")

    # Check if password length is at least 8 characters
    if len(input_password) >= 8:
            total_score += 10
    else:
        raise ValueError("Password must be at least 8 characters long")
    
    if total_score < 20:
        print(f"Your password is weak ! Total score: {total_score}%.")
    if total_score > 20:
        print(f"Your password is strong ! Total score: {total_score}%.")
except (ValueError, TypeError) as e:
    print(str(e))
    

