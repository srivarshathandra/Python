# Implement a function that takes a list of numbers as input and returns the average of these numbers.
def calculate_average(numbers):
    if len(numbers) == 0:
        return 0
    return sum(numbers) / len(numbers)
print(calculate_average([1, 2, 3, 4, 5]))

# Create a function that accepts a string and returns the string with all vowels removed.

def remove_vowels(text):
    vowels = "aeiouAEIOU"
    result = ""
    for char in text:
        if char not in vowels:
            result += char
    return result

print("Without vowels:", remove_vowels("Hello World"))

# def v(a):
#     b=""
#     for i in a:
#         if i not in "aeiouAEIOU":
#             b+=i
#     return b
# print(v("My name is Varsha")) 

# Develop a function to find and return the maximum value in a given list of integers

# def m(q):
#     n=q[0]
#     for i in q:
#         if i>n:
#             n=i
#     return n
# print(m([1,2,3,4,5]))

def find_max(numbers):
    if len(numbers) == 0:
        return None
    max_val = numbers[0]
    for num in numbers:
        if num > max_val:
            max_val = num
    return max_val

print("Max value:", find_max([5, 2, 9, 1]))

# Design a function that simulates a basic calculator, 
# allowing for addition, subtraction, multiplication, and division based on user input.

# m= int(input("Enter the first number: "))
# n= int(input("Enter the second number: "))      
# op= input("Enter the operator (+, -, *, /): ")
# def my_calculator(m,n,op):
#     if op=="+":
#         return m+n
#     elif op=="-":
#         return m-n
#     elif op=="*":
#         return m*n
#     elif op=="/":
#         return m/n      
#     else:
#         return "Invalid operator"

# print(my_calculator(m,n,op))

def calculator(num1, num2, operation):
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        if num2 == 0:
            return "Cannot divide by zero"
        return num1 / num2
    else:
        return "Invalid operation"

print("Calculator:", calculator(10, 5, "*"))

# Write a function that takes a list of strings as input and returns the longest string in the list.

# def l(a):
#     q=a[0]
#     for i in a:
#         if len(i)>len(q):
#             q=i
#     return q
# print(l(["apple", "banana", "grapefruit", "kiwi", "orange"]))

def longest_string(strings):
    if len(strings) == 0:
        return ""
    longest = strings[0]
    for s in strings:
        if len(s) > len(longest):
            longest = s
    return longest

print("Longest string:", longest_string(["apple", "banana", "grapefruit", "kiwi", "orange"]))


# Utilize functions to solve a problem of your choice 
# (e.g., calculating the area and perimeter of different shapes, converting units, etc.), 
# demonstrating your understanding of how functions can be applied in various contexts.

def rectangle_area(length, width):
    return length * width

def rectangle_perimeter(length, width):
    return 2 * (length + width)

def circle_area(radius):
    return 3.14 * radius * radius

def circle_perimeter(radius):
    return 2 * 3.14 * radius

print("Rectangle Area:", rectangle_area(5, 3))
print("Rectangle Perimeter:", rectangle_perimeter(5, 3))
print("Circle Area:", circle_area(4))
print("Circle Perimeter:", circle_perimeter(4))

