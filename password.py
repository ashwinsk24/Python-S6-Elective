# Write a Python program to check the validity of a password given by the user.

import re

def check_password(password):
    # Check length
    if len(password) < 6:
        print("Password is too short. It must be at least 6 characters.")
        return False
    
    # Check for lowercase letters
    if not re.search("[a-z]", password):
        print("Password must contain at least one lowercase letter.")
        return False
    
    # Check for uppercase letters
    if not re.search("[A-Z]", password):
        print("Password must contain at least one uppercase letter.")
        return False
    
    # Check for digits
    if not re.search("[0-9]", password):
        print("Password must contain at least one digit.")
        return False
    
    # Check for special characters
    if not re.search("[$#@]", password):
        print("Password must contain at least one special character ($#@).")
        return False
    
    # If all criteria are met, password is valid
    print("Password is valid.")
    return True

password=input("Enter your password: ")
check_password(password)  



'''
python password.py     
Enter your password: ashwin
Password must contain at least one uppercase letter.

python password.py
Enter your password: Abc@123
Password is valid.
'''