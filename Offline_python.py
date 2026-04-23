# 1. Write a python program to remove the duplicate in given list.
#                 a = [2,3,4,2,3,4,5,7]
#                 output: [2,3,4,5,7]

a= [2,3,4,2,3,4,5,7]
def remove_duplicate(a):
    b=[]
    for i in a:
        if i not in b:
            b.append(i)
    return b
print(remove_duplicate(a))

# 2. Write a program that takes array of numbers as input, among the numbers in array,
# print the numbers which forms a prime number by adding one to it. 
# Print such numbers in the given array separated b spaces.

#               Testcase1	:  [ 7, 4, 7, 23, 10, 6]
#                Output     	:  4 10 6

# a = list(map(int, input("Enter the numbers: ").replace(',', ' ').split()))
# def p(a):
#     b=[]
#     for i in a:
#         if i%2==0:
#             b.append(i)
#     return b
# print(p(a))
# 3. Write python program 
#               a   = " aaabbaaccdd"
#              output: "a5b2c2d2"

a= " aaabbaaccdd"
def c(a):
    b=""
    for i in a:
        if i not in b:
            b=b+i+str(a.count(i)) 
    return b
print(c(a))
