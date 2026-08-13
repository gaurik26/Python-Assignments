# Write a program which accept number from user and return addition of digits in that number 
# input: 5187934    output:37

def add(num):
    temp = 0
    while num > 0:

        remainder = num % 10 # extract the last digit of number 

        temp = remainder + temp

        num = num // 10 # remove the last value 

    return temp

def main():

    number = int(input("Enter a number : ")) # 5187934

    result = add(number)

    print(result)

if __name__ == "__main__":
    main()