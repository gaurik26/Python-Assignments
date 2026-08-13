# Write a program which accept N numbers from user and store it into List.
# Return addition of all elements from that list .
# Input : 6
# Input Elements : 13 5 45 7 4 56
# output : 130

def add(data):
    # Store the running total of all list elements
    sum = 0

    # Take each element from the list one by one
    for no in data:
        # Add the current element to the running total
        sum = sum + no

    # Send the final addition back to the function call
    return sum

def main():
    # Ask the user how many numbers they want to enter
    number = int(input("Enter the number of elements: "))

    # Create an empty list to store user-entered numbers
    in_list = []

    # Run the loop 'number' times to accept all elements
    for i in range(number):
        # Accept one number from the user
        no = int(input("Enter a number: "))

        # Add the entered number to the list
        in_list.append(no)

    # Display all elements stored in the list
    print("Input elements are:", in_list)

    # Call add() and store the returned sum in 'ret'
    ret = add(in_list)

    # Display the final addition
    print("Addition of the list is:", ret)


# Start the program by calling main()
if __name__ == "__main__":
    main()



