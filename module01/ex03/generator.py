import string

def txt_print(text):
    if not isinstance(text, str):
        raise SystemExit("Text is not a string")
    for c in text:
        if not c in string.printable:
            return 0
    return (1)

def generator(text, sep=" ", option=None):
    if not txt_print(text):
        raise SystemExit("Erreur dans la chaine text")
    lst = text.split(sep)

    for words in lst:
        yield words



for words in generator("Le Lorem Ipsum est simplement du faux texte.", sep=" "):
    print(words)