import string
import sys


def c_upper(str):
    count = 0
    for x in str:
        if x in string.ascii_uppercase:
            count += 1
    return count


def c_lower(str):
    count = 0
    for x in str:
        if x in string.ascii_lowercase:
            count += 1
    return count


def c_isspace(str):
    count = 0
    for x in str:
        if x in string.whitespace:
            count += 1
    return count


def c_ponct(str):
    count = 0
    for c in str:
        if c in string.punctuation:
            count += 1
    return count


def text_analyzer(arg):
    """ This function counts the number of upper characters, lower characters,
        punctuation and spaces in a given text. """
    if arg is None:
        print("What is the text to analyze : ")
        arg = input()
    if type(arg) is not str:
        print("Erreur")
        exit()
    print("The text contains %d character(s):" % len(arg))
    print("- %d upper letter(s)" % c_upper(arg))
    print("- %d lower letter(s)" % c_lower(arg))
    print("- %d ponctuation mark(s)" % c_ponct(arg))
    print("- %d space(s)" % c_isspace(arg))


ln = len(sys.argv)
if ln is not 2:
    print("Erreur")
else:
    text_analyzer(sys.argv[1])
