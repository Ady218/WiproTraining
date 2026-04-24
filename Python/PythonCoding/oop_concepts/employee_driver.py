"""
driver code
"""
from oop_concepts.employee_details import EmployeeDetails

#driver
eno = int(input('Emp no.: '))
name = input('Emp name: ')
bp = float(input('Basic pay: '))


employee = EmployeeDetails(empno=eno, ename=name, basicpay=bp)

print('Emp no.: ', employee.emp_no) #attributes
print('Emp name: ', employee.emp_name)
print('Basic pay: ', employee.basic_pay)
print('DA: ', employee.da)

print('Salary: ', employee.calculate_netsal()) #methods

