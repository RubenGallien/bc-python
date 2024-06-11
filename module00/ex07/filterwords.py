import sys
import string

if len(sys.argv) == 3 and sys.argv[2].isdigit():
    result = []
    count = 0
    s_arg = sys.argv[1]
    s_arg = s_arg.translate(str.maketrans('','', string.punctuation))
    lst_w = s_arg.split()
    for w in lst_w:
        if len(w) > int(sys.argv[2]):
            result.append(w)
    print(result)
else:
    print("ERROR")
    exit()
