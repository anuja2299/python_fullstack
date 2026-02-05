scores = {'Alice': 88, 'Bob': 95, 'Charlie': 70}
max = 0
for key,value in scores.items():
    if value > max :
        max = value
        result = key
    else:
        continue
print(result)



