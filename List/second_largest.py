my_list = []
l = int(input("Enter the length of the string : "))
for i in range (0,l):
    e = int(input(("Enter the elements : ")))
    my_list.append(e)
a = 0
b = 0
for i in my_list:
    if i > a:
        b = a
        a = i
print(f"Second largest item is : {b}")