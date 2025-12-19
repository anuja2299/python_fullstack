my_list = [4, 5, 6, 7, 8, 5, 6]
a = my_list
result =[]
for i in my_list:
    c = 0
    for j in a:
        if i ==j:
            c+=1
    if c ==1:
        result.append(i)
print(result[0])