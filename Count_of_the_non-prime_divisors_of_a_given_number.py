def prime(x):
    val=True
    for i in range(2,int(x**0.5)+1):
        if x%i==0:
            val=False
    else:
        if val==False:
            return True
        else:
            return False
            
n=int(input())
s=[1,]
for i in range(1,n+1):
    if n%i==0 and prime(i):
        s.append(i)
print(len(s))