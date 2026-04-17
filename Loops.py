# Using for loop find even and sum, product range between 1 to 10

# def sum_of_Even():
#     sum=0
#     for i in range(1,11):
#         if i%2==0:
#             sum+=i
#     return sum
# print(sum_of_Even())

# Using while loop find even and sum, product range between 1 to 10
def sum_of_even():
    total=0
    i=1
    while i<=10:
        if i%2==0:
            total+=i
        i+=1
    return total
print(sum_of_even())    
# Print -1 to -100 and -100 to -1 using for loops

def print_negative():
    for i in range(-1,-101,-1):
        print(i,end=" ")
    print()
    for i in range(-100,0):
        print(i,end=" ")