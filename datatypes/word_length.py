"""Word Length Checker Take a string input. Print: Short word → length < 5 Medium word → 5–8 Long word → > 8"""

word = input("Enter a word: ")

length = len(word)

if length < 5:
    print("Short word")
elif length <= 8:
    print("Medium word")
else:
    print("Long word")