lst = [10, 25, 30, 41, 56]

even = 0
odd = 0

for num in lst:
    if num % 2 == 0:
        even += 1
    else:
        odd += 1

print("Even:", even)
print("Odd:", odd)