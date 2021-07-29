user = int(input())
if user>1:
    for i in range (2, user):
        if (user%i)==0:
            print("Not a prime number")
            break
    else:
        print("Prime numbber")
else:
    print("Not a Prime numbber")
            