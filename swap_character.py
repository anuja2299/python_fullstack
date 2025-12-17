my_string = input("Enter the String")
result = ''
for i in my_string:
    result = result + i.swapcase()
print(result)