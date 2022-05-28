#PATTERN 138

n= 4
k = 0

for x in range(1,n+1):
    k+=x
    for y in range(k,k-x,-1):
        print(str(y) +"",end="")
    print()
    
'''
1
32
654
10987
'''
    
