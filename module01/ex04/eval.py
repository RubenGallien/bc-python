class Evaluator:
    def __init__(self, coefs, words):
        if not isinstance(coefs, list) or not isinstance(words,list):
            return -1
        if len(coefs) != len (words):
            return -1
        self.coefs = coefs
        self.words = words

    def zip_evaluate(coefs, words):
        if not isinstance(coefs, list) or not isinstance(words,list):
            return -1
        if len(coefs) != len (words):
            return -1
        result = 0.0
        for i in zip(coefs, words):
            result += i[0] * len(i[1])
        print(result)

    def enumerate_evaluate(coefs, words):
        if not isinstance(coefs, list) or not isinstance(words,list):
            return -1
        if len(coefs) != len (words):
            return -1
        result = 0.0
        for _, (coef, word) in enumerate(zip(coefs, words)):
            result += coef * len(word)
        print(result)