from database import User
try:
    user_name =input("Enter name\n")
    user_email = input("enter email\n")
    user_password =input("enter password\n")
    User.create(name=user_name, email= user_email, password=user_password)
    print("data saved successfully")
except:

    print("please input valid details")
