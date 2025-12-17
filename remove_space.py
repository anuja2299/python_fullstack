my_string = input("Enter your String : ")
result = ''
for i in my_string:
    if i == ' ':
        result = result
    else:
        result = result + i
print(result)