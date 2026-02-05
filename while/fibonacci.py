n = int(input("Enter number of terms greater than 0: "))
if n==1:
    print(0)
elif n==2:
    print("0 1")
else:
    a = 0
    b = 1
    count = 0
    while count < n:
        print(a, end=" ")
        c = a + b
        a = b
        b = c
        count += 1
