a=int(input("Enter Mark 1"))
b=int(input("Enter Mark 2"))
c=int(input("Enter Mark 3"))
if(a>=b and a>=c):
     if(b>c):
        print("A and B is big",(a+b)/2)
     else:
        print("A and C is big",(a+c)/2)
elif(b>=c and b>=a):
     if(a>c):
         print("B and A are big",(a+b)/2) 
     else:
         print("B and C is big",(b+c)/2)
else:
     if(a>b):
         print("C and A are big",(a+c)/2) 
     else:
         print("B and C is big",(b+c)/2)


