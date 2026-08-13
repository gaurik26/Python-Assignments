# Write a lambda function which accepts two numbers and return maximum of those two numbers

'''def maximum(a,b):
    if a>b:
        print(a)
    else:
        print(b)'''


num1 = int(input())
num2 = int(input())

maximum = lambda x,y : max(x,y)

Ret = maximum(num1,num2)
print(Ret)