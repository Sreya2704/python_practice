"""Write a function that checks which number is greater and return the greater number."""

def greater_number(a, b):

    result = None

    # logic
    if a>b:
        result=a
    else:result=b

    return result
print(greater_number(10,5))
print(greater_number(10,50))