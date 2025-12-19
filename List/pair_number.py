my_list = [3,4,5,2,5]
target = 7
result = []
for i in range(0, len(my_list)-1):
    for j in range(i+1 , len(my_list)):
        if my_list[i] + my_list[j] == target:
            l = (i,j)
            result.append((my_list[i],my_list[j]))
print(result)
