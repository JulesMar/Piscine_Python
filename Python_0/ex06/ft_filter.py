def ft_filter(func, iterable):
    """
filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true.
    """
    res = []
    if func is None:
        for elem in iterable:
            if elem:
                res.append(elem)
    else:
        for elem in iterable:
            if func(elem):
                res.append(elem)
    return iter(res)


def sort(i):
    if i < 10:
        return True
    else:
        return False


def main():
    iter = [True, False, True, False, False, True, 1, 0, 9]
    print(list(filter(None, iter)))
    print(list(ft_filter(None, iter)))


if __name__ == "__main__":
    main()
