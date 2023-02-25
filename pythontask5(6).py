#Area of a trapezoid

#The formula used in this program are Area = (1/2) * (a + b) * h where a and b are the 2 bases of trapezium & h is the height.

a = eval(input("Please Enter base values"))
b = eval(input("Please Enter second base values "))

h = eval(input("Please Enter the height values "))

trapezoid = 0.5 * (a+b) * h
print("Your area is trapezoid is ", trapezoid)

#Area of a parallelogram
base = eval(input("Please Enter the base values"))
height = eval(input("Please Enter the height values "))

parallelogram = base * height
print("The area in the parallelogram is :" , parallelogram)

# Calculate surface volume and area of a cylinder.
radius = eval(input("Please Enter the radius of cylinder "))
heightcy = eval(input("Please Enter the height of cylinder"))

surfacearea = 2 * (22 / 7) * radius * (radius + heightcy)
volumecylinder= (22 / 7) * radius * radius * heightcy

print("The surface area of cylinder is " , surfacearea)
print("The volume of the cylinder is " , volumecylinder)