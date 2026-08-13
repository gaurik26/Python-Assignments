# Write a lambda function using reduce() which accepts a list of numbers and return the product of all the elements

# Import the reduce() function from the functools module
from functools import reduce

# Lambda function to add two numbers
product = lambda x, y: x * y

def main():

    # Create an empty list to store the user-entered numbers
    data = []

    # Accept how many numbers the user wants to enter
    number = int(input("Enter how many numbers: "))

    # Repeat 'number' times to accept input from the user
    for i in range(number):

        # Accept one number from the user
        no = int(input())

        # Add the entered number to the list
        data.append(no)

    # Display the original list
    print(data)

    # Use reduce() to add all the elements of the list
    result = reduce(product, data)

    # Display the final sum
    print(result)

# Call the main() function only when this file is run directly
if __name__ == "__main__":
    main()