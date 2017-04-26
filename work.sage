import operator
import itertools
var("x", "y", "z", "r", "s", "t")
a = matrix(SR, [[1, 0, 0], 
                [0, 1, y], 
                [0, 0, 1]])

b = matrix(SR, [[1, x, 0], 
                [0, 1, 0], 
                [0, 0, 1]])

c = matrix(SR, [[1, 0, z], 
                [0, 1, 0], 
                [0, 0, 1]])

d = matrix(SR, [[1, 0, 0], 
                [0, 1, 0], 
                [0, r, 1]])

e = matrix(SR, [[1, 0, 0], 
                [s, 1, 0], 
                [0, 0, 1]])

f = matrix(SR, [[1, 0, 0], 
                [0, 1, 0], 
                [t, 0, 1]])

def allSymbolic(m):
    for row in m:
        for entry in row:
            if entry in {0,1}: return False
    return True

def symbolicOnlyInTopLeft(m):
    for i, row in enumerate(m):
        for j, entry in enumerate(row):
            if not i and not j and entry in {0, 1}: return False
            # if (i or j) and entry not in {0, 1}: return False
    return True

# wait, this is 6 items. So it's undecidable...
# But these are 6 specific matrices, not 6 general matrices.
# Like, these are fixed ahead of time. They aren't the input.
generators = [a, b, c, d, e, f]

def findMatrix(f):
    done = False
    length = 2
    # now we BFS over words in the generators
    while not done:
        for word in itertools.product(generators, repeat=length):
            m = reduce(operator.mul, word)
            if f(m):
                print m
                print length
                print m.rank()
                done = True
                # break
        length += 1


# print e.solve_right(matrix(SR, [[2, 0, 0], 
#                           [s, 1, 0], 
#                           [0, 0, 1]]))

print findMatrix(symbolicOnlyInTopLeft)
