# Implement a function that takes a list of numbers as input and returns the average of these numbers.
a=[1,2,3,4,5]
def avg_num(a):
    sum=0
    for i in a:
        sum+=i
    return sum/len(a)

print(avg_num(a))

# Create a function that accepts a string and returns the string with all vowels removed.

def v(a):
    b=""
    for i in a:
        if i not in "aeiouAEIOU":
            b+=i
    return b
print(v("My name is Varsha")) 

# Develop a function to find and return the maximum value in a given list of integers

def m(q):
    n=q[0]
    for i in q:
        if i>n:
            n=i
    return n
print(m([1,2,3,4,5]))

# Design a function that simulates a basic calculator, 
# allowing for addition, subtraction, multiplication, and division based on user input.

m= int(input("Enter the first number: "))
n= int(input("Enter the second number: "))      
op= input("Enter the operator (+, -, *, /): ")
def my_calculator(m,n,op):
    if op=="+":
        return m+n
    elif op=="-":
        return m-n
    elif op=="*":
        return m*n
    elif op=="/":
        return m/n      
    else:
        return "Invalid operator"

print(my_calculator(m,n,op))

# Write a function that takes a list of strings as input and returns the longest string in the list.

def l(a):
    q=a[0]
    for i in a:
        if len(i)>len(q):
            q=i
    return q
print(l(["apple", "banana", "grapefruit", "kiwi", "orange"]))


# Utilize functions to solve a problem of your choice 
# (e.g., calculating the area and perimeter of different shapes, converting units, etc.), 
# demonstrating your understanding of how functions can be applied in various contexts.

def areas_of_different_shapes(shapes,details):
    for i in range(len(shapes)):
        if shapes[i]=="circle":
            r=details[i]
            area=3.14*r*r
            print("The area of the circle is:",area)
        elif shapes[i]=="square":
            s=details[i]
            area=s*s
            print("The area of the square is:",area)
        elif shapes[i]=="rectangle":
            l=details[i][0]
            w=details[i][1]
            area=l*w
            print("The area of the rectangle is:",area)
shapes=["circle","square","rectangle"]
details=[5,4,[3,6]]     
areas_of_different_shapes(shapes,details)

