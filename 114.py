#PATTERN 114

n= 5
cen = n//2  + 1

for x in range(1,n+1):
    for y in range(1,n+1):
        if(x==cen or y == cen):
            print("X",end="")
        else:
            print("O",end="")
    print()
        

        
''' 
 OOXOO
 OOXOO
 XXXXX
 OOXOO
 OOXOO
'''
