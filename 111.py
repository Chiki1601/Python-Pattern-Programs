#PATTERN 111

n= 5

for x in range(1,n+1):
    for y in range(1,n+1):
        if(x==y or x+y == n+1):
            print("O",end="")
        else:
            print("X",end="")
    print()
        

        
''' 
 OXXXO
 XOXOX
 XXOXX
 XOXOX
 OXXXO
'''
