parent = input()
yes_no = input()

if yes_no =='N' or yes_no =='n':
    print("total members = 1 \n commission details\n {0}: 250 INR".format(parent))

elif yes_no == 'Y' or yes_no == 'y':
    child = list(map(str, input().split(",")))
    print("Total members: {}".format(len(child)+1))
    print("commission details \n{0}:{1} INR".format(parent, len(child)*500))

    for i in child:
        print("{0}:250 INR".format(i))