#swastika drawing in Python
n = 10
for x in range(1,n+1):
    for y in range(1,n+1):
        if((x==n//2+1 or y==n//2+1)or
          (x==1 and y>=n//2+1)or
            (x==n and y<=n//2)or 
            (y==1 and x<=n//2)or
            (y==n and x>=n//2+1)):
                print("*",end="")
        else:
            print(" ",end="")
    print()
        
