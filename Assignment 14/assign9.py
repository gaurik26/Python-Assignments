# Write a lambda function which accepts two numbers and return multiplication.

'''def add(a,b)
    return a * b'''

num1 = int(input())
num2 = int(input())

add = lambda x,y : x*y

Ret = add(num1 , num2)
print(Ret)