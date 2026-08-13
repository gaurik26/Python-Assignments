#write a program which accepts one number and prints factorial of that number 
#4! = 4*3*2*1

no = int(input())

fact = 1

for i in range(1, no+1): #1,2,3,4,5
    fact = fact * i

print(fact)