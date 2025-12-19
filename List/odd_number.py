my_list = [1, 1, 2, 3, 2, 3, 3, 1]
result=[]
a = my_list
for i in my_list:
    c = 0
    for j in a:
        if i==j:
            c+=1
    if c%2==1:
        result.append(i)
r = set(result)
r = list(r)
for i in r:
    print(i, end=' ')