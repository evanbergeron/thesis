var("m", "n", "o", "p", "q", "r")

a = matrix(SR, [[1, 0, 0], 
                [0, 1, 1], 
                [0, 0, 1]])

b = matrix(SR, [[1, 1, 0], 
                [0, 1, 0], 
                [0, 0, 1]])

c = matrix(SR, [[1, 0, 0], 
                [0, 1, -1], 
                [0, 0, 1]])

d = matrix(SR, [[1, -1, 0], 
                [0, 1, 0], 
                [0, 0, 1]])

e = matrix(SR, [[1, 0, 1], 
                [0, 1, 0], 
                [0, 0, 1]])

print e**7 * a ** 2 * b ** 6

# really just want. (x * y == z) for x, y, z in Z iff (these semigroups elements are equal to those semigroup elements)

'''
So let's start with 2 * 3 == 6

maybe instead of equal to the identity, we could do equal to the square of a thing?
'''

f = a**2
g = b**3
h = c**2
i = d**3
# print (f * g)
# print (h * i)
# print (f * g * c * d)
# print ((e**6).inverse() * (f * g)).inverse()


'''
we want
[1 3 0]     [1 0 6]
[0 1 2] M = [0 1 0]
[0 0 1]     [0 0 1]

which would just be...
'''

# print (f * g).solve_right(matrix([[1, 3, 6], [0, 1, 2], [0, 0, 1]]))

'''
so this looks like
[1 3 0]     [1 3 6]
[0 1 2] M = [0 1 2]
[0 0 1]     [0 0 1]

or rather

a**x * b**y * e**z = a**x * b**y * e**(x+y)

meh this just reduces to
e**(x+y) == e**z

ok but sure i can get natural number multiplication this way
how to encode the sign without using negatives in the matrix elements?

yah this is cool though. turns addition into multiplication
THIS DOESN"T WORK

maybe i could get something like
[1 6 6]
[0 1 6]
[0 0 1]

this would just be
'''

# print f * g
# print
# print (f * g).solve_right(matrix([[1, 6, 6], [0, 1, 6], [0, 0, 1]]))

ooo = matrix(SR, [[1, m, 0], 
                  [0, 1, 0], 
                  [0, 0, 1]])

ppp = matrix(SR, [[1, 0, 0], 
                  [0, 1, r], 
                  [0, 0, 1]])

# print ooo * ppp
# print e**4
# print ooo**3

'''
Ok, I think we can do this. I don't think we need to ever care about negative
multiplications ever. Integer solutions to Diophantine equations is equivalent
to natural number solutions (the proof is on wikipedia page for Hilbert's tenth).
And we don't need to check if P(x1..xn) = a, we can move all the negative coeffs 
over to the other side. So we're asking if P(x1..xn) == a + Q(x1..xn).

So we can build a systems of equations for each of these polynomials. It becomes
a bunch of additions and a bunch of multiplications, where everything is positive.

Then we can just use 
e = matrix(SR, [[1, 0, 1], 
                [0, 1, 0], 
                [0, 0, 1]])

and ask if e**(x+y) == e**z? Fuck, no. Not quite.
'''
# print e**(2 + 3)
# print (a ** 3) * (b ** 2) * (e ** 2)
