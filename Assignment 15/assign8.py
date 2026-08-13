# Write a lambda function using filter() which accepts the list of numbers and returns the list of numbers divisible by both 3 and 5.

div = lambda x : (x % 3 == 0 and x % 5 == 0)

def main():

    data = []

    number = int(input("Enter a number : "))

    for i in range(number):
        no = int(input())
        data.append(no)

    print(data)

    Result = list(filter(div,data))
    print(Result)


if __name__ == "__main__":
    main()