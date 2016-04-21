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

def even(f):
    return f[0] % 2 == 0

def groupEquivClass(f, n, m):
    orig_f = f
    f = list(f) # immutability is hard
    s = gcd(n, m)
    r = m / s
    # should be fine to process in this order,
    # it's all the identity anyway
    # so something something commutative
    for i in xrange(0, s):
        while (all(elt >= 1 for elt in f[m+i::s]) and f[m+i::s] and \
               all(elt >= 2 for elt in f[i:(r-1)*s+i+1:s]) and f[i:(r-1)*s+i+1:s]):
            # print f, f[i:(r-1)*s+i+1:s], f[m+i::s]
            for j in xrange(i, (r-1)*s+i+1, s):
                # print "minus two to j = ", j
                f[j] -= 2
            for k in xrange(m+i, len(f), s):
                # print "minus one to k = ", k
                f[k] -= 1
    # if (list(orig_f) != f): print orig_f, tuple(f)
    return tuple(f)

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

def residual(f, b, n, m):
    shifted = list(f[i] for i in xrange(1, len(f))) + [0]
    if even(f):
        # shift over, but send half to n-1 and half to m-1
        shifted[n-1] += f[0] / 2
        shifted[m-1] += f[0] / 2
    else:
        shifted[n-1] += f[0] / 2 + (b == 0)
        shifted[m-1] += f[0] / 2 + (b == 1)
    return tuple(shifted)

def canonicalResidual(f, b, n, m):
    return orbitRepresentative(groupEquivClass(residual(f, b, n, m), n, m))

def componentWiseAdd(a, b):
    return tuple(sum(elt) for elt in zip(a, b))

def dag2edgeList(t):
    edgeList = []
    def recurse(i):
        if i not in t: return
        if 2*i in t and 2*i in t:
            edgeList.append((t[i], t[2*i]))
            recurse(2*i)
        if 2*i+1 in t and 2*i + 1 in t:
            edgeList.append((t[i], t[2*i+1]))
            recurse(2*i+1)
    recurse(1)
    return edgeList

def tree2graphviz(t):
    edgeList = []
    def recurse(i):
        if i not in t: return
        if 2*i in t and 2*i in t:
            edgeList.append((t[i], t[2*i]))
            recurse(2*i)
        if 2*i+1 in t and 2*i + 1 in t:
            edgeList.append((t[i], t[2*i+1]))
            recurse(2*i+1)
    recurse(1)
    result = ["digraph G {"]
    for (u, v) in set(edgeList):
        result.append('"%s" -> "%s"' % (u, v))
    result.append("}")
    return "\n".join(result)

def residualTree(n, m, depth=22):
    f = tuple(0 + (i == 0) for i in xrange(n))
    orig_f = f
    dag = dict()
    nodes = set()
    def recurse(f, i):
        # i is index of cur node in tree
        if i >= 2**depth - 1: return
        dag[i] = f
        if even(f):
            recurse(canonicalResidual(f, 0, n , m), 2*i)
        else:
            # if odd, WLOG move left (TODO maybe make ternary?)
            child_f = orbitRepresentative(groupEquivClass(componentWiseAdd(
                canonicalResidual(f, 0, n, m),
                canonicalResidual(f, 1, n, m)), n, m))
            recurse(child_f, 2*i)
    recurse(f, 1)
    return dag

tree = residualTree(7, 5)
print tree2graphviz(tree)
