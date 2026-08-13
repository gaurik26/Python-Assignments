# Write a program which accepts one number and check weather it is perfect number or not.
# input : 6   output : perfect number
sum = 0
no = int(input())   #10

for i in range(1, no):  # 1,2,3,4,5,6,7,8,9
    if no % i == 0:     #1 % 10 == 0, 2 % 10 == 0, 3%10 == 1, 4%10 == 2, 5%10 == 0, 6%10 == 4, 7%10 == 3, 8%10 == 2, 9%10 == 1, 10%10 == 0
           sum = sum + i # sum = 0 + 1 = 1, sum = 1 + 2 = 3, sum = 3 + 5 = 8, sum = 8 + 10 = 18

if sum == no:
    print("Perfect number")
else:
    print("Not a perfect number")
