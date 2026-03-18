"""
Take a string input. Count: Number of digits Number of alphabets Print both counts. Example: Input: a1b2c3 Alphabets: 3 Digits: 3
"""

text = input("Enter a string: ")

digit_count = 0
alpha_count = 0

for ch in text:
    if ch.isdigit():
        digit_count += 1
    elif ch.isalpha():
        alpha_count += 1

print("Alphabets:", alpha_count)
print("Digits:", digit_count)