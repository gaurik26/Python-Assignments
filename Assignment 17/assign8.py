# Write a program which accept one number and display below pattern:
#1
#1 2
#1 2 3
#1 2 3 4
#1 2 3 4 5

number = int(input("Enter a number: "))

for row in range(1,number+1):        # # Outer loop controls the number of rows
    for num in range(1 ,row+1):      # # Inner loop prints numbers from 1 up to the current row number
        print(num,end = " ")
    print()