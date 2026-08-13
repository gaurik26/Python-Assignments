# // 10 gives the quotient (how many complete groups of 10).
# % 10 gives the remainder (the last digit).
# % 10 extracts the last digit means remainder of the number when divided by 10.
# // 10 removes the last digit means quotient of the number when divided by 10.
# Write a program whcih accepts one nmber and prints reverse of that number. For example if the input is 12345 then the output should be 54321.
no = int(input()) #12345
ans = 0

while no > 0:
    rem = no % 10 #5
    ans = ans * 10 + rem #0*10+5=5, 5*10+4=54, 54*10+3=543, 543*10+2=5432, 5432*10+1=54321
    quotient = no // 10 #1234
    no = quotient    # This is because // only returns a value. It doesn't change the variable by itself.
print(ans)