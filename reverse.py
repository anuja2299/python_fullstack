s = input("enter your string : ")
l = len(s)
r = ''
for i in range(-1,-l-1,-1):
    r = r + s[i]
print(r)