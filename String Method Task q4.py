import string

# Prompt the user to set a password that contains both letters and numbers
password = input("Please set a password that contains both letters and numbers: ")

# Check if the password meets the requirements using set operations
is_valid_password = set(password).isdisjoint(set(string.ascii_letters)) == False and set(password).isdisjoint(set(string.digits)) == False

# Print the password and a message indicating whether it is valid
print("Your password is:", password)
print("Valid password:", is_valid_password)
password