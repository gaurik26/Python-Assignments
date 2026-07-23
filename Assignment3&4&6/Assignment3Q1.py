def mulfun():
    print("Enter any 2 number to perform their multiplication")
    No1 = int(input("Enter first number: "))
    No2 = int(input("Enter second number:"))
    Ret = No1 * No2
    print(f"Multiplication of {No1} and {No2} is {Ret}")

def main():
    mulfun()
    
if __name__ == "__main__":
    main()