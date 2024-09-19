from PIL import Image
import numpy as np


def ft_load(path: str) -> np.array:
    if path is None:
        print("No path given")
        exit()
    extension = (".jpg", "jpeg")
    if not path.endswith(extension):
        print("Wrong extension file please give .jpg or .jpeg")
        exit()
    try:
        im = Image.open(path)
    except Exception:
        print("Opening image failed")
        exit()
    im.show()
    pix = im.load()
    print(f"The shape of image is: ({im.size[1]},\
 {im.size[0]}, {len(pix[0,0])})")
    arr = np.array(im)
    print(arr)
    return arr
