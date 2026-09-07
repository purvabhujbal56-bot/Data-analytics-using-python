import re

password = input("Enter your password: ")

if (len(password) >= 8 and
    re.search("[A-Z]", password) and
    re.search("[a-z]", password) and
    re.search("[0-9]", password) and
    re.search("[@#$%&*!]", password)):

    print("Valid Password")
else:
    print("Invalid Password")
    print("Password must contain:")
    print("- At least 8 characters")
    print("- At least one uppercase letter")
    print("- At least one lowercase letter")
    print("- At least one digit")
    print("- At least one special character (@#$%&*!)")