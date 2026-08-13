# write a program which accept one number from user and return its factorial.

def factor(num):

    fact = 1

    for i in range(1, num + 1):      # for i in range(1,5)
        fact = fact * i

    return fact

def main():
    number = int(input("Enter a number : "))   #5

    Result = factor(number)

    print("Factorial of", number, "is", Result)

if __name__ == "__main__":
    main()