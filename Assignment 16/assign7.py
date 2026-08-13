# Write a program which contains one function that accept one number from user and returns true if number is divisible by 5 otherwise return false .

def div():

    number = int(input("Enter a number : "))
    if number % 5 == 0:
        return True
    else:
        return False

def main():

    Ret = div()
    print(Ret)

if __name__ == "__main__":
    main()