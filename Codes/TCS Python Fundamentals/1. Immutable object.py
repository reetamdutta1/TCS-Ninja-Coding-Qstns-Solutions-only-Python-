def changeme1( myset ):
    #myset.append([1,2,3,4]);
    print ("Values inside the function: ", myset)
    myset[2]=333
    return
myset = (10,20,30);
changeme1( myset );
print ("Values outside the function: ", myset)