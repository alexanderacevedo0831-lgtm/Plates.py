expr = input("Expression: ").strip()
x, y, z = expr.split(" ")

# convert numbers
x = float(x)
z = float(z)

# check operator and calculate
if y == "+":
    result = x + z
elif y == "-":
    result = x - z
elif y == "*":
    result = x * z
elif y == "/":
    result = x / z

# output formatted result
print(f"{result:.1f}")