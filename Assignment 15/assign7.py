# Write a lambda function using filter() which accepts a list of strings and return a list of strings having length greater than 5 .

name = lambda x : (len(x) > 5)

def main():

    data = []

    num = int(input("Enter number or string you want in list"))

    for i in range(num):
        char = input()
        data.append(char)

    print(data)

    Result = list(filter(name,data))

    print(Result)

if __name__ == "__main__":
    main()