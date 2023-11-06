# class Employee:
#     raise_amount = 1.04
#
#     def __init__(self,first_name,last_name,pay):
#         self.first = first_name
#         self.last= last_name
#         self.pay = pay
#         self.email = first_name + '.' + last_name + "@company.com"
#
#     def fullname(self):
#         return '{} {}'.format(self.first, self.last)
#
#     def apply_raise(self):
#         self.pay = int(self.pay * self.raise_amount)
#
# class Developer(Employee):
#     raise_amount = 1.10
#
#     def __init__(self, first_name, last_name, pay, prog_lang):
#         super().__init__(first_name,last_name,pay)
#         self.prog_lang = prog_lang
#
#
# class Manager(Employee):
#
#     def __init__(self,first_name, last_name, pay, employees=None):
#         super().__init__(first_name, last_name, pay)
#         if employees is None:
#             self.employees = []
#         else:
#             self.employees = employees
#
#     def add_emp(self,emp):
#         if emp not in self.employees:
#             self.employees.append(emp)
#
#     def remove_emp(self,emp):
#         if emp in self.employees:
#             self.employees.remove(emp)
#
#     def print_emp(self):
#         for emp in self.employees:
#             print('---->',emp.fullname())
#
#
# emply_1 = Developer('Bishal',"KC",25000, "Python")
# emply_2 = Developer("Alice","Cordy",50000, "Java")
#
# mgr_1 = Manager("Sue","Smith", 90000,[emply_1])
# print(mgr_1.email)
# mgr_1.add_emp(emply_2)
# mgr_1.remove_emp(emply_1)
# mgr_1.print_emp()
#
# class Employee:
#     raise_amount = 1.04
#
#     def __init__(self,first_name,last_name,pay):
#         self.first = first_name
#         self.last= last_name
#         self.pay = pay
#         self.email = first_name + '.' + last_name + "@company.com"
#
#     def fullname(self):
#         return '{} {}'.format(self.first, self.last)
#
#     def apply_raise(self):
#         self.pay = int(self.pay * self.raise_amount)
#
#     def __repr__(self):
#         return "Employee('{}','{}',{})".format(self.first,self.last,self.pay)
#
#     def __str__(self):
#         return '{} - {}'.format(self.fullname(),self.email)
#
# emp_1 = Employee("Bishal","KC",50000)
# emp_2 = Employee("Sujin","Thapa",60000)
#
# print(repr(emp_1))
# print(str(emp_1))
#


# class Employee:
#     raise_amount = 1.04
#
#     def __init__(self,first_name,last_name):
#         self.first = first_name
#         self.last= last_name
#
#     @property
#     def email(self):
#         return '{}.{}@email.com'.format(self.first, self.last)
#     @property
#     def fullname(self):
#         return '{} {}'.format(self.first, self.last)
#
#     @fullname.setter
#     def fullname(self,name):
#         first,last = name.split(" ")
#         self.first = first
#         self.last = last
#
#     @fullname.deleter
#     def fullname(self):
#         print('Delete Name')
#         self.first = None
#         self.last = None
#
# emp_1 = Employee('John', 'Smith')
#
# emp_1.first = "Joe"
# emp_1.fullname = "Corey Schafer"
#
# print(emp_1.first)
# print(emp_1.email)
# print(emp_1.fullname)
#
# del emp_1.fullname

list = ["1", "4", "0", "6", "9"]
list = [int(i) for i in list]
list.sort()
print (list)

