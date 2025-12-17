my_string = input("Enter a string")
vowels = ['a','e','i','o','u','A','E','I','O','U']
result = ''
for i in my_string:
    if i in vowels:
        result = result + '*'
    else:
        result = result + i
print(result)