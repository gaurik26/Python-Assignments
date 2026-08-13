# Write a lambda function which accept one number and return true if divisible by 5.

'''def is_div()
    if no % 5 == 0:
        print("True")'''


num = int(input())

is_div = lambda no : (no % 5 == 0)

Ret = is_div(num)

print(Ret)