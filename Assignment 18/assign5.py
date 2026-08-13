# Write a program which accept N numbers from user and store it into list. 
# Return adddition of all prime numbers from that list .
# Main python file accepts N numbers from user and pass each number to ChkPrime()
# function which is part of our user defined module named as MarvellousNum. 
# Name of the function from main python file should be ListPrime().

#Accept N numbers from the user.
#Store those numbers in a list.
#Check each number whether it is prime or not.
#For checking prime, use a function called ChkPrime().
#ChkPrime() must be inside a separate user-defined module called MarvellousNum.py.
#From the main Python file, create a function called ListPrime().
#ListPrime() should find all prime numbers and return their addition/sum.

import MarvellousNum as mp

def ListPrime(final):
    add = 0
    for no in final:
        add = no + add

    print(add)

def main():

    number = int(input("Enter Number of Elements : ")) # 11 

    num_list = []      # 13 5 45 74 56 10 34 2 5 8
    num_prime = []

    for i in range(number):
        no = int(input())
        num_list.append(no)

    print(num_list)    # 13 5 45 74 56 10 34 2 5 8

    for n in num_list:
        result = mp.ChkPrime(n) 
        if result != False:
            num_prime.append(result)

    print(num_prime)

    ListPrime(num_prime)
        
if __name__ == "__main__":
    main()