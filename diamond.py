#diamond program

n=int(input('enter the number-:'))
print(' '*(n+(n-1)) + ' *')
for i in range(1,n+1):
    print('  '*(n-i) + ' *'*i + ' *'*i)
for j in range(n,0,-1):
    print('  '*(n-j) +' *'*j +' *'*j)
print(' '*(n+(n-1)) + ' *')
