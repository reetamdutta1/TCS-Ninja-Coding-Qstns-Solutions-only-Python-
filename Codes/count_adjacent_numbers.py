def get_count(num_list):
    count=0
    for x in range (0,len(num_list)-1):
        if (num_list[x]==num_list[x+1]):
            count+=1
            x+=1
        else:
            x+=1
    # Write your logic here
    return count
#provide different values in list and test your program
num_list=[1,1,5,100,-20,-20,6,0,0]
print(get_count(num_list))