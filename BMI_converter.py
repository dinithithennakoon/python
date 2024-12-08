name = input("Enter you're name: ")
weight = float(input("Enter weight in pounds: "))
height = float(input("Enter height in inches: "))

bmi = (weight * 703) / (height * height)
print(name + "Your BMI: ", bmi)


if bmi > 0:
    if bmi < 18.5:
        print(name ," You're Underweight")

    elif bmi <=24.9 :
         print(name,"You're Normal weight")
    elif bmi <=29.9 :
        print(name,"You're Overweight")
    elif bmi <= 34.9:
        print(name,"You're Obese")
    elif bmi <= 39.9 :
        print(name,"You're Severely Obese")
    else:
        print(name,"You're Morbidly Obese")
else:
    print("ERROR!")
