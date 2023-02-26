name = input("What is your good name? ")
print("Hello," +name , "! I hope you are fine. Let me know how I can help you!".format(name=name))
response = input("Do you need any help? ")
print(input() == response)
problem = input("Please share your problem with us.") \
    if response.lower() == "yes" else None
print("Thanks for your feedback. We will resolve your problem.") \
    if problem else print("Okay! Good to see you, stay connected!")
