n=input()
count=0
a=[]
for i in n:
    if i=='0' or i=='1':
        a.append(i)
    else:
        count+=1
if count>0:
    print("no")
else:
    print("yes")
