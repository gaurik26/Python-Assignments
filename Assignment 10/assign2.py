#write a program which accepts one number and print sum of first N natural numbers 
#input = 5
#1+2+3+4+5 = 15

no = int(input())

sum = 0

for i in range(1, no+1): #1,2,3,4,5
    sum = sum + i

print(sum)