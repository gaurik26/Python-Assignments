import sys

a = input("Enter a value: ")
if a.isdigit():
    a = int(a)
    
print("datatype of a:", type(a))
print("memory address of a is :",id(a))
print("Size of a is :",sys.getsizeof(a))
