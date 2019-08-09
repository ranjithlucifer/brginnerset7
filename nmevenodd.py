n=list(map(int,input().split()))
if n[0]>n[1]:
  a=n[0]-n[1]
  if a%2==0:
    print("even")
  else:
    print("odd")
else:
  a=n[1]-n[0]
  if a%2==0:
    print("even")
  else:
    print("odd")
