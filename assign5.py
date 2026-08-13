# Write a lambda function using reduce() which accepts a list of numbers and returns the maximum elements 

from functools import reduce

maximum = lambda x,y: max(x,y)

def main():

    data = []

    number = int(input("Enter how many numbers:"))

    for i in range(number):
        no = int(input())
        data.append(no)

    print(data)

    Result = reduce(maximum,data)

    print(Result)

if __name__ == "__main__":
    main()
    