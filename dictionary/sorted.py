unsorted = {'apple': 5, 'banana': 2, 'cherry': 7}
result = dict(sorted(unsorted.items(), key = lambda x:x[1]))
print(result)