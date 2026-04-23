# Oops intro task :-- 

# 🧩 Task 1: Student System
# 👉 Question:
# Create a class Student with:
# Class variable: school_name = "XYZ School"
# A method set_details()
#  → inside method, assign:
# name = "Vamsi"
# marks = 85
# A method display()
#  → print:
# Name
# Marks
# School name
# 👉 Outside the class:
# Create object
# Call set_details()
# Call display()

class Student:
    school_name = "XYZ School"
    
    def set_details(self):
        name = "Vamsi"
        marks = 85
        self.name=name
        self.marks=marks
    
    def display(self):
        print("Name:", self.name)
        print("Marks:", self.marks)
        print("School Name: ", self.school_name)
# Outside the class
student1 = Student()
student1.set_details()
student1.display()
    
        
# 🧩 Task 2: Employee System
# 👉 Question:
# Create a class Employee with:
# Class variable: company = "Infosys"
# A method set_data()
#  → assign:
# name = "Ravi"
# salary = 20000
# A method increase_salary()
#  → add 5000 to salary
# A method display()
#  → print all details
# 👉 Outside the class:
# Create object
# Call all methods


class Employee:
    company ="Infosys"
    
    def set_data(self):
        name="Ravi"
        salary= 20000
        self.name=name
        self.salary=salary
        
    def increase_salary(self):
        self.salary +=5000
        
    def display(self):
        print("Name:", self.name)
        print("Salary:", self.salary)
        print("Company Name: ", self.company)

# Outside the class
employee1 = Employee()
employee1.set_data()
employee1.increase_salary()
employee1.display()

# 🧩 Task 3: Mobile System
# 👉 Question:
# Create a class Mobile with:
# Class variable: brand = "Apple"
# A method set_details()
#  → assign:
# model = "iPhone 14"
# price = 80000
# A method discount()
#  → reduce price by 10%
# A method show_details()
#  → print all details
# 👉 Outside the class:
# Create object
# Call methods

class Mobile:
    brand="Apple"
    
    def set_details(self):
        model="iPhone 14"
        price=80000
        self.model=model
        self.price=price
        
    def discount(self):
        self.price -= self.price * 0.10
        
    def show_details(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Price:", self.price)

# Outside the class
mobile1 = Mobile()
mobile1.set_details()
mobile1.discount()
mobile1.show_details()

