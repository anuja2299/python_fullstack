user_name = 'admin'
password = '1234'
while True:
    user = input("enter user name : ")
    pw = input("enter the password : ")
    if user == user_name and pw == password:
        print("login successful !!")
        break
    else:
        print("try again")