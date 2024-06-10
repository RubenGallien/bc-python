import sys
ln = len(sys.argv)

if ln > 2:
    print("error")
elif ln > 1:
    if str.isdigit(sys.argv[1]):
        nb = int(sys.argv[1])
    if ln == 0:
        print("I'm zero")
    elif nb % 2:
        print("I'm Odd")
    else:
        print("I'm even")
