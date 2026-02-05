row = int(input("enter the length"))
for i in range(1,row+1):
    for j in range(row-i):
        print(' ',end ='')
    for k in range(1,i+1):
        print(i,end="")
    print()