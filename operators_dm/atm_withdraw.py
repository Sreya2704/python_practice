#ATM Withdrawal System
balance = 10000
amount = int(input("Enter amount: "))

if amount % 100 != 0:
    print("Enter amount in multiples of 100")
elif amount > balance:
    print("Insufficient balance")
else:
    balance -= amount
    print("Transaction successful")
    print("Remaining balance:", balance)