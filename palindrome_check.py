my_string = input("enter the string : ")
reverse_string = my_string[::-1]
#reverse_string = "".join(reversed(my_string))
if my_string == reverse_string:
    print(True)
else:
    print(False)