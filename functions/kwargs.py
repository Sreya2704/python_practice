def display_info(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)

display_info(name="Sreya", age=21, place="Kerala")