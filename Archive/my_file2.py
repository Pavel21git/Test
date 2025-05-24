

s = float(input("Enter loan amount (s): "))
i = float(input("Enter annual interest rate (i) in %: "))
n = int(input("Enter loan term in months (n): "))

p = i / 12 / 100
m = (s * p * (1 + p) ** n) / ((1 + p) ** n - 1)

total_payment = m * n
overpayment = total_payment - s

print("\nResults:")
print(f"Monthly payment: {m:.2f}")
print(f"Total payment to bank: {total_payment:.2f}")
print(f"Overpayment: {overpayment:.2f}")
