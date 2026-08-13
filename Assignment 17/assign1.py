# create one module named as Arithemetic which contains 4 functions as Add() for 
# addition , sub() for substraction ,Mult() for multiplication and Div() for Division 
# All functions accepts two parameters as number and perform the operation ,
# Write one python program which call all the function from Arithmetic module
#  by accepting the parameters from user.


import Arithemetic as ari

def main():

    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter second number: "))

    Result = ari.Add(num1,num2)
    Result1 = ari.sub(num1,num2)
    Result2 = ari.Mult(num1,num2)
    Result3 = ari.Div(num1,num2)

    print(Result)
    print(Result1)
    print(Result2)
    print(Result3)

if __name__ == "__main__":
    main()