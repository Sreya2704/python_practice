"""
1. Reverse a String
Write a program to reverse a given string.
# Input: "hello"
# Output: "olleh"
"""
word=input("Enter s string:")
#print(word[::-1])

rev=""
for i in range(len(word)-1,-1,-1):
    rev=rev+word[i]
print(rev)