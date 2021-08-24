def create_doctors():
    d_list=[]
    with open('doctors_list.txt','r+') as doctor:
        d=doctor.readlines()
        for i in d:
            j=i.split('|')
            d_list.append([j[0],j[1],int(j[2])])
    return d_list

if __name__=="__main__":
    doctors=create_doctors()
    #print (doctors)
    for i in doctors:
        #print(i)
        print(i[0])
        print(i[1])# a=i[1]
            # print(a)
        # print(type(a))