p = 28151


def generators(n):
    s = set(range(1, n))  # {1, 2, ..., n-1}
    results = []
    for a in s:
        g = set()  # {a, a^2, a^3, ...}
        for x in s:
            g.add(pow(a, x, n))
        if g == s:
            results.append(a)
    return results


print(generators(p))
