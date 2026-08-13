# Write a program which accepts one number and display below pattern:
# Outer loop = usually controls rows
# Inner loop = usually controls columns/items in that row
# Outer loop starts one row
#    ↓
# Inner loop fills that row
#    ↓
# print() moves to next row
# How many rows? → controls your outer loop range
# In row i, how many things do I print? → controls your inner loop range
# What do I print each time? → star? number? space? j? i?
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5

'''Big loop = How many lines? 
Small loop = How many things on each line? 
print() = Go to the next line '''

number = int(input("Enter a number : "))

for row in range(1 , number+1):
    for num in range(1, number+1):
        print(num , end=" ")
    print()

