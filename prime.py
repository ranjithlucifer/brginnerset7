name=int(input())
if name>1:
    for i in range(2,name//2):
        if (name%i)==0:
            print("no")
            break
    else:
        print("yes")
else:
    print("no")
