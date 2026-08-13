# Write a lambda function which accepts three numbers and return largest number

num1 = int(input())
num2 = int(input())
num3 = int(input())

maximum = lambda x,y,z : max(x,y,z)

Ret = maximum(num1,num2,num3)
print(Ret)