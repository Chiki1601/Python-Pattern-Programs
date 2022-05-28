#PATTERN 109

n= 5

for x in range(1,n+1):
    for y in range(1,n+1):
        if(x==y):
            print("O",end="")
        else:
            print("X",end="")
    print()
        
''' 
 OXXXX
 XOXXX
 XXOXX
 XXXOX
 XXXXO
'''
