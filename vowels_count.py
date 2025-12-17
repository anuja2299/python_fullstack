my_string = input("Enter the string : ")
vowels = ['a','e','i','o','u','A','E','I','O','U']
c = 0
for i in my_string:
    if i in vowels:
        c = c+1
print(c)