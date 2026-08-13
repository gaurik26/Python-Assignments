#write a program which accepts one number and prints count of digits in that number .
# we are not using for loop because here there is no sequence
# // 10 gives the quotient (how many complete groups of 10).
# % 10 gives the remainder (the last digit).
# % 10 extracts the last digit means remainder of the number when divided by 10.
# // 10 removes the last digit means quotient of the number when divided by 10.
'''| Division  | Quotient (`//`) | Remainder (`%`) |
| --------- | --------------: | --------------: |
| 7 ÷ 10    |               0 |               7 |
| 15 ÷ 10   |               1 |               5 |
| 28 ÷ 10   |               2 |               8 |
| 123 ÷ 10  |              12 |               3 |
| 4567 ÷ 10 |             456 |               7 |
| 9999 ÷ 10 |             999 |               9 |
'''

'''| Human                             | Computer (Integer)                    |
| --------------------------------- | ------------------------------------- |
| Sees `12345` as **1, 2, 3, 4, 5** | Sees `12345` as **one numeric value** |
| Can count digits by looking       | Must use operations like `//` and `%` |
| Recognizes each digit visually    | Doesn't automatically separate digits |
'''

no = int(input())  #12345
count = 0

while no > 0:
    count = count + 1
    no = no // 10  
  #no value will change after every loop and that value will get in while condition 
    
print(count)