def retouner(ch):
    output = ""
    for i in ch:
        output = i + output
    return output
Huong = "Hello"
print (retouner(Huong))
 #exercise 6.2
def palindrome(ch):
    s = retouner(ch)
    if (s == ch):
        print ("Yes")
    else:
        print ("No")
Study = "Live evil"
print (palindrome(Study))
