#Vowel or Consonant

ch = input("Enter a letter: ").lower()

if ch in "aeiou":
    print("Vowel")
elif ch.isalpha():
    print("Consonant")
else:
    print("Not an alphabet")