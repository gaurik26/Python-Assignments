# Write a lambda function using filter() which accepts a list of numbers and return the count of even numbers .

count = lambda x : (x%2==0)

def main():

    data = []

    number = int(input("Enter how many numbers: "))

    for i in range(number):
        no = int(input())
        data.append(no)

    print(data)

    result = len(list(filter(count,data)))
    print(result)

if __name__ == "__main__":
    main()