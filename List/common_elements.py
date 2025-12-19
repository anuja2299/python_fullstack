list1 = [2,3,4]
list2 = [1,2,3]
result = []
for i in list1:
    if i in list2:
        result.append(i)
print(result)