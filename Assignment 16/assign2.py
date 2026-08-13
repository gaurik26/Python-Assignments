# Write aprogram which contains one function named as ChkNum() which accept one parameter as number. If number is even then it should display "Even number" otherwise display "odd number" on console.

def ChkNum(num):
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")


def main():
    number = int(input("Enter the number: "))
    ChkNum(number)


if __name__ == "__main__":
    main()