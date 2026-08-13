# Write a program which accepts one number and check whether it is palindrome or not

original = int(input()) #121
reverse = 0
ans = original

while ans > 0:
    rem = ans % 10 
    reverse = reverse * 10 + rem
    ans = ans // 10

if original == reverse:
    print("It is palindrome")
else:
    print("It is not palindrome")

        



