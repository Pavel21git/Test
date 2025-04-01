import math

a = float(input("Enter a: "))
b = float(input("Enter b: "))
x = float(input("Enter x: "))

y_1 = (a**2 / 3) + (a**2 / b) + math.sqrt(a**2 + 4) / 4 + math.sqrt(a**2 + 64)
y_2 = math.cos(x) + math.sin(x)
y_3 = (math.cos(x**2))**2 + math.sin(2 * x - 1)
y_4 = 5*x + 3*x**2 * math.sqrt(1 + (math.sin(x))**2)

print("\nResults:")
print("Formula (a) result:", y_1)
print("Formula (b) result:", y_2)
print("Formula (c) result:", y_3)
print("Formula (d) result:", y_4)
