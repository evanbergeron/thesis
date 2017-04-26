STR = lambda r : "".join([str(e) for e in r])

def noncom_simple(s, i):
    j = i
    s = list(int(e) for e in s)
    r = list(s)
    touched = []
    while i < len(s):
        if s[i] == 1:
            r[i] = 0
            touched.append(i)
            i += 1
            if i >= len(s):
                break
            if s[i] == 1:
                i += 2
            else:
                i += 1
        else:
            r[i] = 1
            touched.append(i)
            break
    if j: print "%s," % len(touched),
    return STR(r)

f = lambda s : noncom_simple(s, 0)
g = lambda s : noncom_simple(s, 1)
h = lambda s : g(f(s))

def orbit(f, s):
    orig_s = s
    result = []
    s = f(s)
    result.append(s)
    while s != orig_s:
        s = f(s)
        result.append(s)
    return result

EACH = "\n".join

for s in ["0" * i for i in xrange(24, 25)]:
    print "#####################"
    o = orbit(h, s)
    # print "s len:", len(s)
    # print "orbit len:", len(o)
    # print EACH(o)
