"""A number is a Duck Number if it contains 0,
but should not start with 0
Examples:
1023 → Duck number
0123 → Not allowed (starts with 0)
123 →  No zero"""

num = input("Enter number: ")

if num[0] == '0':
    print("Not a Duck Number")
elif '0' in num:
    print("Duck Number")
else:
    print("Not a Duck Number")