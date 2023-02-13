from database import Employee
try:
    e_name = input("enter employee name")
    e_email =input("enter employee email")
    e_post =input("enter employee post")
    Employee.create(name =e_name, email=e_email, post=e_post)
    print ("saved successfully")
except:
    print("Error")