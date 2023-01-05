# BMI (Body-Mass Index) Calculator

import sys
name = input("Enter you name: ")
x=int(input("Enter the number corresponding the units which you want to use:\n1. Kg-cm\n2. lbs-ft\n3. kg-ft\n4. lbs-cm\n"))

if x==1:
    weight = float(input("Enter your weight in kg: "))
    height = float(input("Enter your height in cm: "))
    BMI = (weight)/((height/100)**2)
elif x==2:
    weight = float(input("Enter your weight in pounds: "))
    height = float(input("Enter your height in feet: "))
    BMI = (weight*703) / ((height * 12) ** 2)
elif x==3:
    weight = float(input("Enter your weight in kg: "))
    height = float(input("Enter your height in feet: "))
    BMI = (weight) / ((height /3.281) ** 2)
elif x==4:
    weight = float(input("Enter your weight in pounds: "))
    height = float(input("Enter your height in cm: "))
    BMI = (weight * 703) / ((height / 2.54 ) ** 2)
else:
    sys.exit("Invalid input, program terminated.")

print("BMI = "+"%.2f"%BMI)  #formatting the output upto 2 decimal places

if BMI>0:
    if(BMI<18.5):
        print(name +", you are underweight.")
    elif (BMI<=24.9):
        print(name +", you are normal weight.")
    elif (BMI<29.9):
        print(name +", you are overweight. You need to exercise more and stop sitting")
    elif (BMI<34.9):
        print(name +", you are obese.")
    elif (BMI<39.9):
        print(name +", you are severely obese.")
    else:
        print(name +", you are morbidly obese.")
else:
    print("Enter valid input")