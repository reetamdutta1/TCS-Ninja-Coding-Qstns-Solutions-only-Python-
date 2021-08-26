n=int(input())
user_list=[]

for i in range(n):

    x=int(input())
    user_list.append(x)

squared_num= [num**2 for num in user_list]
print(squared_num)