# Write a program which accept one number and display below pattern:
'''
*****
*****
*****
*****
*****
'''

def star(num):
    for row in range(num):

        # Repeat 5 times to print 5 stars in the current row
        for star in range(num):

            # Print a star on the same line
            print("*", end="")

        # Current row is complete, so move to the next line
        print()


def main():
    
    number = int(input("Enter a number: "))

    star(number)

if __name__ == "__main__":
    main()