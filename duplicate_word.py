my_string = input("Enter the string : ")
text = my_string.split()
result = []
for i in text:
    if i not in result:
        result.append(i)
print(" ".join(result))
