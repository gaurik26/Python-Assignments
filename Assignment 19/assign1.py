# Write a program which contains one lambda function which accepts one parameter and return power of two.
# Input : 4        output:16
# Input : 6        output : 64


pow = lambda no : (no ** 2)
    
def main():
    number = int(input("Enter a number : "))

    Ret = pow(number)

    print(Ret)

if __name__ == "__main__":
    main()