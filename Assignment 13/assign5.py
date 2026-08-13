# Write a program which accepts marks and displays grade.
# >= 75 --> Distinction
# >= 60 --> First Class
# >= 50 --> Second Class
# < 50 --> Fail

marks = int(input("Enter your marks: "))

if marks >= 75:
    print("Grade: Distinction")
elif marks >= 60:
    print("Grade: First Class")
elif marks >= 50:
    print("Grade: Second Class")
else:
    print("Grade: Fail")