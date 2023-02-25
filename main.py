"""Task 1
Design a calculator that takes 2 values from user to apply mathematical
operations Addition, subtraction, and division, multiplication, floor
division."""

num1 = eval(input("Please Enter Your First Number"))
print(num1)
num2 = eval(input("Please Enter Your Second Number"))

#for adding two value
print(num1+ num2) # Here we can do addition directly which is not good practice for user
#OR
print("The addition of the num1 & num2 is ", num1+num2)

# for Subtraction
print(num1 - num2)
#OR
print("The Subtraction of the num1 & num2 is ", num1 - num2)

#for division
print(num1/num2)
print("The addition of the num1 & num2 is ", num1/num2)

#for multiplication
print(num1*num2)
print("The Multiplication of the num1 & num2 is ", num1 * num2)
