s1= str(input())
s2= str(input())
s3= str(input())
vowels = 'AEIOUaeiou'
consonants = 'BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz'

for i in vowels:
    s1 = s1.replace(i,'*')


for i in consonants:
    s2 = s2.replace(i, '@')

s3 = s3.upper()

print(s1+s2+s3)

#for i in range(len(s1)+1):
#    if (s1[i] =='a') or (s1[i] =='e') or (s1[i] =='i') or (s1[i] =='o') or (s1[i] =='u'):
#        s1[i]='*'

#for i in range(len(s2)+1):
#    if (s2[i] >='a'and s2[i] <='z') or (s2[i] >='A' and s2[i] <='Z') or (s1[i] =='u'):
#       s2[i]='@'

#for i in range(len(s3)+1):
#    if (s3[i] >='a' and s3[i] <='z'):
#        s3[i]= s3[i]-32
 


