def slice_me(family: list, start: int, end: int) -> list:
    if type(family) is not list:
        print("not good")
        return 0
    if not family or not all(len(elem) == len(family[0]) for elem in family):
        print("not good 2")
        return 0
    tmp = family.copy()
    print("My shape is : ({}, {})".format(len(tmp), len(tmp[0])))
    del tmp[0:start]
    del tmp[end:len(tmp)]
    print("My new shape is : ({}, {})".format(len(tmp), len(tmp[0])))
    return tmp
