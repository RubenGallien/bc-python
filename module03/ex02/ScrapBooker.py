import numpy as np

class ScrapBooker:
    def crop(self, array, dim, position=(0,0)):
        if not isinstance(array, np.ndarray):
            return None
        if not isinstance(dim, tuple) or not isinstance(position, tuple):
            return None
        if len(dim) != 2 and len(position) != 2:
            return None
        new_arr = array[dim[1]:dim[0] + 1, position[1]:position[0]]
        return new_arr

    def thin(self, array, n, axis):
        print(array)
        if n == 0:
            return array
        if axis == 0:
            sense = 1
        else:
            sense = 0
        stand = [i for i in range(array.shape[sense]) if i % n != n - 1]
        if sense == 0:
            new_arr = array[stand, 0]
        else:
            new_arr = array[0, stand]
        return new_arr

    def juxtapose(self, array, n, axis):
        