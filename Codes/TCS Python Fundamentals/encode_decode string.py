def encode(text):
    new_text =""  #CREATING A NEW STRING VARIABLE
    for i in range(len(text)):
        val = ord(text[i])  #RETURN THE ASCII VALUE OF EACH CHARACTER
        chk = text.isalpha()  #CHECKS IF INPUT STRING IS ALPHABETS ONLY
        if chk == True:  #IF CHECK RETURNS TRUE FOR ISALPHA()
            if val + 5>122:
                new_text += chr(96 + (val - 117)) #CYCLES TO THE FIRST CHARACTER
            else:
                new_text += chr(val + 5) #INCREASES ASCII VALUE BY 5
        else:
            return("INVALID INPUT") #NO NUMERICAL OR SPECIAL CHARACTERS ALLOWED

    return(new_text)

def decode(text):
    new_text =""
    for i in range(len(text)):

        val = ord(text[i])
        chk = text.isalpha()
        if chk == True:
            if val - 5 < 65:
                new_text += chr(90 - (70 - val))
            else:
                new_text += chr(val - 5) #DECREASES ASCII VALUE BY 5
        else:
            return("INVALID INPUT")

    return(new_text)

def encode_decode(str1, str2):
    print(str1 +" --> " + encode(str1) + " (encoded)")
    return(str2 +" --> " + decode(str2) + " (decoded)")

n=input() #ENTER STRING WITHOUT SPACE
p=input() #ENTER STRING WITHOUT SPACE
print(encode_decode(n,p))
