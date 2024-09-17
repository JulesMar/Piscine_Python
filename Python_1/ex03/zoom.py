from load_image import ft_load
from PIL import Image
import numpy as np
from matplotlib import pyplot


def zoom(arr_img: np.array, x: int, y: int, z: int):
    to_cutX = len(arr_img) - x
    to_cutY = len(arr_img[0]) - y
    startX = int(to_cutX / 2)
    startY = int(to_cutY / 2)
    if to_cutX % 2 != 0:
        startX += 1
    if to_cutY % 2 != 0:
        startY += 1
    arr_img = arr_img[startX:-int(to_cutX/2), startY:-int(to_cutY/2), :1]
    return arr_img


def main():
    arr_img = ft_load("animal.jpeg")
    print(arr_img)
    arr_img = zoom(arr_img, 400, 400, 1)
    print(f"New shape after slicing: ({len(arr_img)},\
 {len(arr_img[0])}, {len(arr_img[0][0])}) or (400, 400)")
    print(arr_img)
    pyplot.imshow(arr_img, cmap='gray')
    pyplot.show()


if __name__ == "__main__":
    main()
