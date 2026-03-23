correct_password = "python123"
attempts = 0

while attempts < 3:
    password = input("Enter password: ")
    
    if password == correct_password:
        print("Access Granted")
        break
    else:
        print("Wrong Password")
    
    attempts += 1

if attempts == 3:
    print("Access Denied")