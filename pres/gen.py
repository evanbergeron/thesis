import sys
def a32(s):
    i = 0
    result = []
    nextFlip = 0
    # print nextFlip
    while i < len(s):
        if i == nextFlip:
            result.append(1 - s[i])
            nextFlip += 1 + (1 - s[i])
            # print nextFlip
        else:
            result.append(s[i])
        i += 1
    return result

# a32([1, 0, 1, 0])
# sys.exit(1)

start = [0 for _ in xrange(30)]
orbit = [start]
cur = a32(start)
# while cur != start:
for _ in xrange(int(round(len(start)*3.0/2))):
    orbit.append(cur)
    cur = a32(cur)

def toTikz(orbit):
    result = ["\\begin{center}\n\\begin{tikzpicture}[scale=0.2]"]
    row = len(orbit)
    for elt in orbit:
        this_row = []
        for col, bit in enumerate(elt):
            result.append("\\filldraw[fill=%s] (%d, %d) circle (%dem);" \
                % ("mDarkTeal" if bit else "mTan",
                   col, row, 1)
            )
        result.append("\n".join(this_row))
        row -= 1
    result.append("\\end{tikzpicture}\n\\end{center}")
    return "\n".join(result)

def simple(orbit):
    result = []
    for elt in orbit:
        result.append("".join([str(e) for e in elt]))
    return "\n".join(result)

print toTikz(orbit)
