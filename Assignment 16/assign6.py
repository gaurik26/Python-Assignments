# Write a program which accept number from user and check whether that number is positive or negative or zero.

def number():
    number = int(input("Enter a number : "))
    
    if number > 0:
        print("Positive")
    elif number < 0:
        print("Negative")
    else:
        print("Zero")

def main():

    number()

if __name__ == "__main__":
    main()