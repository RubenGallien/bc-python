import numpy as np

class NumPyCreator:
    def from_list(self, lst):
        return np.array(lst)

    def from_tuple(self, tpl):
        return np.array(tpl)

    def from_iterable(self, itr):
        return np.fromiter(itr, int)

    def from_shape(self, shape, value=0):
        return np.full(shape, value)

    def random(self, shape):
        return np.random.rand(shape[0], shape[1])

    def identity(self, n):
        return np.identity(n)
