my_list = [4,-6,2,7,-9]
result = []
for i in my_list:
    if i < 0:
        result.append(0)
    else:
        result.append(i)
print(result)