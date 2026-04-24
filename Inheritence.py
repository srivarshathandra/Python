# Task : 

# 🧬 1️⃣ SINGLE INHERITANCE TASK
# 🎯 Scenario: Online Course Platform
# 👉 Parent Class: Course
# course_name
# price
# method → show_course()
# 👉 Child Class: ProgrammingCourse
# language
# duration
# method → show_programming_course()

# 🧑‍💻 Task:
# Create 2 programming courses
# Use super()
# Print all details
# 👉 Expected Thinking:
#  “Base course details reused + extra programming details added”


class Course:
    def show_course(self):
        print("course_name : Data science full-stack course ")
        print("price : 50000")
        
class ProgrammingCourse(Course):
    def show_programming_course(self):
        super().show_course()
        print("language : Python,SQL,Excel,Statistics")
        print("duration :  8 months")
    
o=ProgrammingCourse()
o.show_programming_course()


# 🧬 2️⃣ MULTIPLE INHERITANCE TASK
# 🎯 Scenario: Smart Phone Features
# 👉 Parent 1: Camera
# camera_mp
# method → take_photo()
# 👉 Parent 2: MusicPlayer
# brand
# method → play_music()
# 👉 Child: SmartPhone
# model_name
# method → show_details()

# 🧑‍💻 Task:
# Create 2 smartphones
# Call both parent methods
# Print all features
# 👉 Goal:
#  Understand using multiple parents in one class


class Camera:
    def take_photo(self):
        print("camera_mp: 1080 MP")

class MusicPlayer:
    def play_music(self):
        print("Musicplayer : Play Music ")
        
class Smartphone(Camera,MusicPlayer):
    def show_details(self):
        print("Phone_Model: Samsung")
        self.take_photo()
        self.play_music()

p=Smartphone()
p.show_details()

        
    