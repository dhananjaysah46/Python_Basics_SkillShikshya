class Employee:
    'Common base class for all employees'
    empCount = 0
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1
    def display_count(self):
        print(f"Total Employee {Employee.empCount}")
        
    def get_details(self):
        print(f"Name : {self.name}, Salary: {self.salary}")

emp1 = Employee("Zara", 2000)
emp2 = Employee("Manni", 5000)
emp1.display_count()
emp1.get_details()
print("Total emplyees %d" % Employee.empCount)
    

