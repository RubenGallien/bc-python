import sys

ln = len(sys.argv)
if (ln > 1):
	txt = sys.argv[1][::-1]
	print(txt)