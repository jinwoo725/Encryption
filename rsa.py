from miller_rabin import miller_rabin
from secrets import randbelow

class Rsa:

    def keygen(self, size = 1536):
        if size < 1024: return -1

        while True:
            p = self._prmgen(size - 1)
            q = self._prmgen(size - 1)

            if p == q: continue

            n = p * q
            qn = (p - 1) * (q - 1)
            e = 65537

            if self._gcd(e, qn): continue

            d = pow(e, -1, qn)

            e1 = d % (p - 1)
            e2 = d % (q - 1)
            c = pow(q, -1, p)

            return p, q, n, e, qn, d, e1, e2, c

    def _prmgen(self, size):
        r = 2 ** size + randbelow(2 ** size)
        if r % 2 == 0: r += 1
        while True:
            if miller_rabin(r): return r
            r += 2

    def _gcd(self, e, qn):
        while True:
            e, qn = qn, e % qn
            match qn:
                case 0:
                    return 1
                case 1:
                    return 0