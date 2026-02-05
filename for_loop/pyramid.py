row = int(input("enter a number"))

for i in range(1,row+1):
    for j in range((row+1)-i):
        print(" ",end='')
    n=1
    for k in range(1,i+1):
        print(n,end=' ')
        n+=1
    print()
