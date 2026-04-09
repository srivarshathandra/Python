# Exercise 1. Arithmetic Product and Conditional Logic
# Practice Problem: Write a Python function that accepts two integer numbers. 
# If the product of the two numbers is less than or equal to 1000, return their product; 
# otherwise, return their sum.

# Exercise Purpose: Learn basic control flow and the use of if-else statements. Understand how code decisions change output based on a mathematical threshold.

# Given Input:

# Case 1: number1 = 20, number2 = 30
# Case 2: number1 = 40, number2 = 30
# Expected Output:

# The result is 600
# The result is 70


# def pro_of_two(a,b):
#     if a*b <=1000:
#         print("product of two nyumbers:",a*b)
#     else:
#         print("sum of two numbers:",a+b)
# pro_of_two(20,30)
# pro_of_two(40,30)

# Exercise 2. Cumulative Sum of a Range
# Practice Problem: Iterate through the first 10 numbers (0–9). In each iteration, 
# print the current number, the previous number, and their sum.

# Exercise Purpose: This exercise teaches “State Tracking.” 
# In programming, you often need to remember a value from a previous loop iteration
# to calculate results in the current one. This is the basis for algorithms 
# like Fibonacci sequences or running totals.

# Given Input: Range: numbers = range(10)

# Expected Output:

# Printing current and previous number sum in a range(10)
# Current Number 0 Previous Number 0 Sum: 0
# Current Number 1 Previous Number 0 Sum: 1
# Current Number 2 Previous Number 1 Sum: 3
# ....
# Current Number 8 Previous Number 7 Sum: 15
# Current Number 9 Previous Number 8 Sum: 17

# def sum_two_num():
    
#     for i in range(10):
#         if 1==0:
#             print("Current Number",i,"Previous Number",i,"Sum:",i+i)
#         else:
#             print("Current Number",i,"Previous Number",i-1,"Sum:",i+(i-1))
# sum_two_num()


# chec a num is prime number or not as it return true if it is prime number and false if it is not prime number
# def is_prime(num):
#     if num <= 1:
#         return False
#     for i in range(2, int(num**0.5) + 1):
#         if num % i == 0:
#             return False
#     return True
# print(is_prime(0)) 
# print(is_prime(2))  




# wap to print n number of prime
# i/p: n=5
# o/p: 2,3,5,7,11



    

# def p(n):
#     num=2
#     count=0
#     while n > 0:
#         if p(count):
#             print(count)
#             n-=1
#             count+1
#         num+=1
        
# even number in range 0 to 10
# for i in range(0,10,2):
#     print("even numbers are:",i)
    
    
# odd number in range 0 to 10
# for i in range(1,10,2):
#     print("odd numbers are:",i)
    
   
# a=[13,67,99,55,6,77]
# t=0
# for i in a:
#     t=t+ i
#     print(t)
# print("total sum of list is:",t)


# strip is used to remove the whitespace from a string. 
# lower() is used to convert all characters in a string to lowercase. 
# upper() is used to convert all characters in a string to uppercase.
# file = [" python", "java  ", "    c++ ", "ruby ", "javascript "]
# for i in file:
#     i=i.strip().lower()
#     print(i)

# file = [" python", "java  ", "    c++ ", "ruby ", "javascript "]
# for i in file:
#     i=i.strip().upper()
#     print(i)


# for i in range(7,71,7):
#     print(i)

# for i in range(2,22,2):
#     print(i)


# Can you write a loop that starts at 10, counts down to 1, and then prints "Blast off!" after the loop finishes?
# Goal: 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, Blast off!

# for i in range(10, 0, -1):
#     print(i)
# print("Blast off!")

#Write a program to print the first 10 natural numbers using a for loop.

for i in range(1,11):
    print(i)
    