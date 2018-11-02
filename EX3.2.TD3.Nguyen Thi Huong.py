def somecube(n):
    s = 0
    for k in range(1,n + 1):
        s += k ** 3
    return s
h = somecube(5)
print(h)