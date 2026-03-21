"""number is a Spy Number if:
sum of digits == product of digits
Example:
1124 → sum = 1+1+2+4 = 8
product = 1*1*2*4 = 8 """

num = int(input("Enter number: "))
temp = num

digit_sum = 0
digit_product = 1

while num > 0:
    ldigit = num % 10
    digit_sum += ldigit
    digit_product *= ldigit
    num //= 10

if digit_sum == digit_product:
    print("Spy Number")
else:
    print("Not a Spy Number")