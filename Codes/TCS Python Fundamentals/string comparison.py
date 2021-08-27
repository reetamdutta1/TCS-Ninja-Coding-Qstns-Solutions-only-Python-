import re #regular expression
string1 = input()
string2 = input()

def string_check(string1,string2):
    if string1==string2:
        return("The Strings are identical!")
    elif(re.search(string2,string1)):
        return(string2 + " is a substring of " + string1)
    else:
        return("The strings are NOT identical!")

print(string_check(string1,string2))
