"""take a password input and check:
Length ≥ 8
Contains at least one digit
If both conditions satisfy → print "Strong Password"
Else → "Weak Password"."""

password = input("Enter password: ")

has_digit = False

for ch in password:
    if ch.isdigit():
        has_digit = True

if len(password) >= 8 and has_digit:
    print("Strong Password")
else:
    print("Weak Password")