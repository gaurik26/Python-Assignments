# Write a program which accept number from user and return number of digits in that number 
# input: 5187934    output:7

def counter(num):
    count = 0
    while number > 0:

        remiander = number % 10

        count = count + 1

        number = number // 10

    return count

def main():
    number = int(input("Enter a number : "))
    result = counter(number)

if __name__ == "__main__":
    main()