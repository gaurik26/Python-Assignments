# Write a lambda function using filter() which accepts a list of numbers and returns a list of even numbers.

is_even = lambda x : (x%2==0)

def main():

    number = int(input("Enter how many numbers: "))

    data = []

    for i in range(number):
        no = int(input())
        data.append(no)

    print(data)
    result = list(filter(is_even,data))  #filter(function_name,Iterables)
    print(result)


if __name__ == "__main__":
    main()