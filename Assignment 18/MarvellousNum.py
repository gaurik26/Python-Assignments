#Accept N numbers from the user.
#Store those numbers in a list.
#Check each number whether it is prime or not.
#For checking prime, use a function called ChkPrime().
#ChkPrime() must be inside a separate user-defined module called MarvellousNum.py.
#From the main Python file, create a function called ListPrime().
#ListPrime() should find all prime numbers and return their addition/sum.

def ChkPrime(no):
    count = 0
    for i in range(1,no+1):    # ex: num = 13 , range(1,14) , 1,2,3,4,5.....13
        if no % i == 0:        # 13 % 1 == 0 , 13 % 2 == 1,.....
            count = count + 1   
    if count == 2:
        return no
    else:
        return False
