#Write a program which accepts one number and prints sum of digits 

no = int(input()) #123
ans = 0

while no > 0:
    rem = no % 10
    ans = ans + rem
    quotient = no // 10
    no = quotient    # This is because // only returns a value. It doesn't change the variable by itself.

print(ans)





