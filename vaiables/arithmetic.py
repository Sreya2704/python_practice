"""Write a function that returns the sum, product, and remainder of two numbers."""

def arithmetic_ops(a, b):

    #result = None

    # logic
    total=a+b

    product=a*b
    

    remainder=a%b
    result=(total,product,remainder)
    return result
print(arithmetic_ops(10,5))
