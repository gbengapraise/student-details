class Person:
    def __init__(self, name, idnumber):
        self.name = name
        self.idnumber = idnumber
    def display(self):
        print("Name:", self.name, "ID:", self.idnumber)
class Employee(Person):
    def __init__(self, name, idnumber, salary, post):
        super().__init__( name, idnumber)
        self.salary = salary
        self.post = post
    def display(self):
        print("Name:", self.name, "ID:", self.idnumber)
employee1 = Employee("praise", "4656", 1000, "coder")
employee1.display()