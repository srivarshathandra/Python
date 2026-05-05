# MULTILEVEL INHERITANCE TASK
# 🎯 Scenario: Education System
# 👉 Class 1: School
# school_name
# method → show_school()
# 👉 Class 2: Teacher (inherits School)
# teacher_name
# subject
# method → show_teacher()
# 👉 Class 3: Student (inherits Teacher)
# student_name
# grade
# method → show_student()

# 🧑‍💻 Task:
# Create 2 students
# Use super() in all classes
# Print full hierarchy details
# 👉 Goal:
#  Understand chain inheritance


class School:
    def __init__(self,school_name):
        self.school_name = school_name
    
    def show_school(self):
        print("School:", self.school_name)
        
class Teacher(School):
    def __init__(self, school_name,teacher_name,subject):   
        super().__init__(school_name)
        self.teacher_name = teacher_name
        self.subjects = subject
    
    def show_teacher(self):
        print("Teacher name",self.teacher_name)
        print("Subject:",self.subjects)

class Student(Teacher):
    def __init__(self,school_name,teacher_name,subject,student_name,grade):
        super().__init__(school_name, teacher_name, subject)
        self.student_name = student_name
        self.grade =grade
    
    def show_student(self):
        print("Student_name",self.student_name)
        print("grade",self.grade)
        
s1 = Student("XYZ School", "Varsha", "Maths", "Divya", "A")
s2 = Student("XYZ School", "Varsha", "Maths", "Rahul", "B")

for s in [s1, s2]:
    print("\n--- Details ---")
    s.show_school()
    s.show_teacher()
    s.show_student()
    
    
# HIERARCHICAL INHERITANCE TASK
# 🎯 Scenario: Food Delivery App
# 👉 Parent: User
# name
# location
# method → login()
# 👉 Child 1: Customer
# order_item
# method → place_order()
# 👉 Child 2: DeliveryPartner
# vehicle_type
# method → deliver_order()

class User:
    def __init__(self,name,location):
        self.name = name
        self.location = location
    
    def login(self):
        print(self.name, "logged it from", self.location)

# child 1

class Customer(User):
    def __init__(self,name,location,order_item):
        super().__init__(name,location)
        self.order_item = order_item
    
    def place_order(self):
        print(self.name, "ordered", self.order_item)
        
class DeliveryPartner(User):
    def __init__(self,name,location,vechile_type):
        super().__init__(name,location)
        self.vechile_type=vechile_type
    
    def deliver_order(self):
        print(self.name,"is delivering using", self.vechile_type)
        

c1 = Customer("Varsha", "Hyderabad", "Burger")
d1 = DeliveryPartner("Ravi", "Hyderabad", "Bike")

c1.login()
c1.place_order()

print()

d1.login()
d1.deliver_order()
        
        
