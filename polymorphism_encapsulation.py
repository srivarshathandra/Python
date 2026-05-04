# Task : 

# Encapsulation Task 1: E-Commerce Product
# 📌 Instructions:
# Create a class Product
# Create private variable for price
# Add method set_price(price)
# Accept only values greater than 0
# Add method apply_discount(percent)
# Discount should not exceed 50%
# Update price after discount
# Add method get_price()
# Return current price

class Product():
    def __init__(self):
        self.__price = 0
        
    def set_price(self,price):
        if price >0:
            self.__price=price
        else:
            print("Invalid Price!!! Accepts only greater than 0 values")
    
    def apply_discount(self, percent):
        if 0 < percent <= 50:
          discount = (self.__price * percent) / 100
          self.__price -= discount
        else:
            print("Discount should be between 0 and 50")
    def get_price(self):
        return self.__price

p = Product()

p.set_price(1000)
p.apply_discount(20)

print(p.get_price())   # 800


# Encapsulation Task 2: Mobile Lock System
# 📌 Instructions:
# Create a class Mobile
# Create private variable for password
# Add method set_password(pwd)
# Password must be at least 4 characters
# Add method unlock(pwd)
# Check password and print result
# Add method change_password(old_pwd, new_pwd)
# Change only if old password is correct
# New password must follow rules

class Mobile():
    def __init__(self):
        self.__password = None
    
    def set_password(self,pwd):
        if len(pwd) >=4:
            self.__password=pwd
            print("Password set up is successfully done")
        else:
            print("Invalid!! Password should be at least 4 characters ")
    
    def unlock(self,pwd):
        if pwd == self.__password:
            print("Mobile unclocked")
        else:
            print("Wrong password")
    
    def change_password(self,old_password,new_password):
        if old_password != self.__password:
            print("Incorrect password")
        elif len(new_password)<4:
            print("New password with atleast 4 characters")
        else:
            self.__password = new_password
            print("Password changed successfully!")
                
m = Mobile()

m.set_password("1234")
m.unlock("1111")          # Wrong
m.unlock("1234")          # Correct

m.change_password("1234", "12")     # Too short
m.change_password("1234", "5678")   # Success

m.unlock("5678")          # New password works

# Encapsulation Task 3: HR Employee System
# 📌 Instructions:
# Create a class Employee
# Create private variables:
# __salary
# __designation
# Add method set_salary(salary)
# Salary should be greater than 0
# Prevent invalid updates
# Add method get_salary()
# Return salary
# Add method set_designation(role)
# Allow only specific roles (e.g., "Manager", "Developer", "HR")
# Add method get_designation()
# Return designation
# Add method increment_salary(percent)
# Increase salary based on percentage
# Percentage should not exceed 30%
# Do not allow direct access to salary or designation from outside the class

class Employee:
    def __init__(self):
        self.__salary = None
        self.__designation = None
        self.__allowed_roles = ["Manager", "Developer", "HR"]

    def set_salary(self, salary):
        if salary > 0:
            self.__salary = salary
            print("Salary set successfully ")
        else:
            print("Invalid salary ")

    def get_salary(self):
        return self.__salary

    def set_designation(self, role):
        if role in self.__allowed_roles:
            self.__designation = role
            print("Designation set successfully ")
        else:
            print("Invalid designation")

    def get_designation(self):
        return self.__designation

    def increment_salary(self, percent):
        if self.__salary is None:
            print("Set salary first ")
        elif 0 < percent <= 30:
            increment = (self.__salary * percent) / 100
            self.__salary += increment
            print("Salary incremented successfully ")
        else:
            print("Increment should be between 0 and 30% ")


e = Employee()

e.set_salary(50000)
print(e.get_salary())        # 50000

e.set_designation("Developer")
print(e.get_designation())   # Developer

e.increment_salary(20)
print(e.get_salary())        # 60000.0

e.increment_salary(50)       # invalid
e.set_designation("Tester")  # invalid