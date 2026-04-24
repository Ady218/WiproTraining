"""

"""
from logging import basicConfig


class EmployeeDetails:
    def __init__(self, empno, ename, basicpay): #constructors
        self.__emp_no = empno
        self.__emp_name = ename
        self.__basic_pay = basicpay
        self.da = 20.0
        self.hra = 10.0
        self.pf = 5.5

    # def get_emp_no(self): #getter(used for private variables)
    #     return self.__emp_no
    # def set_emp_no(self, eno): #setter(used for private variables)
    #     self.__emp_no = eno

    #or we can do the below the decorator way
    @property
    def emp_no(self):
        return self.__emp_no

    @emp_no.setter
    def emp_no(self, eno):
        self.__emp_no=eno

    @property
    def emp_name(self):
        return self.__emp_name

    @emp_name.setter
    def emp_name(self, ename):
        self.__emp_name = ename

    @property
    def basic_pay(self):
        return self.__basic_pay

    @basic_pay.setter
    def basic_pay(self, basicpay):
        self.__basic_pay = basicpay

    def __calculate_allowance(self):
        allowance = (self.basic_pay *self.da/100) + (self.basic_pay * self.hra/100)
        return allowance
    def __calculate_deduction(self):
        deduction = (self.basic_pay *self.pf/100)
        return deduction
    def calculate_netsal(self):
        netsal = self.basic_pay + self.__calculate_allowance() - self.__calculate_deduction()
        return netsal