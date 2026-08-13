# Write a program which accepts number from user and print that number of " * " on screen 

def star():
    
    number = int(input("Enter a number : "))
    
    for i in range(number):
        print("*",end=" ")

def main():

    star()

if __name__ == "__main__":
    main()