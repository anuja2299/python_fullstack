a = {1, 2, 3}
b = {2, 3, 4}
c = {3, 2, 5}
common = a.intersection(b,c)
print(common)
result = []
for i in a:
    for j in b:
        for k in c:
            if i==j==k:
                result.append(k)
result = set(result)
print(result)
