#exercise7.1
def Nbsmotscommuns(list1, list2):
    count = 0
    for i in list1:
        for j in list2:
            if i == j:
                count += 1
    return count
menu1 = ["Chicken", "frites", "cat"]
menu2 = ["cat", "pig", "frites"]
print(Nbsmotscommuns (menu1, menu2))
#exercise 7.2:
def Motscommuns(list1, list2):
    output = ""
    for i in list1:
        for j in list2:
            if i == j:
                output += i
    return output
print(Motscommuns(menu1, menu2))
#Exercise 7.3
def Fusion(list1, list2):
    s = ""
    for i in list1:
        for j in list2:
            if i not in j:
                s += i
            else:
                s = s
            return s
print(Fusion(menu1, menu2))
#Exercise 7.4:
def Pluspetitelongueur(listedemots):
    h = ""
    temp = ""
    for i in listedemots:
        if i >= i:
            temp = i
        elif i >= temp:
            h = i
        else:
            h = h
    return h
List = [ "call", "you", "baby", "beautifull" ]
print(Pluspetitelongueur(List))


