full_name = input("Please enter your full name along with your caste or father's name: ")
name_parts = full_name.split()
last_name = name_parts.pop()
first_name = " ".join(name_parts)
print("First Name: ", first_name)
print("Last Name: ", last_name)

full_name = input("Please enter your full name along with your caste or father's name: ")


name_parts = full_name.split()

last_name = name_parts[-1]


first_name = " ".join(name_parts[:-1])


print("First Name: ", first_name)
print("Last Name: ", last_name)
