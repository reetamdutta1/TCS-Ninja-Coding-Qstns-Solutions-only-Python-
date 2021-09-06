n = int(input()) #reetamdutta1
user = [] 
output = [] 
for i in range(0,n): 
    ele = int(input()) 
    user.append(ele) 
    
for ele in user: 
    if ele%2==0: 
        output.append(ele) 
        print(ele) 
        
if len(output)==0: 
    print("No Even Elements Found.")