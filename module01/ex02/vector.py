class Vector:
    def __init__(self, values):
        if isinstance(values, list):
            for value in values:
                 if not isinstance(value, list):
                     print("Parameters is not a list of list")
                     exit(1)
                 elif not isinstance(value[0], float):
                     print("It's not a list of lis of floats")
                     exit(1)
            print("Bonjour")
            exit(1)
        else:
            print("?")