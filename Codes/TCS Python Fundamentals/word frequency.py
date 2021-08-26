"""
Input a string
Input the word to calculate its frquency
EXAMPLE:
    My name name is Reetam Dutta name
    name
    3 <- This must be the output

NOTE: If the word is not found, print "WORD NOT FOUND"
"""


def wordFreq(str1,str2):
    a = str1.split(" ") 
    b = a.append(str2) 
    c = a.count(a[-1])-1
    if c>0:
        return c
    else:
        return("WORD NOT FOUND")

str1=input() 
str2=input()
print(wordFreq(str1,str2))

