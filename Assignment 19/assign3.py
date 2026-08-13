# Write a program which contains filter(), map() and reduce() in it . Python application which contains 
# one list of numbers . List contains the numbers which are accepted from user .
# Filter should filter out all such numbers which greater than or equal to 70 and less than or equal to 90. 
# Map function will increase each number by 10 . Reduce will return product of all that numbers 

from functools import reduce

def filternumber(u_list):

    filterlist = list(filter(lambda u : u >= 70 and u <= 90 , u_list ))
    return list(filterlist)

def map_increase(I_list):

    increase = list(map(lambda i : i+10 , I_list))
    return list(increase)

def reduce_prd(R_prd):

    reduce_l = reduce(lambda n1 ,n2 : n1 * n2 , R_prd)
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

    MResult = map_increase(FResult)

    print(MResult)

    RResult = reduce_prd(MResult)

    print(RResult)

if __name__ == "__main__":
    main()