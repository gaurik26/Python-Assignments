# Write a lambda function using map() which accepts a list of numbers and returns a list of squares of each number

square = lambda x: x ** 2

def main():

    # Accept how many numbers the user wants to enter
    number = int(input("Enter how many numbers: "))

    # Create an empty list to store the input numbers
    data = []

    # Repeat 'number' times to take input from the user
    for i in range(number):         # for i in range(5):

        # Accept one number from the user
        no = int(input())

        # Add the entered number to the list
        data.append(no)

    # Display the complete list
    print(data)

    result = list(map(square,data))
    print(result)


# Call the main() function only when this file is run directly
if __name__ == "__main__":
    main()