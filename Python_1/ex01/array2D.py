def slice_me(family: list, start: int, end: int) -> list:
    if type(family) is not list:
        print("not good")
        return 0
    if not family or not all(len(elem) == len(family[0]) for elem in family):
        print("not good 2")
        return 0
    print("My shape is : ({}, {})".format(len(family), len(family[0])))
