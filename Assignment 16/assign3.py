# Write a program which contains one function named as Add() which accepts two numbers from user and return 
# addition of that two number.

def Add():

    num1 = int(input("Enter 1st number : "))
    num2 = int(input("Enter 2nd number : "))

    return num1 + num2


def main():
    Ret = Add()
    print(Ret)

if __name__ == "__main__":
    main()
