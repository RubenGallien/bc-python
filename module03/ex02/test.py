import numpy as np
from ScrapBooker import ScrapBooker

#[[ 0  1  2  3  4]
# [ 5  6  7  8  9]
# [10 11 12 13 14]
# [15 16 17 18 19]
# [20 21 22 23 24]]

#[[ 5]
# [10]
# [15]]

# spb = ScrapBooker()
# arr1 = np.arange(0,25).reshape(5,5)
# print(f"avant :\n {arr1}")


# L = [65, 31, 9, 32, 81, 82, 46, 12]
# print(L[::2])

# print(f"apres\n{spb.crop(arr1, (3, 1),(1,0))}")

arr2 = np.array("A B C D E F G H I".split() * 6).reshape(-1, 9)

spb = ScrapBooker()
print(spb.thin(arr2, 2, 0))