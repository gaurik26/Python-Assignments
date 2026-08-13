# Write a lambda function using reduce() which accepts a list of numbers ans returns the minimum elements# Write a lambda function using reduce() which accepts a list of numbers and returns the maximum elements 

from functools import reduce

minimum = lambda x,y: min(x,y)

def main():

    data = []

    number = int(input("Enter how many numbers:"))

    for i in range(number):
        no = int(input())
        data.append(no)

    print(data)

    Result = reduce(minimum,data)

    print(Result)

if __name__ == "__main__":
    main()
    