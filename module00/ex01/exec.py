import sys

ln = len(sys.argv)
txt = None
if (ln > 1):
    for x in range(1, ln):
        str = sys.argv[x]
        if txt is None:
            txt = str
        else:
            txt += str
        txt = txt + ' '
txt = txt.swapcase()
txt = txt[::-1]
print(txt)