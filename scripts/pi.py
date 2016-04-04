# lol funny file name
import random
import fractions

# polyadic gcd
def gcd(*args):
    assert len(args) > 0
    if len(args) == 1: return args[0]
    g = fractions.gcd(args[0], args[1])
    for elt in args[2:]:
        g = fractions.gcd(g, elt)
    return g

def gocd(*args):
    # greatest odd common divisor
    g = gcd(*args)
    while g % 2 == 0:
        g /= 2
    return g

def str2intlist(s):
    result = []
    for c in s:
        result.append(int(c))
    return result

def pebbleSetup((z, o, t)):
    automaton = """
   %s
  / \\
 %s - %s
    """
    return automaton % (z, o, t)

def shrink((zero, one, two)):
    while two > 0:
        # print (zero, one, two), "asdf"
        if zero >= 2 and one >= 2:
            zero -= 2
            one -= 2
            two -= 1
        else:
            break
    return (zero, one, two)

def orbitEquiv(cur_f, orig_f):

    nonzero_cur_f = [(i, pebbles) for i, pebbles in enumerate(cur_f) if pebbles > 0]
    nonzero_orig_f = [(i, pebbles) for i, pebbles in enumerate(orig_f) if pebbles > 0]

    # need set of pebble positions to match
    if set([i for i, _ in nonzero_cur_f]) != set([j for j, _ in nonzero_orig_f]):
        return False

    # all nonzero pebbles in orig should divide corresponding nonzero pebbles in cur
    if not all(cur_pebbles % orig_pebbles == 0 for (cur_pebbles, orig_pebbles) in \
        zip([peb for _, peb in nonzero_cur_f],
            [peb for _, peb in nonzero_orig_f])):
        return False

    # need a unique common factor between everything
    if len(set(cur_pebbles / orig_pebbles for (cur_pebbles, orig_pebbles) in \
        zip([peb for _, peb in nonzero_cur_f],
            [peb for _, peb in nonzero_orig_f]))) > 1:
        return False

    return True

def orbitRepresentative(f):

    nonzero_f = [(i, pebbles) for i, pebbles in enumerate(f) if pebbles > 0]
    pebble_counts = [pebs for _, pebs in nonzero_f]
    nonzero_f = [(i, pebbles) for i, pebbles in enumerate(f) if pebbles > 0]

    if len(pebble_counts) < 1:
        return f

    g = gocd(*pebble_counts)
    return tuple(n / g for n in f)

def residual((z, o, t), b):
    if b == 0: return (o, t, z)
    else: return (o, t + z, 0)

def componentWiseAdd(a, b):
    return tuple(sum(elt) for elt in zip(a, b))

# on input all 0's
def a32_pi(s):
    f = (1, 0, 0)
    orig_f = f
    for i in range(len(s)):
        bit = s[i]
        print f
        # step
        if (f[0] % 2 == 0):
            # even
            f = residual(f, bit) # depends on bit
        else:
            f = componentWiseAdd(residual(f, 0), residual(f, 1))
        f = shrink(f)
        f = orbitRepresentative(f)
        if f == orig_f:
            print "quit on iteration %d" % i
            return


a32_pi([random.randint(0, 1) for _ in xrange(100)])
# a32_pi(str2intlist("000000000"))
