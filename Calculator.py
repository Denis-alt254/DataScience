# Take operators from the user

num1 = int(input("Enter num 1: "))
op = input("Enter operator: ")
num2 = int(input("Enter num 2: "))
result = 0

if (op == '*' ):
    result = num1 * num2
    print("Result: ", result)
elif (op == '/'):
    result = num1/num2
    print("Result: ", result)
elif (op == '+'):
    result = num1+num2
    print("Result: ", result)
elif(op == '-'):
    result = num1-num2
    print("Result: ", result)
else:
    print("Enter (*, /, -, +) operators only.")