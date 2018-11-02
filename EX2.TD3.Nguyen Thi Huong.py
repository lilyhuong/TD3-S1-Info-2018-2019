def countc(c,ch):
    ccount = 0
    for i in ch:
        if i == c:
            ccount += 1
    return(ccount)
Huong = countc("c", "combien de temp tu etudier")
print(Huong)
 #exercise 2.2
def Ex22(c,i, ch):
    output = ""
    for x in range (0, len(ch)):
        if x == i:
            output += c
        else:
            output += ch[x]
    return (output)
change = Ex22("c",3,"hello")
print(change) 





