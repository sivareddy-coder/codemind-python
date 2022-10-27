n=int(input())
for i in range(n):
    a,b,c,d=map(int,input().split())
    x=a//b
    y=a%b
    s=0
    for j in range(x):
        s+=(c+j*d)*b
    s+=(c+x*d)*y
    print(s)