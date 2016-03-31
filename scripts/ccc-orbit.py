import sys

"""
Flip. If was a zero, skip two. Else skip one.

Facts:
* ith gets flipped every other time (i-2) and (i-3) get flipped
* Let $c$ be the array of counts - that is, $c[i]$ is the number of times
  x[i] is flipped.
  Then, if we assume that x[i-3] = 0 and x[i-2] = 1, then we have

    c[i] = ceil(c[i-3]/2) + ceil(c[i-2]/2)

  In general,

    c[i] = FC(c[i-3]/2) + FC'(c[i-2]/2)

  where

    FC = ceil if x[i-3] = 0 and floor otherwise
    FC' = ceil if x[i-2] = 1 and floor otherwise

  Alternatively,

    c[i] = floor(c[i-3]/2) + (parity[i-3] * (1 - x[i-3]))
         + floor(c[i-2]/2) + (parity[i-2] * (x[i-2]))

  where parity[i] = c[i] % 2 = x[i] ^ y[i] for all i.

"""

def binStrings(start, stop):
    yield ""
    i = start
    while i < stop - 1:
        yield bin(i)[2:]
        i += 1

def importantBinStrings(start, stop):
    i = start
    while i < stop:
        yield "1" + ("0" * i)
        i += 1

printf = sys.stdout.write

def ccc(n, m):
    # n > m
    def automata(s):
        idx = 0
        result = list(s)
        while idx < len(s):
            printf(str(idx))
            if s[idx] == '0':
                result[idx] = 1
                idx += n
                printf(" " * (n-1))
            else:
                result[idx] = 0
                idx += m
                printf(" " * (m-1))
        printf("\n")
        return "".join([str(elt) for elt in result])
    return automata

def orbit(f, s):
    result = [s]
    cur = f(s)
    while cur != s:
        result.append(cur)
        cur = f(cur)
    return result

def inOrbitBad(f, x, y):
    return y in orbit(f, x)

# def simpleResidual(f, c):
#     if f == 0 and c == "0": return 2
#     if f == 0 and c == "1": return 1
#     if f == 2: return 1
#     if f == 1: return 0

def residual(h, a):
    (u, v) = h
    if (u % 2 == 0): return (v-u, -u/2)
    if a == "0": return (v-u-1, int((-3.0-u) / 2))
    if a == "1": return (v-u+1, int((3.0-u) / 2))

def residualsOverString(h, s):
    result = []
    for c in s:
        result.append(c if not h[0] % 2 else str(1 - int(c)))
        h = residual(h, c)
        print h
    print "".join(result)

def inOrbit(x, y):
    # assumes f is 0
    (h1, h2) = (0, 0)
    n = len(x) / 2
    tBits = []
    for r in xrange(n):
        nextBit = h2

def strXor(a, b):
    result = [0 for _ in xrange(len(a))]
    idx = 0
    for (x, y) in zip(a, b):
        result[idx] = (int(x) + int(y)) % 2
        idx += 1
    return "".join([str(elt) for elt in result])

def main():
    f = ccc(3, 2)
    s = "100000000"
    idx = 0
    h = (1,0)
    # print residual(h, "1")
    # print residual(h, "0")
    print residualsOverString(h, "1111")
    # print residual((101, 0), "1")


if __name__ == "__main__":
    main()

