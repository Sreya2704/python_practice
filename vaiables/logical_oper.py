"""Write a function that returns True if a number is between 10 and 50."""

def check_range(num):

    result = False

    # logic
    if num>=10 and num<=50:
        result=True

    # for i in range(10,51):
    #     if num == i:
    #         result=True

    return result
print(check_range(15))
print(check_range(60))