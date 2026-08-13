# Write a program which accept N numbers from user and store it into list.
# Accept one another number from user and return frequency of that number from List.

# Input : Number of elements :11
# Input elements : 13 5 45 7 4 56 5 34 2 5 65
# Element to search : 5
# output: 3

def Display(num):

    count = 0
    in_list = []
    
    for i in range(num):
        no = int(input())
        in_list.append(no)
    
    print("Input elements are:",in_list)
    
    no = int(input("Element to search : "))
    
    for n in in_list:
        if n == no:
            count = count + 1
                
    return count
        
def main():

    number = int(input("Enter a number : ")) # number = 6

    Ret = Display(number)

    print("Frequency of the number in the list is : ",Ret)

if __name__ == "__main__":
    main()
