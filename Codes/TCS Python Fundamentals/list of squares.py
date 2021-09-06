n=int(input())
user = []
output=[]

for i in range(0,n):
    ele = int(input())
    user.append(ele)

for ele in user:
    sqr = ele ** 2
    output.append(sqr)
    print(sqr)


