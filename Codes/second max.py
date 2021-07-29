user=[]
num = int(input("enter number of elements: "))
for i in range(1, num + 1):
    ele = int(input("enter elements: "))
    user.append(ele)

user.sort()
print(user)
print("The second largerst number is: ", user[-2])
