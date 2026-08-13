# Write a lambda function which accepts two numbers and return minimum of those two numbers

'''def maximum(a,b):
    if a>b:
        print(a)
    else:
        print(b)'''


num1 = int(input())
num2 = int(input())

minimum = lambda x,y : min(x,y)

Ret = minimum(num1,num2)
print(Ret)