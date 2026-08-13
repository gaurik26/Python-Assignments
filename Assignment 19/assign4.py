# Write a program which contains filter(), map() and reduce() in it . Python application which contains 
# one list of numbers . List contains the numbers which are accepted from user .
# Filter should filter out all such numbers which are Even.Map function will calculate its square . 
# Reduce will return addition of all that numbers 

from functools import reduce

def filternumber(u_list):

    filterlist = list(filter(lambda u : u % 2 == 0 , u_list ))
    return list(filterlist)

def map_cal(I_list):

    increase = list(map(lambda i : i*i , I_list))
    return list(increase)

def reduce_prd(R_prd):

    reduce_l = reduce(lambda n1 ,n2 : n1 + n2 , R_prd)
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

    FResult = filternumber(user_list)

    print(FResult)

    MResult = map_cal(FResult)

    print(MResult)

    RResult = reduce_prd(MResult)

    print(RResult)

if __name__ == "__main__":
    main()