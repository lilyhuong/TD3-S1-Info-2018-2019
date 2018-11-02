def Func():
    print ("g(x,y)= 1 / (x * x) + (1/(y * y)")
    x = int(input("Entre votre value de x: "))
    y  = int(input("Entre votre value de y: "))
    g = 1 / (x * x) + (1 / (y * y))
    return g
print (Func())