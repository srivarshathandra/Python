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
        print("course_name : Data science course ")
        print("price : 50000")
        
class ProgrammingCourse(Course):
    def show_programming_course(self,Language,Duration):
        super().show_course()
        print("language :",Language)
        print("duration :",Duration)
    
o1=ProgrammingCourse()
o2=ProgrammingCourse()
o1.show_programming_course("Python", "6 months")
o2.show_programming_course("Java", "5 months")
print("------------------")
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
    def take_photo(self,camera_mp):
        print("camera_mp :",camera_mp)

class MusicPlayer:
    def play_music(self,brand):
        print("Musicplayer :", brand)
        
class Smartphone(Camera,MusicPlayer):
    def show_details(self,model,camera_mp,brand):
        print("Phone_Model :", model)
        self.take_photo(camera_mp)
        self.play_music(brand)

p1=Smartphone()
p2=Smartphone()
p1.show_details("Samsung", "108 MP", "Play Music")
p2.show_details("iPhone", "48 MP", "Apple Music")

        
    