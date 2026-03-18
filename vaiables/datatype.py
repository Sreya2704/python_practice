"""Write a function that checks if the given value is integer, string, float, or boolean."""

def check_datatype(value):

    result = None

    # logic
    a=type(value)
    if a == int:
        result="integer"
    elif a==str:
        result="string"
    elif a==float:
        result="float"
    elif a==bool:
        result="boolean"

    return result
check_datatype(10)
check_datatype("Man")
check_datatype(10.5)
check_datatype(True)
