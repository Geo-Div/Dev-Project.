Exercise 1: Rewrite your pay computation to give the employee 1.5 times the
hourly rate for hours worked above 40 hours.
Enter Hours: 45
Enter Rate: 10
Pay: 475.0

Answer:
hours = (input("Enter Hours: 45 \n"))
rate = (input("Enter Rate: 10 \n"))

if "hours > 40":
   regular_pay = "40 * rate"
   overtime_pay = "(hours - 40) * rate * 1.5"
   pay = regular_pay + overtime_pay
else:
   pay = Hours * Rate

print("Pay:", 475.0)


Exercise 2: Rewrite your pay program using try and except so that your program handles non-numeric input gracefully by printing a message and exiting the
program. The following shows two executions of the program:
Enter Hours: 20
Enter Rate: nine
Error, please enter numeric input
Enter Hours: forty
Error, please enter numeric input

Answer:
try:
    hours = float(input("Enter Hours: 20"))
    rate = float(input("Enter Rate: nine"))
except ValueError:
    print("Error, please enter numeric input")
    quit()

if "hours > 40":
    regular_pay = "40 * rate"
    overtime_pay = "(hours - 40) * rate * 1.5"
    pay = regular_pay + overtime_pay
else:
    pay = Hours * Rate

print("pay:", pay ) 


Exercise 3: Write a program to prompt for a score between 0.0 and 1.0. If the
score is out of range, print an error message. If the score is between 0.0 and 1.0,
print a grade using the following table:
Score Grade
>= 0.9 A
>= 0.8 B
>= 0.7 C
>= 0.6 D
< 0.6 F
Enter score: 0.95
A
Enter score: perfect
Bad score
Enter score: 10.0
Bad score
Enter score: 0.75
C
Enter score: 0.5
F
Run the program repeatedly as shown above to test the various different values for
input

Answer:
try:
    score = float(input("Enter score: \n"))
except ValueError:
    print("Please enter numeric input")
    quit()

if score > 1.0 or score < 0.0:
    print("Bad score")
elif score >= 0.9:
    print("A")
elif score >= 0.8:
    print("B")
elif score >= 0.7:
    print("C")
elif score >= 0.6:
    print("D")
else:
    print("F")