"""
Find Frequency of Each Character
# Input: "aabbc"
# Output: {'a':2, 'b':2, 'c':1}
"""
word = input("Enter a string: ")

freq = {}

for ch in word:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1

print(freq)