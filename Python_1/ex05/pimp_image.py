import numpy as np
from PIL import Image


def ft_invert(array) -> np.array:
    """
Inverts the color of the image received.
    """
    invert = array.copy()
    invert[:, :, :] = 255 - invert[:, :, :]
    im = Image.fromarray(invert)
    im.show()
    return invert


def ft_red(array) -> np.array:
    """
Remove the color other than red of the image received.
    """
    red = array.copy()
    red[:, :, [1, 2]] = 0
    im = Image.fromarray(red)
    im.show()
    return red


def ft_green(array) -> np.array:
    """
Remove the color other than green of the image received.
    """
    green = array.copy()
    green[:, :, [0, 2]] = 0
    im = Image.fromarray(green)
    im.show()
    return green


def ft_blue(array) -> np.array:
    """
Remove the color other than blue of the image received.
    """
    blue = array.copy()
    blue[:, :, [0, 1]] = 0
    im = Image.fromarray(blue)
    im.show()
    return blue


def ft_grey(array) -> np.array:
    """
Remove the color of the image received.
    """
    grey = array.copy()
    grey = grey[:, :, 1]
    im = Image.fromarray(grey)
    im.show()
    return grey
