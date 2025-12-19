l = int(input("Enter the number of items in the list"))
my_list = []
for i in range(l):
    item = input("enter the item : ")
    my_list.append(item)
result = []
for i in my_list:
    if i not in result:
        result.append(i)
print(" ".join(result))