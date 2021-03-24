

employees_file = open("employees.txt", "r")
print(employees_file.readlines()[1])
employees_file.close()