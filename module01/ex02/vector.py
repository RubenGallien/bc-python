class Vector:

    def __init__(self, values):
        if not values:
            raise SystemExit("Need values for the object")
        elif isinstance(values, list):
            for value in values:
                 if not isinstance(value, list):
                     print("Parameters is not a list of list")
                     exit(1)
                 elif not isinstance(value[0], float):
                     print("It's not a list of lis of floats")
                     exit(1)
            self.values = values
        elif isinstance(values, int):
            self.values = [[float(i)] for i in range (values)]
        elif isinstance(values, tuple) and len(values) == 2 and values[0] < values[1]:
            self.values = [[float(i)] for i  in range(values[0], values[1])]
            print(self.values)
        else:
            raise SystemExit("Incorrect arg")

        self.shape = self.create_shape(self.values)

    def create_shape(self, values):
        if isinstance(values, list):
            if len(values) == 1 and isinstance(values[0], list):
                values = values[0]
            if all(isinstance(el, list) and len(el) == 1 for el in values):
                return (len(values), 1)
            elif all(not isinstance(el, list) for el in values):
                return (1, len(values))
        else:
            raise SystemExit("Error")

    def dot(self, vecteur):
        result = 0.0
        if isinstance(vecteur, Vector):
            if (self.shape == vecteur.shape):
                for i in range(len(self.values[0])):
                    result += self.values[0][i] * vecteur.values[0][i]
                return result
            else:
                raise SystemExit("Shapes are not the same")
        raise SystemExit("Arguments is not a vector")