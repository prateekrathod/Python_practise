from demo4_employee.employee_module import Employee

Employee.company_name= "Accenture"
Employee.company_location= "Bhubhaneswar"

emp1 = Employee()
emp1.emp_id = 101
emp1.emp_name = "Prateek"
emp1.emp_salary = 35000
emp1.emp_performance = "B"

print(emp1.calculate_bonus())

