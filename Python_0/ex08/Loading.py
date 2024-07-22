import os


def ft_tqdm(lst: range) -> None:
    """
ft_tqdm(lst: range) -> None

Print a loading bar

Args:
    lst (range): The range represent the percentage of the loading

Returns:
    None
    """
    tot = lst[-1] + 1
    for elem in lst:
        index = lst.index(elem) + 1
        barSize = os.get_terminal_size().columns - (34 + len(str(tot))
                                                    + len(str(index)))
        percent = int(index / tot * 100)
        filledBar = int(barSize * index // tot)
        bar = "█" * filledBar + " " * (barSize - filledBar)
        endLine = str(index) + "/" + str(tot)
        print('{:>3}%|'.format(percent) + bar + "| " + endLine, end='\r')
        yield elem
