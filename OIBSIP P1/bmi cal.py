print("------------BMI CALCULATOR--------")
name=input("enter your name")
w=int(input("enter your body weight in pounds"))
h=int(input("enter your height in inches"))
bmi=(w*703)/(h*h)
print(bmi)
if bmi>0:
    if(bmi<18.5):
        print(name+",you are under weight")
    elif(bmi<=24.9):
        print(name+",you are normal weight")
    elif(bmi<=25):
        print(name+",you are over weight")
    elif(bmi<=34.9):
        print(name+",you are obese")
    elif(bmi<=39.9):
        print(name+",you are severely obese")
    elif(bmi<=40):
        print(name+",you are morbidly obese")
else:
    print("enter a valid data")
print("---------------------------------------")