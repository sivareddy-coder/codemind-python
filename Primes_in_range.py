def prime(n):
    for i in range(2,int(n**0.5)+1):

        if(n%i==0):

            return 0

    else:

        if(n!=0 and n!=1):

            return 1

m=int(input())

n=int(input())

c=0

for i in range(m,n+1):

    if(prime(i)):

        c+=1

print(c)