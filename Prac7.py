import re
password = input("Enter Password: ")
pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'
if re.match(pattern, password):
    print("Valid Password")
else:
    print("Invalid Password")
    print("Password must contain:")
    print("- Minimum 8 characters")
    print("- At least one uppercase letter")
    print("- At least one lowercase letter")
    print("- At least one digit")
    print("- At least one special character (@$!%*?&)")