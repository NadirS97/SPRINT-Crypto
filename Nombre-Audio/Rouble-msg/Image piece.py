import sys
from itertools import islice

sys import argv
## RECUPERER GRACE AU DECODE64 DU MESSAGE CRYPTER QU ON A TROUVE A L INTERIEURE DE L IMAGE DES ROUBLES AVEC UN BLOC NOTE

class lfsr:
    """
    LFSR en mode Fibonacci
    cf https://fr.wikipedia.org/wiki/Registre_à_décalage_à_rétroaction_linéaire
    """
    def __init__(self, n, *taps):
        "initialise un registre de longueur [n] avec bits de retour [taps]"
        self.n = n - 1
        self.taps = taps
        self.state = 0

    def seed(self, s):
        "initalise le contenu du registre"
        self.state = s & ((1 << self.n) - 1)

    def onebit(self):
        "génère le bit suivant"
        b = self.state & 1
        nb = b
        for x in self.taps:
            nb ^= (self.state >> x) & 1
        self.state = (self.state >> 1) | (nb << self.n)
        return b

def digits(l):
    "générateur équitable d'entiers"
    m=0
    while True:
        n=0
        for i in range(5):
            n = (n << 1) | l.onebit()
        if n<30:
            yield (n%10)
            m=0
        else:
            m+=1
            if m==100:
                raise ValueError("stucked")

if __name__ == '__main__':
    if len(argv) < 5:
        print(f"usage: {argv[0]} how_many_digits seed regsize tap1 tap2 ... tapN")
        exit(1)
    nargs=[int(x) for x in  argv[1:]]
    x=lfsr(nargs[2], *nargs[3:])
    x.seed(nargs[1])
    l=[]
    c=''
    for d in islice(digits(x), nargs[0]):
        c+=str(d)
        if len(c)==5:
            l.append(c)
            c=''
    print(' '.join(l))