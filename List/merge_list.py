list1 = ['a','b','c']
list2 = [1,2,3,4]
result = []
i=0
while i < len(list1) and i < len(list2):
    result.append(list1[i])
    result.append(list2[i])
    i += 1
result.extend(list1[i:])
result.extend(list2[i:])
print(result)