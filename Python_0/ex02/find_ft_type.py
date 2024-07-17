def all_thing_is_obj(object: any) -> int:
    if isinstance(object, (list, tuple, set, dict)):
        print(str(type(object))[8:-2].capitalize(), ":", type(object))
    elif type(object) is str:
        print(object, "is in the kitchen :", type(object))
    else:
        print("Type not found")
    return (42)
