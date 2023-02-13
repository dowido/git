from database import Employee
users =Employee.select()

for user in users:
    print (user.name, user.email, user.post)























