"""Student Pass/Fail System
Take marks (float).
Rules:
>= 90 → Grade A
>= 75 → Grade B
>= 50 → Pass
< 50 → Fail"""

marks = float(input("Enter marks: "))

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Pass")
else:
    print("Fail")