#Calculator

number1 = int(input("Enter the 1st number: "))
number2 = int(input("Enter the 2nd number: "))
Action = str(input("Choose an action: add(+), sub(-), mult(*) or div(/), exp(**)"))

#Actions

print("Result for this calculation is: ")
if Action == "+":
    print(number1+number2)
elif Action == "-":
    print(number1-number2)
elif Action == "/":
    print(number1/number2)
elif Action == "**":
    print(number1**number2)
else:
    print(number1*number2)
