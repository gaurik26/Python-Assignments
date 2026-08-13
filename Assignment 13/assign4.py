# Write a program which accepts one number and prints binary equivalent .
# Divie the number by 2 and store the remainder in a list. Repeat the process until the number becomes 0. 
# Finally, reverse the list and print the binary equivalent.Read the remainder from bottom to top 
# input : 13  for example to find binary of 13
# 13 % 2 = 1 remainder 1
# 6 % 2 = 0 remainder 0
# 3 % 2 = 1 remainder 1
# 1 % 2 = 1 remainder 1
# Reading from bottom to top gives 1101.

no = int(input())  # 13

while no > 0:

    quotient = no // 2
    remainder = no % 2

    print(remainder, end='')

    no = quotient