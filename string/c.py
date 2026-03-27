"""
5. Count Words
Count number of words in a sentence.
# Input: "I love Python"
# Output: 3
"""
sentence = input("Enter a sentence: ")

words = sentence.split()
count = len(words)

print(count)