class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def __add__(self, other):
        return Employee(self.name + " & " + other.name, self.salary + other.salary)
    def __sub__(self, other):
        return self.salary - other.salary
    def __str__(self):
        return f"Employee({self.name}, {self.salary})"
emp1 = Employee(input("Enter name  :"), int(input("Enter salary : ")))
emp2 = Employee(input("Enter name : "), int(input("Enter salary : ")))
emp3 = emp1 + emp2
print(emp3)
print("Salary difference:", emp2 - emp1)
