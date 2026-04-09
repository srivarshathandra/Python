
# def greet(name): # creating a function called greet that takes one parameter, name
#     return f"Hello, {name}!" # the function returns a greeting message that includes the name passed as an argument


# def add():
#     a=10
#     b=3
#     print(a+b)
    
# add()# the function returns the sum of a and b
# # python_functions.py
# 

# def mul():
#     a=10
#     b=3
#     print(a*b)
# mul()# the function returns the product of a and b

## real life secenerio: dashboard accessing
# register---- login--- password

# def register():
#     name=input("Enter your name: ")
#     email=input("Enter your email: ")
#     password=input("Enter your password: ")
#     confrim_password=input("Confirm your password: ")
    
#     if password == confrim_password:
#         print("registration successful")
#     else:
#         print("passwords do not match. registration failed.")   
# register()

# def adc():
#     # code
#     abc()

# types of user defined functions:

# a=10
# b=20
# def abc(x,y): # function define: () these are identifiers and x and y are parameters
#     print(x+y) # function body: this is the code that will be executed when the function is called. 
# # In this case, it prints the sum of x and y.
#     print() # this is an empty print statement that will print a blank line after the sum.
# abc(a,b)    # function call: this is where you actually execute the function. 
# In this case, we are calling the abc function and passing the values of a and b as arguments. 
# When this line is executed, the function will run and print the sum of a and b,
# followed by a blank line.

# function example without arguments and and parameters and its a normal function
# def yz():
#     print(20+10)
# yz()


# user input function example
# a=int(input("enter the number:"))
# b=int(input("enter the number:"))
# def xyz(x,y):
#     c=x+y
#     print(c)
# xyz(a,b)

# after exceuting the xyz then automatically it will ask for the input of a and b and
# then it will print the sum of a and b after it gets disapeared the the c after print(c) will be printed.


## function with arguements and return type
# a=int(input("enter the number:"))
# b=int(input("enter the number:"))
# def xyz(x,y):
#     c=x+y
#     print(c)
#     return c
# c=xyz(a,b)
# print(c) 

# def abc(*xyz):
#     print(xyz)
# abc(1,2,3,4,5,6,7,8,9,10)    

# def abc(*xyz):
#     # print(xyz)
#     for i in xyz:
#         print(i)    
# abc(1,2,3,4,5,6,7,8,9,10) 




# dictinary type example
# def abc(**a):
#    print(a)
# abc(name="varsha", age=25, location="pune")

# tuple type example
def abc(*a):
    print(a)
abc(1,2,3,4,5,6,7,8,9,10)