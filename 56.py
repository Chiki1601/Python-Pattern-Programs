# pattern 56

size= 3
for x in range(size,-(size+1),-1):
    for y in range(abs(x),size+1):
        print(y,end="")
    print()
    
''' 
3
23
123
0123
123
23
3
'''
