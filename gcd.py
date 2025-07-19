n1,n2=map(int,input().split())
while n1>0 and n2>0:
    if n1>n2:
        n1=n1%n2
    elif n2>n1:
        n2=n2%n1
    else:
        print(n1)
        break
if n1==0:
    print(n2)
else:
    print(n1)