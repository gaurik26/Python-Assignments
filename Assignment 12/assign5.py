# Write a program which accepts one number and prints that number in reverse order.
# input: 5
# output: 54321

no =  int(input())

for i in range(no,0,-1):
    print(i , end=" ")
