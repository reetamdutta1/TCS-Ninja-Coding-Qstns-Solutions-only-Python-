def carnivalGame(n):
    user = []
    for i in range(n):
        ele = int(input())
        user.append(ele)

    lst = []
    for i in range(len(user)):
        if i==0:
            value = user[i+1] * user[n-1]
        elif i == len(user)-1:
            value = user[n-2] * user[0]
        else:
            value = user[i-1] * user[i+1]
        lst.append(value)

    print(lst) #ignore
    
    return user[lst.index(max(lst))]


n = int(input())
print(carnivalGame(n))






