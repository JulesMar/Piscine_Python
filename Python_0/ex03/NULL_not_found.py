def NULL_not_found(object: any) -> int:

    if object is None:
        print("Nothing: None", type(object))
        return 0
    elif object != object:
        print("Cheese: nan", type(object))
        return 0
    elif type(object) is int and object == 0:
        print("Zero: 0", type(object))
        return 0
    elif type(object) is str and len(object) == 0:
        print("Empty:", type(object))
        return 0
    elif type(object) is bool and object == False:
        print("Fake: False", type(object))
        return 0
    print("Type not found")
    return 1