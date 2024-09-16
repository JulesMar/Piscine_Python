def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
    """
give_bmi(height: list[int | float],
         weight: list[int | float]) -> list[int | float]

Give a list of BMI calculate from the list of height and weight.

Args:
    height (list[int | float]): The list of height
    weight (list[int | float]): The list of weight

Returns:
    ret (list[int | float]): BMI values
    """
    if type(height) is not list or type(weight) is not list:
        print("not list")
        return 0
    if len(height) != len(weight):
        print("not same len")
        return 0
    if not all(isinstance(elem, (int, float)) for elem in height):
        print("not int or float in height")
        return 0
    if not all(isinstance(elem, (int, float)) for elem in weight):
        print("not int or float in weight")
        return 0
    ret = []
    for x, y in zip(height, weight):
        ret.append(y / pow(x, 2))
    return ret


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
apply_limit(bmi: list[int | float], limit: int) -> list[bool]

Give a list of boolean if the BMI value is above the limit.

Args:
    bmi (list[int | float]): The list of BMI value
    limit (int): The limit

Returns:
    ret (list[bool]): List of boolean value if above the limit
    """
    if type(bmi) is not list or type(limit) is not int:
        print("wrong type")
        return 0
    if not all(isinstance(elem, (int, float)) for elem in bmi):
        print("not int or float in bmi")
        return 0
    ret = []
    for elem in bmi:
        ret.append(elem > limit)
    return ret
