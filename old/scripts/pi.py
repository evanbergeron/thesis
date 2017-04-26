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
    if z % 2 == 0:
        return (o, t + z / 2, z / 2)
    if b == 0:
        return (o, t + z / 2, z / 2 + 1)
    return (o, t + z / 2 + 1, z / 2)
    # if b == 0: return (o, t, z)
    # else: return (o, t + z, 0)

def residualBig(f, b, n, m):
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
    return orbitRepresentative(shrink(residualBig(f, b, n, m)))
    # if b == 0: return orbitRepresentative(shrink((o, t, z)))
    # else: return orbitRepresentative(shrink((o, t + z, 0)))

def componentWiseAdd(a, b):
    return tuple(sum(elt) for elt in zip(a, b))

def even(f):
    return f[0] % 2 == 0

def a32_pi(s):
    f = (1, 0, 0)
    n, m = 3, 2
    orig_f = f
    for i in range(len(s)):
        bit = s[i]
        print f
        # step
        if even(f):
            # even
            f = residualBig(f, bit, n, m) # depends on bit
        else:
            f = componentWiseAdd(residualBig(f, 0, n, m), residualBig(f, 1, n, m))
        f = shrink(f)
        f = orbitRepresentative(f)
        if f == orig_f:
            print "quit on iteration %d" % i
            # print "".join([str(c) for c in s])
            return i

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

def residualTree(depth=22):
    f = (1, 0, 0, 0)
    orig_f = f
    n, m = 4, 3
    # tree = [None for _ in xrange(2**depth - 1)]
    dag = dict()
    nodes = set()
    def recurse(f, i):
        # i is index of cur node in tree
        if i >= 2**depth - 1: return
        # tree[i] = f
        dag[i] = f
        if even(f):
            # f = residual(f, bit) # depends on bit
            recurse(canonicalResidual(f, 0), 2*i, n, m)
            # recurse(canonicalResidual(f, 1), 2*i + 1)
        else:
            # if odd, WLOG move left (TODO maybe make ternary?)
            child_f = orbitRepresentative(shrink(componentWiseAdd(
                canonicalResidual(f, 0, n, m),
                canonicalResidual(f, 1, n, m))))
            recurse(child_f, 2*i)
    recurse(f, 1)
    return dag

# print residualTree()
# print set(residualTree().values())
print tree2graphviz(residualTree())

# max_iterations = 0
# for _ in xrange(100):
#     arg = [random.randint(0, 1) for _ in xrange(100)]
#     iters = a32_pi(arg)
#     max_iterations = max(max_iterations, iters)
# print max_iterations
