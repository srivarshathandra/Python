# ASSIGNMENT



Date : 27-04-2026 
Tech stack :Python
Topic:: List And Tuple
Task : 

Method: append()

EASY QUESTIONS

1. What happens to the length of a list after calling the append() method?
answer: Append() is a method in List that is used to adds exactly one element to the end of the list.

before append: arr = [10, 20, 30]
               len(arr)  # 3

After append: arr.append(40)
              len(arr)  # 4  ---Length increased by +1

-----Python lists are dynamic arrays: They can grow in size When you use append(),
Python: Finds the end of the list then Inserts the new element,Updates the size
No matter what you pass (number, string, list, object) . It is treated as one single item

2.Where is the new element placed when you use list.append(x)?

Answer: When you use list.append(x), the new element is placed at the end of the list.


arr = [1, 2, 3]
arr.append(4)

print(arr)

o/p:[1, 2, 3, 4]

append() never inserts in the middle
It always adds at the last position
The existing elements stay in the same order
The new element x is added after the last element

[1, 2, 3]
         ↑ end

After append(4):


[1, 2, 3, 4]
            ↑ new element


3. Write a simple line of code to add the string 'apple' to a list named 'fruits'.

answer: fruits.append("apple")


MEDIUM QUESTIONS

4. If you append a list [10, 20] to an existing list [1, 2], what is the total number of elements in the final list?

arr = [1, 2]
arr.append([10, 20])

o/p: [1, 2, [10, 20]]       --Total elements = 3,Because [10, 20] is treated as one single object (a list)

5. Explain the difference in result between list.append([5, 6]) and list + [5, 6].

arr = [1, 2]

arr.append([5, 6])             # → [1, 2, [5, 6]]
arr + [5, 6]                   # → [1, 2, 5, 6]

append() → adds one item

+ → combines lists (adds elements individually)
  


EASY QUESTIONS-Method: extend()

6. Does the extend() method add elements individually or as a single nested object?

>> extend() adds elements individually, not as a nested object.

When you use extend(), Python iterates through the input and adds each element one by one to the list.

>> arr = [1, 2]
   arr.extend([3, 4])
   print(arr)

o/p: [1, 2, 3, 4]

>> [3, 4] is an iterable and extend() takes each element (3 and 4).....Adds them separately

7. What type of argument (e.g., integer, iterable) does the extend() method expect?

The extend() method expects an iterable as its argument.

An iterable is anything you can loop over.

Examples:
list ✅
tuple ✅
string ✅
set ✅
range ✅

arr = [1, 2]

arr.extend([3, 4])      # list
arr.extend((5, 6))      # tuple
arr.extend("78")        # string

print(arr)

o/p: [1, 2, 3, 4, 5, 6, '7', '8']
The extend() method expects an iterable (like list, tuple, string), not a single value like an integer.

8. How do you merge list B into list A using extend()?

You merge list B into A using:

A.extend(B)

ex: A = [1, 2]
    B = [3, 4]
    A.extend(B)
    print(A)
o/p:[1, 2, 3, 4]

extend() takes each element from B,Adds them one by one into A and the original list A is modified.

MEDIUM QUESTIONS

9. Predict the output: my_list = [1, 2]; my_list.extend('34'); print(my_list).

 output is [1, 2, '3', '4']

 my_list = [1, 2]
my_list.extend('34')
'34' is a string, and strings are iterable
So extend() takes each character:
'3' '4'

It adds them one by one to the list. extend() treats the string as an iterable and adds each character separately.

10. What is the difference between extend() and the += operator for lists, if any?
For lists, extend() and += behave almost the same — both add elements individually to the existing list.
a = [1, 2]

b = [3, 4]

a.extend(b)


print(a)   # [1, 2, 3, 4]

a = [1, 2]

b = [3, 4]

a += b

print(a)   # [1, 2, 3, 4]

they both contains same result. so, There is no major difference—both add elements individually and modify the list in-place.
extend() is a method, while += is an operator.


Method: insert()
EASY QUESTIONS

11. How many arguments does the insert() method take?

The insert() method takes 2 arguments.

syntax : list.insert(index, element)

index → where to insert
element → what to insert

example:
arr = [1, 2, 3] 

arr.insert(1, 100)

print(arr)

output:  [1, 100, 2, 3]

--- insert() takes 2 arguments: index and element

12. If you want to add an element at the very beginning of a list, what index should you use in
insert()?

Use index 0 to insert an element at the beginning of a list

arr = [1, 2, 3]

arr.insert(0, 100)

print(arr)

Output:
[100, 1, 2, 3]

Index 0 represents the first position in a list
So inserting at 0 pushes all existing elements to the right


13. Does insert() replace the existing element at the given index or shift it?

insert() does not replace the existing element — it shifts elements to the right.

arr = [1, 2, 3]

arr.insert(1, 100)


print(arr)

output:
[1, 100, 2, 3]

You inserted 100 at index 1
The original element at index 1 (2) is not removed
It gets shifted to the right

insert() shifts existing elements to the right; it does not replace them

MEDIUM QUESTIONS


14. What happens if you use a negative index, like list.insert(-1, 'x'), on a list of 3 items?

Using list.insert(-1, 'x') inserts the element just before the last element.

arr = [1, 2, 3]

arr.insert(-1, 'x')

print(arr)

output:
[1, 2, 'x', 3]

Index:   0   1   2

List:   [1,  2,  3]

insert(-1, 'x') → before index 2

Negative index -1 refers to the position before the last element
So 'x' is inserted before 3
Existing elements are shifted to the right

It inserts the element just before the last element, shifting elements to the right


15.In terms of performance, why is insert(0, x) considered slower than append(x) for large lists?

insert(0, x) is slower because it has to shift all existing elements, while append(x) just adds to the end.

arr = [1, 2, 3, 4]

arr.insert(0, 100)

[1, 2, 3, 4]

→ shift all → [_, 1, 2, 3, 4]
→ insert → [100, 1, 2, 3, 4]               ----Every element moves → more work


append at end

arr.append(100)

[1, 2, 3, 4] → [1, 2, 3, 4, 100] --no shifting needed

insert(0, x) is slower because it shifts all elements to the right (O(n)), while append(x) adds directly at the end (O(1))
