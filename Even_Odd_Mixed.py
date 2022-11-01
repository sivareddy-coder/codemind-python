a=int(input())
b=str(a)
c1=0
c2=0
while a>0:
    n=a%10
    a=a//10
    if n%2==0:
        c1+=1
    else:
        c2+=1
if c1==len(b):
    print("Even")
elif c2==len(b):
    print("Odd")
else:
    print("Mixed")
