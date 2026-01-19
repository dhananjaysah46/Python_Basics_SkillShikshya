# Example of a class with class methods in Python
class Employee:
    empCount = 0
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Employee.empCount += 1

    @classmethod
    def showcount(cls):
        print(cls.empCount)

    @classmethod   
    def newemployee(cls, name, age):
        return cls(name, age)

emp1 = Employee("Zara", 20)
emp2 = Employee("Manni", 50)
emp4 = Employee.newemployee("Ramesh", 22)
