# Write a lambda function which accept one number and return true if number is even otherwise false.

'''def is_even()
    if no % 2 == 0:
        print("Even")
    else:
        print("Odd)'''


num = int(input())

is_even = lambda no : (no % 2 == 0)

Ret = is_even(num)

print(Ret)