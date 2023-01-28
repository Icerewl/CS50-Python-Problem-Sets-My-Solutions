calculation = input("Expression: ")

a,b,c = calculation.split(" ")

a1 = float(a)
c1 = float(c)

if c1 == 0:
    print("You cant divide by 0, welllp...")
elif b == "+":
    example1 = a1 + c1
elif b == "-":
    example1 = a1 - c1
elif b == "/":
    example1 = a1 / c1
elif b == "*":
    example1 = a1 * c1

print(example1)