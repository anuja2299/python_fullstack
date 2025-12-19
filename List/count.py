my_list = [3,7,9,0,2]
od = 0
evn = 0
zro = 0
for i in my_list:
    if i%2  == 0 and i != 0:
        evn = evn + 1
    elif i==0:
        zro += 1
    else:
        od += 1
result = [od,evn,zro]
print(result)