# Write a lambda which accepts one number and return cube of that number 

'''def cube(a):
    return a*a*a'''

num = int(input())
cube  = lambda x : x ** 3
Ret = cube(num)
print(Ret)