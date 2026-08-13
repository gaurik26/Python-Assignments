# This program is to check whether the given number is prime or not
# The prime numbers are those numbers which are divisible by 1 and itself only.
# Other numbers are called composite numbers. The number 1 is neither prime nor composite.
# 2 is the only even prime number. All other even numbers are composite numbers.
# other than 2, all prime numbers are odd numbers. The first few prime numbers are 2,3,5,7,11,13,17,19,23,29
# We never check numner larger than the given number. We check only till the square root of the given number.- for 2nd program
# We can never divide a number by 0. So we start checking from 2 to the given number -1. If the number is divisible by any of these numbers, then it is not prime.
# We never check the number larger than the given number because they can never divide the number excactly. For example, 7 cannot be divided by 8,9,10,11,12,13,14,15,16,17,18,19,20. So we check only till the given number -1.

no = int(input())

prime = 0
# suppose no is 7
for i in range(2,no): # 2,3,4,5,6 = (2,7)
    if no % i == 0: #7%2=1, 7%3=1, 7%4=3, 7%5=2 , 7%6=1 = prime
        # 8%2=0
        prime = 1
        break

if no <= 1:
    print("Not prime")
elif prime == 1:
    print("Not prime")
else:
    print("Prime")


#########################################################
#instead of checking all prime number we used square root n 

'''no = int(input())    # prime numbers: 2,3,5,7,11,13,17,19,23,29
if no <= 2:
    print("Not prime")
else:
    for i in range(2,int(no**0.5)+1): # 2,3,4,5,6 = (2,7)
        if no % i == 0: #7%2=1, 7%3=1, 7%4=3, 7%5=2 , 7%6=1 = prime
            # 8%2=0
            print("Not prime")
            break
    else:
        print("Prime")'''