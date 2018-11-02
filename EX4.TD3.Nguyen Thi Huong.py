def sometuple(array):
    output = 0
    for k in array:
        output += k
    return output
tuple = [2,3]
result = sometuple(tuple)
print("some =" , result)
tuple2 = [1,2,3]
result2 = sometuple(tuple2)
print("some = ", result2)
