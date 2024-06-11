import sys

alphabet = dict(A='.-', B='-...', C='-.-.', D='-..', E='.', F='..-.', G='--.',
                H='....', I='..', J='.---', K='-.-', L='.-..', M='--', N='-.',
                O='---', P='.--.', Q='--.-', R='.-.', S='...', T='-', U='..-',
                V='...-', W='.--', X='-..-', Y='-.--', Z='--..')
alphabet.update({
    '0': '-----', '1': '.----',
    '2': '..---', '3': '...--',
    '4': '....-', '5': '.....',
    '6': '-....', '7': '--...',
    '8': '---..', '9': '----.',
})

if len(sys.argv) > 1:
    arg = ""
    res = ""
    i = 1
    while i < len(sys.argv):
        arg += sys.argv[i] + ' '
        i += 1
    arg = arg.strip().upper()
    for c in arg:
         if not c.isalnum() and not c.isspace() :
              print("ERROR")
              exit()
    for c in arg:
        if c.isspace():
            res += "/ "
        else:
            res += alphabet[c] + ' '
    print(res)

else:
    print("error")
    exit()