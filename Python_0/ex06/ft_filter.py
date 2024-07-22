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
