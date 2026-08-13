# Write a program which accept one number from user and return adddition of its factors.


def factor(num):
    add = 0

    for i in range(1, num + 1):   # for i in range(1,13)
        if num % i == 0:          # if 12 % 1 = 0, 12 % 2=0 , 12 % 3 = 0... 
            add = add + i

    return add

def main():
    
    number = int(input("Enter a number : "))   #12

    Result = factor(number)

    print("Factors of number is",Result)

if __name__ == "__main__":
    main()
