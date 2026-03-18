"""
Take a username input.
Length must be at least 6
Must contain at least one digit
Must contain at least one alphabet
Print "Valid Username" or "Invalid Username".
"""
username=input("Enter name:")
has_digit=False
for ch in username:
    if ch.isdigit():
        has_digit = True
has_char=False
for ch in username:
    if ch.isalpha():
        has_char = True
if len(username)>=6 and  has_digit and has_char:
    print("Valid user")
else:print("Not valid")