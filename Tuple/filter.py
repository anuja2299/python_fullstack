data = ((1, 'a'), (2, 'b'), (3, 'a'))

result = []

for item in data:
    if item[1] == 'a':
        result.append(item)

print(result)
