def removePaint(a,b):
    c = a-b
    d = (c/a)*b
    e = c - d
    return e

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(removePaint(a,b))



    