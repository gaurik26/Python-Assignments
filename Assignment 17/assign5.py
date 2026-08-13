# Write a proram which accept one number for user and check whether it is prime or not .
# 2 is the only prime number 
# 

def is_prime(num):
    if num > 1:
        for i in range(2,num):
            if num % i == 0:
                return "It is not a prime number."
            else:
                return "It is a prime number."
            
def main():
    number = int(input("Enter a number : "))

    Result = is_prime(number)

    print(Result)

if __name__ == "__main__":
    main()

