def mer(a, b):
    ai, bi = 0, 0
    l = []

    while ai < len(a) and bi < len(b):
        if a[ai] < b[bi]:
            l += [a[ai]]
            ai += 1
        else:
            l += [b[bi]]
            bi += 1

    if ai == len(a):
        l += b[bi:]
    elif bi == len(b):
        l += a[ai:]

    return l
