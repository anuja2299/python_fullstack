my_string = input("Enter the string : ")
result = ''
text = my_string.split()
for i in text:
    result = result + i[::-1] +' '
print(result)

