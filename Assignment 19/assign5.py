# Write a program which contains filter(), map() and reduce() in it . Python application which contains 
# one list of numbers . List contains the numbers which are accepted from user .
# Filter should filter out all such numbers which are Prime .Map function will multiply each number by 2. 
# Reduce will return maximum of all that numbers 

from functools import reduce

def is_prime(num):

    for i in range(2 ,num):
        if num % i==0:
            return False

    return True

def map_cal(I_list):

    increase = list(map(lambda i : i*2 , I_list))
    return list(increase)

def reduce_prd(R_prd):

    reduce_l = reduce(lambda n1 ,n2 : max(n1,n2) , R_prd)
    return reduce_l 

def main():

    user_list = []
    filter_list = []
    number = int(input("Enter a number of Elements you want in a list : ")) # 10
    
    print("Enter the elements you want in list : ")

    for no in range(number):
        Element = int(input())

        user_list.append(Element)

    print("List :",user_list)

    FResult = list (filter(is_prime,user_list))

    print(FResult)

    MResult = map_cal(FResult)

    print(MResult)

    RResult = reduce_prd(MResult)

    print(RResult)

if __name__ == "__main__":
    main()