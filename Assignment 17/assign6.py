# Write a program which accepts one number and display below pattern.
# * * * * *
# * * * *
# * * *
# * *
# *

number = int(input("Enter a number."))

for i in range(number, 0, -1):
    for j in range(i):
        print("*", end="")
    print()

'''for i in range(number):
    for j in range(number-1):
        print(j,end = " ")
    print(i)'''
