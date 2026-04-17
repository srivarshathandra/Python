# Using for loop find even and sum, product range between 1 to 10

# def sum_of_Even():
#     sum=0
#     for i in range(1,11):
#         if i%2==0:
#             sum+=i
#     return sum
# print("The sum of even numbers between 1 and 10 is:",sum_of_Even())

#  checking the num is palindrome or not using conditional statement

number=int(input("Enter a number: "))
rev=0
t=number
while t>0:
    rev=rev*10+t%10
    t//=10
    if number==rev:
        print("The number is a palindrome")
    else:        
        print("The number is not a palindrome")    
