h,m=map(int,input().split(':'))
a=abs(30*h-(11/2)*m)
if a>180:
    print(360-a)
else:
    print(a)