a = input()

x, op, y = a.split()

x = int(x)
y = int(y)

if op == "+":
    print(x + y)
elif op == "-":
    print(x - y)
elif op == "*":
    print(x * y)
elif op == "/":
    print(x / y)
elif op == "%":
    print(x % y)
elif op == "**":
    print(x ** y)
else:
    print("Invalid operator")