"""
Reverse Number & Check Palindrome Take an integer input. 
Reverse the number and check using a boolean variable: If same → True Else → False 
Example: 121 → True 123 → False
"""

num = int(input("Enter a number: "))

temp = num
rev = 0

while temp != 0:
    digit = temp % 10
    rev = rev * 10 + digit
    temp = temp // 10

is_palindrome = (num == rev)

print(is_palindrome)