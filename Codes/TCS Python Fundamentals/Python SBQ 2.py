str1=input() #input the string
str2=input() #input the word to find its frequency

a = str1.split(" ") #split the string into a list
b = a.append(str2) #append the word in the list


#----------------------------------------------------
#print(a) #prints the appended list
#print(a[-1]) #prints the last item of the list, 
             #since it is appended at the last position

#for i in range(0,len(a)): #length of new list
#a.reverse()
#----------------------------------------------------


print(a.count(a[-1])-1) #since we added an extra word




