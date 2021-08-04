#Every character in the input string is followed by its frequency.
#Write a function to decrypt the string and find the nth character of the decrypted string. If no character exists at that positionthen then return "-1".
#For eg:- If the input string is "a2b3" the decrypted string is "aabbb".
#Note: The frequency of encrypted string cannot be greater than a single digit i.e.<10. */

def decrypt(s):
    output = []
    for i in s:
        if(i.isalpha()):
            output.append(i)
        else:
            for i in range(int(i)-1):
                output.append(output[-1])
                
    print(''.join(output))


s=input("Enter the string: ")
decrypt(s)
#decrypt("a9b7") #'aabbb'