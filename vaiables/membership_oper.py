"""Write a function that checks whether a given element exists in a list."""

def check_membership(data, element):

    result = False
    result=element in data

    # logic
    # for el in data:
    #     if element == el:
    #         result=True
    return result
print(check_membership(["cat","art","mat","eat","lock"],"arts"))
#print(check_membership("camel","m"))