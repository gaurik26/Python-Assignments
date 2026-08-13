# Write a program which accept N numbers from user and store it into List.
# Return Minimum number from that list.

# Input : Number of element :7
# Input elements : 13 5 45 7 4 56 34 
# output : 4

def Display(Data):

    minimum = Data[0]
    
    # Take each element from the list one by one
    for no in Data:

        if minimum > no:
            minimum = no

    return minimum

def main():

    number = int(input("Enter a number : ")) # number = 6

    in_list = []

    for i in range(number):
        no = int(input())
        in_list.append(no)

    print("Input elements are:",in_list)

    ret = Display(in_list)

    print("Minimum number from the list is : ",ret)


if __name__ == "__main__":
    main()
