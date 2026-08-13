# Write a program which contains one lambda function which accepts two parameters and return its multiplication.
# Input : 4   3      output : 12
# Input : 6   3      output : 18

mul = lambda x,y:(x*y)

def main():
    num1 = int(input("Enter any 1st number for multiplication: "))
    num2 = int(input("Enter any 2nd number for multiplication: "))

    Ret = mul(num1 , num2)
    print(Ret)

if __name__ == "__main__":
    main()