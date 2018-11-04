def Exercise31(n):
    output = 0
    k = 0
    for x in range (1, n + 1):
        k = x ** 2
        output = output + k
    return output
print(Exercise31(5))



