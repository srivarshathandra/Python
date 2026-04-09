# Conditional Statements Basics

# Objective
# In this assignment, students will practice applying conditional statements 
# to solve basic programming problems, focusing on building logical 
# decision-making processes within their code.

# Background / Context
# Conditional statements are fundamental in programming,
# allowing code to make decisions based on conditions or user inputs. 
# This assignment is designed for students in basic classes to apply
# their understanding of if-else statements, switch statements, 
# and conditional operators in real-world scenarios.

# Tasks / Requirements
# Implement a program that asks the user for their age and then tells them
# if they are eligible to vote based on a minimum voting age of 18.
# Write a function that takes a grade (from 1 to 100) as input and returns
# a string indicating whether the grade corresponds to a fail (below 50), 
# pass (50-69), good (70-84), or excellent (85 and above).
# Create a simple calculator that takes in two numbers and 
# an operator (+, -, *, /) and performs the operation based on the operator,
# handling division by zero errors using conditional statements.
# Develop a program that determines whether a given year is a leap year or not, 
# using conditional statements to apply the rules for leap years.
# Write a conditional statement that checks if a given number is
# odd or even and prints out the result.


# # Implement a program that asks the user for their age and then tells them
# if they are eligible to vote based on a minimum voting age of 18.




# age = int(input("Please enter your age: "))
# if age >= 18:
#     print("You are eligible to vote.")
# else:
#     print("You are not eligible to vote.")  



    
# Write a function that takes a grade (from 1 to 100) as input and returns
# a string indicating whether the grade corresponds to a fail (below 50),  
# pass (50-69), good (70-84), or excellent (85 and above).



# marks = int(input("Please enter your grade (1-100): "))
# if marks <= 50:
#     print("Fail")
# elif marks <= 70:
#     print("Pass")          
# elif marks <= 85:
#     print("Good")       
# else:
#     print("Excellent")      



# Create a simple calculator that takes in two numbers and 
# an operator (+, -, *, /) and performs the operation based on the operator,
# handling division by zero errors using conditional statements.

# n_1 = float(input("Enter the first number: "))
# n_2 = float(input("Enter the second number: ")) 
# operator = input("Enter the operator (+, -, *, /): ")   
# if operator=='+':
#     print("sum:", n_1 + n_2)
# elif operator=='-':
#     print("difference:", n_1 - n_2) 
# elif operator=='*':
#     print("product:", n_1 * n_2)    
# elif operator=='/':
#     if n_2!=0:
#         print("quotient:", n_1 / n_2 )
#     else:
#         print("Error: Division by zero is not allowed.")        
        
        

a=int(input("Enter a number: "))
b=int(input("Enter another number: "))  
op=input("enter an opeator(+,-,*,/,%):--")
if op == "+":
            print("sum of two numbers is :",a+b)
            elif op == "-":
            print("difference of two numbers is :",a-b)
            elif op =="*":
            print("product of two numbers is :",a*b)
        elif op =="/":
            if b!=0:
                print("quotient of two numbers is :",a/b)
        elif op =="%":    
            if b!=0:
                print("remainder of two numbers is :",a%b)
        else:
            print("Invalid operator")
            


# Develop a program that determines whether a given year is a leap year or not, 
# using conditional statements to apply the rules for leap years.

 
# leap_year=int(input("Enter a year: "))
# if (leap_year %4==0 and leap_year %100!=0) or (leap_year %400==0):
#     print(leap_year, "is a leap year.")
# else:
#     print(leap_year, "is not a leap year.") 



# # Write a conditional statement that checks if a given number is
# # odd or even and prints out the result.

# number=int(input("Enter a number: "))
# if number % 2 == 0: 
#     print(number, "is an even number.")         
# else:
#     print(number, "is an odd number.")
