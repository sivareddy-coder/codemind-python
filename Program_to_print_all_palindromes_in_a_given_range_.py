fs=int(input())
ls=int(input())
for i in range(fs,ls):
    s=0
    x=i
    while i>0:
        r=i%10
        s=s*10+r
        i=i//10
    if x==s:
        print(x,end=" ")