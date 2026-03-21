"""
Take an integer input.
Check if it is even or odd
Also check if it is divisible by 3 and 5
Print appropriate messages.
"""

num = int(input("Enter a number: "))


if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")


if num % 3 == 0 and num % 5 == 0:
    print("Divisible by both 3 and 5")
elif num % 3 == 0:
    print("Divisible by 3 only")
elif num % 5 == 0:
    print("Divisible by 5 only")
else:
    print("Not divisible by 3 or 5")