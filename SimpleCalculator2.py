number_1 = float(input("Enter first number: ")) 
number_2 = float(input("Enter second number: ")) 
op = input("Enter operator: ")
op == "/","+","*","-"

if op == "+":
    print(number_1, "+" ,number_2, "=" ,number_1 + number_2)
elif op == "/":
    print(number_1, "/" ,number_2, "=" ,number_1 / number_2)
elif op == "*":
    print(number_1, "*" ,number_2, "=" ,number_1 * number_2)
elif op == "-":
    print(number_1, "-" ,number_2, "=" ,number_1 - number_2)
else:
    print("Invalid Operator Detected")
