"""
2. Count Vowels
Count how many vowels are in a string.
# Input: "programming"
# Output: 3
"""
word=input("Enter s string:").lower()
VOWELS="aeiou"
count=0
for ch in word:
    if ch in VOWELS:
        count+=1
print(count)