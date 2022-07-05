#wap  print prime numbers using for loop
n=int(input("enter"))
c=0
for i in range(1,n+1):#123
    if n%i==0:
        c=c+1
if c==2:
    print(n,'prime')
else:
    print(n,'not prime')
         
        
