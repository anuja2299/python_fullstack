original = {'a': 1, 'b': 2, 'c': 3}
swapped = {}
for key, value in original.items():
    swapped[value] = key
print(swapped)