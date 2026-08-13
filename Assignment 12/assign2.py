# Write a program which accepts one number and prints its factors 
# input : 12    output : 1,2,3,4,6,12

no = int(input())

for i in range(1,no+1):
    if no % i == 0:
        print(i)
