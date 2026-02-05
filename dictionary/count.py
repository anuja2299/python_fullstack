data = [1, 2, 2, 3, 4, 4, 4, 5]
freq = {}
for item in data:
    if item in freq:
        freq[item] = freq[item] + 1
    else:
        freq[item] = 1
print(freq)