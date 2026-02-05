n = input("enter a number")
n = str(n)
l = 0
i = 0
while i < len(n):
    if int(n[i]) >= l:
        l = int(n[i])
    i = i+1
print(l)
