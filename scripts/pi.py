# lol funny file name

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

print orbitEquiv((3, 0, 0), (1, 0, 0))


    # (zero_c, one_c, two_c) = cur_f
    # (zero_o, one_o, two_o) = orig_f
    # if (zero_o > 0 and zero_c % zero_o == 0):
    #     factor_zero = zero_c / zero_o
    # if (one_o > 0 and one_c % one_o == 0):
    #     factor_one = one_c / one_o
    # if (two_o > 0 and two_c % two_o == 0):
    #     factor_two = two_c / two_o
    # if (factor_zero == factor_one == factor_two):
    #     return True
    # return False

def orbitRepresentative(f):
    (z, o, t) = f
    if (z % 2 == 1 and o % 2 == 1 and t % 2 == 1):
        pass
    # TODO

def residual((z, o, t), b):
    if b == 0: return (o, t, z)
    else: return (o, t + z, 0)

def componentWiseAdd(a, b):
    # print "asdf"
    # print zip(a, b)
    return tuple(sum(elt) for elt in zip(a, b))

# on input all 0's
def a32_pi(s):
    # (zero, one, two) = (1, 0, 0)
    f = (1, 0, 0)
    orig_f = f
    # runs = 20
    for i in range(len(s)):
        bit = s[i]
        print f
        # print pebbleSetup(f)
        # step
        if (f[0] % 2 == 0):
            # even
            f = residual(f, bit) # depends on bit
        else:
            f = componentWiseAdd(residual(f, 0), residual(f, 1))
        f = shrink(f)
        if orbitEquiv(f, orig_f):
            f = orig_f


# TODO need to look into equivalence classes for orbit equivalence
# coprime to length of orbit

# a32_pi(str2intlist("00000000000000000000000000000000000000000000"))
