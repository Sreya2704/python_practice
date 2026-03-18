"""Write a function that checks whether two variables refer to the same object."""

def check_identity(a, b):

    result = False

    # logic
    result=a is b
    return result
print(check_identity(5,5))