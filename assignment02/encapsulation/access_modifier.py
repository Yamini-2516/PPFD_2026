#private
class Employee:
    def __init__(self, name, salary):
        self.name = name          # public
        self.__salary = salary    # private

    def show_salary(self):
        print("Salary:", self.__salary)


emp = Employee("Rajesh", 60000)
print(emp.name)          # Public accessible
emp.show_salary()        # Accessing private correctly
# print(emp.__salary)    # Error: Not accessible directly



#protected
class Employee:
    def __init__(self, name, age):
        self.name = name       # public
        self._age = age        # protected


class SubEmployee(Employee):
    def show_age(self):
        print("Age:", self._age)   # Accessible in subclass


emp = SubEmployee("Vikas", 30)
print(emp.name)        # Public accessible
emp.show_age()         # Protected accessed through subclass



#public
class Employee:
    def __init__(self, name, age):
        self.name = name       # public
        self._age = age        # protected


class SubEmployee(Employee):
    def show_age(self):
        print("Age:", self._age)   # Accessible in subclass


emp = SubEmployee("Vikas", 30)
print(emp.name)        # Public accessible
emp.show_age()         # Protected accessed through subclass