"""Simple Interest Calculator Take: Principal (float) Rate (float) Time (int) Calculate: SI = (P × R × T) / 100"""


p = float(input("Enter Principal: "))
r = float(input("Enter Rate: "))
t = int(input("Enter Time: "))

si = (p * r * t) / 100

print("Simple Interest:", si)