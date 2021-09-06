num = input()
count = 0

l = len(num)

for i in range(0,l):
    for j in range(i+1,l):
        if num[i]==num[j]:
            print(num[i])
            break

