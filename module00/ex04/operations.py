import sys

ln = len(sys.argv)
if ln != 3:
    print("2 numbers needed")
    exit()
if not sys.argv[1].isdigit() or not sys.argv[2].isdigit():
    print("one or two arg(s) is/are not number(s)")
    exit()
nb1 = int(sys.argv[1])
nb2 = int(sys.argv[2])
print("Sum:          %d" % (nb1 + nb2))
print("Difference:   %d" % (nb1 - nb2))
print("Product:      %d" % (nb1 * nb2))
if nb2 == 0:
    print("Quotient:     Can't divide by 0")
    print("Remainder:    Can't divide by 0")
    exit()
q, mod = divmod(nb1, nb2)
print("Quotient:     %d" % (nb1 / nb2))
print("Remainder:    %d" % mod)
