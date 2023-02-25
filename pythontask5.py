#Design a BMI system both in (US and Metric unit) .

height= int(input("Please Enter your hieght in Inches "))
weight= int(input("Please Enter your weight in lbs "))

bmi = weight/(height**2)*783

print(bmi)