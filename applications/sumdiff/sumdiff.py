"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""

# q = set(range(1, 10))
# q = set(range(1, 200))
q = (1, 3, 4, 7, 12)


def f(x):
    return x * 4 + 6

ht = {}
matched = []

# a + b = b + a,
# so only check unique combinations
curr = set(q)
while len(curr) > 0:
    a = curr.pop()
    for b in curr:
        target = f(a) + f(b)
        if target in ht:
            ht[target].append((a,b))
        else:
            ht[target] = [(a,b)]

for c in q:
    for d in q:
        if c == d:
            continue
        target = f(c) - f(d)
        if target in ht:
            for (a,b) in ht[target]:
                matched.append((a,b,c,d))


for (a,b,c,d) in matched:
    left_col = f"f({a}) + f({b}) = f({c}) - f({d})"
    right_col = f"{f(a)} + {f(b)} = {f(c)} - {f(d)}"
    print(left_col + "\t" + right_col)
