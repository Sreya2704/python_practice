"""Take a single character input and check if it is:
Alphabet
Digit
Special character
Example:
A → Alphabet
7 → Digit
@ → Special Character"""

ch = input("Enter a character: ")

if ch.isalpha():
    print("Alphabet")
elif ch.isdigit():
    print("Digit")
else:
    print("Special Character")