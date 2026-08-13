# Write a lambda function which accept one number and return true if number is odd otherwise false.

'''def is_even()
    if no % 2 != 0:
        print("Odd")
    else:
        print("Even")'''


num = int(input())

is_odd = lambda no : (no % 2 != 0)

Ret = is_odd(num)

print(Ret)