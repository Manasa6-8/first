# -*- coding: utf-8 -*-
"""python_basics.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1we9QbdwaV5_GIREO8R4GZl8Q3KOTu6fS
"""

#data types and variables
my_int=42
print("Original Integer:",my_int)

#Demo of list
my_list=[1,"hello",2,2.13,True]
print("Original list:",my_list)
my_list.append("word")
print("Updated list:",my_list)
my_list.remove(2)
print("Updated list:",my_list)

#Demo for Tuple
a=(1,2,3,4,5)
print(a)
print(a)
print("First element:",a[0])
print("Last element:",a[-1])

#Demo for set:
a={1,2,3,4,5,"hello","hi"}
print(a)
a.add(6)
print(a)
a.remove(2)
print(a)
a.pop()

#Demo of loops in python
for i in range(1,6):
		print(i)

num=int(input("Enter a number"))
if num>0:
	print("numbers is positive")
elif num==0:
	print("number is zero")
else:
	print("the number is negative")

def greet(name):
  print("Hello,",name,"!")
greet("Alice")