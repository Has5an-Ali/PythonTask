
email = input("Please enter your email address: ")

if email.endswith("@gmail.com"):
    print("Thank you for providing your email address.")
else:
    print("You are not providing an accurate email address.")



# Second method

email = input("Please enter your email address: ")


is_gmail = email.endswith("@gmail.com")


print("Thank you for providing your email address." * is_gmail or "You are not providing an accurate email address.")

