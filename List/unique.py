my_list = [1,2,2,3,4,5,4,6,6,8]
a = my_list
result=[]

for i in my_list:
    c = 0
    for j in a:
        if i==j:
            c += 1
    if c == 1:
        result.append(i)
print(result)