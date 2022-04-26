expression = input("Enter an expression: ").split(" ")

if expression[1] == "+":
    print(str(float(expression[0]) + float(expression[2])))
elif expression[1] == "-":
    print(str(float(expression[0]) - float(expression[2])))
elif expression[1] == "*":
    print(str(float(expression[0]) * float(expression[2])))
elif expression[1] == "/":
    print(str(float(expression[0]) / float(expression[2])))
else:
    print("Invalid operator")
